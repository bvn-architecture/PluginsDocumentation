---
title:  "Revit Family Reporter"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Purpose and capabilities of the Revit Family Reporter App"
modified:
layout: "sample"
---

# Family Reporter- Preface

The ‘Family Reporter” app is used to gather a number of properties from families and their catalog files. Those log file can be opened and edited in Excel and then applied to families via the Family Updater app.

Summary of log files and properties they report:

| Log File | Properties |
|---------|------------|
| [FamilyCategory Log] (#FamCategoryLog) | Reports the Revit Category of a family |
| [test] (#markdown-header-Family-Category-Log_2) |  |
| FamilyDefault Log | Reports: Revit Version number, Edited last time stamp, and whether a family uses a catalogue file |
| FamilySubCategory Log | Reports Revit subcategories present in a family. |
| Family Types Log | Reports all family types defined in a family file and, if present, in its associated catalogue file. |
| Host Families Log | Reports all families which contain nested families |
| Materials Log | Reports all materials defined in family file. |
| Nested Families Log | Reports all nested families together with their host family. |
| OmniClass Log | Reports the Omniclass of a family. |
| Parameters Log | Reports all parameters present in a family and their properties but not values |
| ParameterValuesByTypes Log | Reports parameter values by family type. Report includes family types defined in a catalogue files. |
| Reference Planes Log | Reports all reference planes present in a family and their properties |
| Units Log | Reports units set for area, volume, angle, Number and Length |

## Detailed Log file break down

Log files are available in MS Excel format. These log files are formatted to easily identify which fields can be edited and therefore used to update family properties.

* Cells with a grey back ground are read only. 
* Cells with a white bac ground can be edited. Most reports will also have a drop down enabled to allow selection of pre-defined actions.

### Family Defaults Log

### Family Category Log_2

### <h3><a id="FamCategoryLog" />Family Category Log</h3>

| FamilyFilePath | FamilyName | Category |
|--------|----------|-----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The Revit category of a family. |

The 'Category' field can be changed via the drop down. Please note that there are some combinations of current family category and new family category selections which will result in an exception reported when attempting to update a family file:

| Current Category | Selection | why? |
|--------------|---------------|------|
| Non annotation category | Generic Annotation, tag of any type, detail component | This action is not available through the standard Revit user interface. |
| Annotation Categery (generic annotation, tag of any type, detail component) | any family category which may contain 3D elements | This action is not available through the standard Revit user interface. |
