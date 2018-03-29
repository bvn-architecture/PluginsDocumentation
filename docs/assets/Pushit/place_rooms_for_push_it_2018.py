##### STANDARD ENVIRONMENT SETUP #####

import clr
import bvn

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

# Import Revit Utils extension methods
clr.AddReference(bvn.GetBvnVersionedAssembly("RevitUtil"))
import BVN.Revit.Util
clr.ImportExtensions(BVN.Revit.Util.Extensions)

import sys
sys.path.append(r"C:\DanScripting\PythonScripts\Miscellaneous")

# Import linq extension methods
clr.AddReference("System.Core")
import System
clr.ImportExtensions(System.Linq)

##### END STANDARD ENVIRONMENT SETUP #####

clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms

from System.Text import StringBuilder
from System import Guid

from newfuncs import MatchOnKeys, GetStringParameterValue, GetIntegerParameterValue, GetElementIdParameterValue, GetIndent, InTransactionWithResult

from utility import GetOneToManyMapping
import elements
import parameters

# Parameters to transfer

SP_ROOM_NUMBER_PARAMETER_ID = Guid.Parse("eef3dab4-4d17-494a-a1ea-547241ccdd8a")
REVIT_ROOM_NUMBER_PARAMETER_ID = Guid.Parse("eef3dab4-4d17-494a-a1ea-547241ccdd8a")

# Element utility functions

def GetElementName(element):
  return elements.GetName(element)

def GetElementLevel(element):
  doc = element.Document
  levelId = element.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM).AsElementId()
  return doc.GetElement(levelId)

def SetParameterValue(element, parameterId, value):
  result = False
  parameter = Element.get_Parameter(element, parameterId)
  if parameter is not None:
    result = parameter.Set(value)
  if result:
    result = parameters.GetValue(parameter) == value
  return result  

# Retrieve family instance-based 'rooms' from the document.

def HasSPRoomNumberParameter(element):
  return Element.get_Parameter(element, SP_ROOM_NUMBER_PARAMETER_ID) is not None

def GetColumnBasedRoomFamilyInstances(doc):
  columnBasedFamilyInstances = doc.GetElements[FamilyInstance](BuiltInCategory.OST_Columns)
  columnBasedRoomFamilyInstances = columnBasedFamilyInstances.Where(HasSPRoomNumberParameter)
  return list(columnBasedRoomFamilyInstances)

# Room parameter getters/setters

def GetParameterStringValue(element, paramName):
  value = None
  parameter = Element.get_Parameter(element, paramName)
  if parameter is not None:
    value = parameter.AsString()
    value = value if value is not None else str.Empty
  return value

def GetSPRoomNumber(element):
  return GetParameterStringValue(element, SP_ROOM_NUMBER_PARAMETER_ID)

def GetSPRoomFunctionNumber(element):
  return GetParameterStringValue(element, SP_ROOM_FUNCTION_NUMBER_PARAMETER_ID)

def SetRoomNumber(element, number):
  return SetParameterValue(element, REVIT_ROOM_NUMBER_PARAMETER_ID, number)

def SetRoomFunctionNumber(element, functionNumber):
  return SetParameterValue(element, REVIT_ROOM_FUNCTION_NUMBER_PARAMETER_ID, functionNumber)

# Element geometry computations

def ComputeBboxCentre(boundingBoxXYZ):
  return (boundingBoxXYZ.Max + boundingBoxXYZ.Min) / 2.0

def ComputeCentre(element):
  return ComputeBboxCentre(Element.get_BoundingBox(element, None))

def ShowParameterValueCopyWarningMsg(parameterId):
  print GetIndent(2) + "WARNING: Failed to copy parameter value to placed room. (parameter id: " + str(parameterId) + ")"
  return

def ShowRoomPlacementFailureWarning(sourceRoom):
  print GetIndent(2) + "WARNING: Failed to place room '" + GetSPRoomNumber(sourceRoom) + "'"
  return

def ShowFailureWarning(failure, showFailureId=False):
  print GetIndent(2) + "WARNING: " + failure.GetDescriptionText()
  if showFailureId:
    print GetIndent(2) + "         " + "(warning id: " + str(failure.GetFailureDefinitionId().Guid) + ")"
  failingElementIds = failure.GetFailingElementIds()
  additionalElementIds = failure.GetAdditionalElementIds()
  if failingElementIds.Count > 0:
    print GetIndent(2) + "         " + "Failing element ids: " + ", ".join(failingElementIds.Select(lambda id: str(id.IntegerValue)))
  if additionalElementIds.Count > 0:
    print GetIndent(2) + "         " + "Additional element ids: " + ", ".join(additionalElementIds.Select(lambda id: str(id.IntegerValue)))
  return

# Program functions

def CopyRoomParameters(sourceRoom, destinationRoom):
  results = list()
  results.append(("room function number", SetRoomNumber(destinationRoom, GetSPRoomNumber(sourceRoom))))
  for parameterName, result in results:
    if not result:
      ShowParameterValueCopyWarningMsg(parameterName)
  return all(result for parameterName, result in results)

