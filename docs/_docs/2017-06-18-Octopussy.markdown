---
title:  "Revit Family Updater"
date:   2017-06-15 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Purpose and capabilities of the Revit Family Updater App"
modified:
layout: "sample"
categories: Revit
---

# Family Updater - Preface

The ‘Family Updater' app is used to modify your Revit library content in three steps:

* Gather family data via the [Family Reporter App]
* Modify family properties in MS Excel
* Apply those modifications to your families via the Family Updater App

TODO:

* add workflow graphic

## User Interface

The Family Updater is located within the BVN Tab on the Families Panel:
![FamilyUpdaterIcon]({{ site.baseurl }}/assets/FamilyUpdater/Icon-UpdateFamilyParameterValues.png){:class="img-responsive"}{: height="45px" width="100px"}

The user interface comprises of a single window with 2 tabs:

* Reports

![FamilyUpdaterUIReports]({{ site.baseurl }}/assets/FamilyUpdater/GUI-UpdateFamilyParameterValues-MainReports-doc.png){:class="img-responsive"}{: height="700px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Family List | The family list window displays all families contained in a list file. |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3  – Open reports | Open varies report [types](#ReportsSummary)
| 4 - Cancel | Cancels any user input and returns to Revit
| 5 – Process Families (x) | Will start to process all highlighted families. The number of families to be processed is shown in brackets. After completion a ‘Finished’ Message will be displayed. |

* General

![FamilyUpdaterUIGeneral]({{ site.baseurl }}/assets/FamilyUpdater/GUI-UpdateFamilyParameterValues-MainGenUpdates-doc.png){:class="img-responsive"}{: height="700px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Family List | The family list window displays all families contained in a specified folder. |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3 - Purge Unused | See [here](#PurgeUnused) |
| 3 - Force Change | See [here](#ForceChange) |
| 4 - Cancel | Cancels any user input and returns to Revit. |
| 5 – Process Families (x) | Will start to process all highlighted families. The number of families to be processed is shown in brackets. After completion a ‘Finished’ Message will be displayed. |

## Type of updates available

Family Reporter differentiates between two main types of updates:

* Report based
* Common

### <a id="ReportsSummary"></a> Report based updates

Report based updates require an MS Excel sheet containing the information requiring updates.
The following report based updates are available:

| Report | Updates available |
|---------|------------|
| [FamilyCategory Log](#FamCategoryLog) | Updates the Revit Category of a family |
| [FamilySubCategory Log](#FamSubCatLog) | Updates Revit subcategories present in a family. |
| [Family Types Log](#FamTypesLog) | Updates all family types defined in a family file and, if present, in its associated catalogue file. |
| [OmniClass Log](#FamOmniLog) | Updates the Omni class of a family. |
| [ParameterValuesByTypes Log](#FamParaValuebyTypeLog) | Updates parameter values by family type. This may includes family types defined in a catalogue files. |

### Common updates

Whilst report based updates require specific instructions per family file what to do, common updates apply the same update to all family files.

The following common updates are available:

| Update | Action |
|---------|------------|
| Purge Unused <a id="PurgeUnused"></a> | Attempts to purge all unused nested families or nested family types within a family |
| Force Change <a id="ForceChange"></a> | Internally this action creates a new family type, saves the family, deletes the dummy type and finally, saves the family again. From a user point of view the family will appear unchanged. However Revit will consider this family as changed and force an update when reloading it. This can be use full when e.g. a typical details file gets migrated from one project to another. In this situation, the families loaded in the project file in the new project location still remember their file origin in the old project folder location. A simple re-load of the families from their new location at this point will not re-path the families since Revit considers them identical and will not update to the new origin. Running a 'Force Change' update prior to re-loading the families will trick Revit into updating the families and therefore their internally stored origin. Note: this will only work on a family which has as a minimum at least one family type set-up already. Otherwise it will report an exception. |

## Detailed report based updates break down

### <a id="FamCategoryLog"></a> Family Category Log

| FamilyFilePath | FamilyName | Category |
|--------|----------|-----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The Revit category of a family. |

The 'Category' field can be changed via the drop down. Please note that there are some combinations of current family category and new family category selections which will result in an exception reported when attempting to update a family file:

| Current Category | Selection | why? |
|--------------|---------------|------|
| Non annotation category | Generic Annotation, tag of any type, detail component | This action is not available through the standard Revit user interface. |
| Annotation Category (generic annotation, tag of any type, detail component) | Any family category which may contain 3D elements | This action is not available through the standard Revit user interface. |

### <a id="FamSubCatLog"></a> Family Subcategory Log

| FamilyFilePath | FamilyName | Category | Id | Line Weight Cut | Line Weight Projection | Colour As RGB | Material Name | Line Pattern Name | SubCategory Action | SubCategory Action Parameter |
|----------------|------------|--------------------|---------------|---------------------|--------|----------|-----------|-----------|---------|----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The Revit category the subcategory belongs to. | The Revit element ID of the subcategory. | Line weight used for cut elements. | Line weight used for projected elements.  | The colour of a subcategory as an comma separated RGB (range 0 to 255) | The assigned material name. 'Default' if none is assigned. | The line pattern name assigned to this subcategory. | SubCategory Action describing what to do with this subcategory. | Additional information required to execute an action. |

Following is a table describing all possible actions and action parameters where required.

| Subcategory Action | Subcategory Action Parameter | Description |
|--------------------|------------------------------|-------------|
| Create | n/a | Creates a new subcategory with properties specified in adjacent columns. |
| Delete | n/a | Deletes a subcategory. |
| Update | optional: new subcategory name | Updates subcategory properties (and name if provided) with values specified in adjacent columns. |
| None | n/a | No action specified for this subcategory. |

### <a id="FamTypesLog"></a> Family Types Log

| FamilyFilePath | FamilyName | Family Type Name | Family Type Name Action | Family Type Name Action Parameter |
|----------------|------------|------------------|-------------------------|-----------------------------------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The family type name. | Family type name action describing what to do with this type. | Additional information required to execute an action |

Following is a table describing all possible actions and action parameters where required.
Note that the actions described apply to Revit family files (.rfa) as well as catalogue files (.txt).

| Subcategory Action | Subcategory Action Parameter | Description |
|--------------------|------------------------------|-------------|
| Create | n/a | Creates a new family type. Parameter values will need to be set [separately](#FamParaValuebyTypeLog). |
| Delete | n/a | Deletes a family type. |
| Update | requires: new type name | Updates family type name. |
| None | n/a | No action specified for this family type. |

### <a id="FamOmniLog"></a> Omni Class Log

| FamilyFilePath | FamilyName | Omni class |
|--------|----------|-----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The omni class code of a family. |

For a description on omni class codes refer [here](http://www.omniclass.org/). 
To change or set the omni class code, just update the cell in the omni class column with the code required.

### <a id="FamParaValuebyTypeLog"></a> Parameter Value by Type Log

| FamilyFilePath | FamilyName | Family Type Name | Parameter Name | Parameter GUID | Parameter Value | Parameter Is Determined By Formula | Parameter Is Instance | Parameter Is Reporting | Parameter Storage Type |
|--------|----------|-----------|----------|-------|-------|------|-----|---------|-----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The family type name. | The name of the parameter | The GUID of a parameter. This value is only set for shared parameters. | The parameter value for this family type. |'TRUE' if formula is present, otherwise 'FALSE' | 'TRUE' if parameter is instance driven. 'False' if type driven | 'TRUE' if this is a reporting parameter, otherwise 'FALSE' | The Revit internal parameter storage type. |

To change or set parameter values in a specific family type, simply change the value in the 'parameter value' column as required.

Note that this assumes that:

* The parameter value is not determined by a formula.
* The parameter is not a reporting parameter.
* The new value you are providing fits the storage type of a parameter. E.g. a string value does not fit an integer storage type.
* If an element ID is provided ensure that that ID is valid:
    * It exists
    * The element it points to matches the required element type.
    * E.g. If the parameter expects a material ID, the ID provided must be of a material element and that material element needs to exists in the family.