def GetPlaceRoomAction(columnBasedRoomFamilyInstance):
  def PlaceRoomAction():
    print GetIndent(1) + "Processing room: " + "'" + str(GetSPRoomNumber(columnBasedRoomFamilyInstance)) + "'"
    doc = columnBasedRoomFamilyInstance.Document
    centre = ComputeCentre(columnBasedRoomFamilyInstance)
    newRoomLocation = UV(centre.X, centre.Y)
    newRoom = doc.Create.NewRoom(GetElementLevel(columnBasedRoomFamilyInstance), newRoomLocation)
    copyResult = CopyRoomParameters(columnBasedRoomFamilyInstance, newRoom)
    if not copyResult:
      raise Exception("Failed to copy one or more parameters while creating new room.")
    return newRoom
  return PlaceRoomAction

def IsMultipleRoomsInSameEnclosedRegion(failure):
  return (failure.GetFailureDefinitionId() == BuiltInFailures.RoomFailures.RoomsInSameRegionRooms)

def IsRoomNotEnclosedFailure(failure):
  return (failure.GetFailureDefinitionId() == BuiltInFailures.RoomFailures.RoomNotEnclosed)

def IsDuplicateValueFailure(failure):
  return (failure.GetFailureDefinitionId() == BuiltInFailures.GeneralFailures.DuplicateValue)

class WarningsAndFailuresHandler(IFailuresPreprocessor):
  def PreprocessFailures(self, failuresAccessor):
    for failure in failuresAccessor.GetFailureMessages():
      if IsRoomNotEnclosedFailure(failure):
        ShowFailureWarning(failure)
        failuresAccessor.DeleteWarning(failure)
      elif IsDuplicateValueFailure(failure):
        ShowFailureWarning(failure)
        failuresAccessor.DeleteWarning(failure)
      elif IsMultipleRoomsInSameEnclosedRegion(failure):
        ShowFailureWarning(failure)
        failuresAccessor.DeleteWarning(failure)
      else:
        print GetIndent(2) + "GOT UNEXPECTED WARNING / FAILURE MESSAGE:"
        ShowFailureWarning(failure, True)
    return FailureProcessingResult.Continue

def PlaceRoom(columnBasedRoomFamilyInstance):
  placedRoom = None
  doc = columnBasedRoomFamilyInstance.Document
  tranny, result = InTransactionWithResult(
      doc,
      "Place room with number '" + GetSPRoomNumber(columnBasedRoomFamilyInstance) + "'",
      GetPlaceRoomAction(columnBasedRoomFamilyInstance),
      WarningsAndFailuresHandler()
    )
  if (tranny.GetStatus() == TransactionStatus.Committed):
    placedRoom = result
  else:
    ShowRoomPlacementFailureWarning(columnBasedRoomFamilyInstance)
  tranny.Dispose()
  return placedRoom

# NOTE: The rooms will be placed in the phase of the currently active view!
def PlaceRooms(doc):
  placedRooms = list()
  #for g in GetColumnBasedRoomFamilyInstances(doc).OrderBy(lambda i: i.Level.Elevation).GroupBy(lambda i: i.Level.Name): print g.Key, g.Count
  columnBasedRoomFamilyInstances = GetColumnBasedRoomFamilyInstances(doc)
  instancesByLevel = columnBasedRoomFamilyInstances.OrderBy(lambda i: GetElementLevel(i).Elevation).GroupBy(lambda i: GetElementLevel(i).Name)
  for levelInstances in instancesByLevel:
    levelName = levelInstances.Key
    print
    print "-" * 60
    print "PROCESSING ROOMS ON LEVEL:", str(levelName)
    print
    for instance in levelInstances.OrderBy(lambda i: GetSPRoomNumber(i)):
      placedRoom = PlaceRoom(instance)
      if placedRoom is not None:
        placedRooms.append(placedRoom)
  return placedRooms

# TODO: perhaps do it in batches (e.g. by level, etc. so we can see progress better! ask adam t.)

# NOTE: The rooms will be placed in the phase of the currently active view!
def Place(uidoc):
  uidoc.Selection.SetElementIds([].ToList[ElementId]())
  placedRooms = PlaceRooms(uidoc.Document)
  selectedElementIds = []
  for placedRoom in placedRooms:
    selectedElementIds.append(placedRoom.Id)
  uidoc.Selection.SetElementIds(selectedElementIds.ToList[ElementId]())
  return

caption = "Place rooms script"
msg = StringBuilder()
msg.AppendLine("ATTENTION:")
msg.AppendLine()
msg.AppendLine("Rooms will be placed:")
msg.AppendLine("  - on the active workset.")
msg.AppendLine("  - in the phase of the active view.")
msg.AppendLine()
msg.AppendLine("Check that these are appropriate before continuing.")

dialogResult = WinForms.MessageBox.Show(
    msg.ToString(),
    caption,
    WinForms.MessageBoxButtons.OKCancel,
    WinForms.MessageBoxIcon.Warning,
    WinForms.MessageBoxDefaultButton.Button2 # default to cancel
  )

if dialogResult == WinForms.DialogResult.OK:
  print "Type 'Place(uidoc)' to run this script."
  #Place(uidoc)
