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
| [FamilyCategory Log](#FamCategoryLog) | Reports the Revit Category of a family |
| [FamilyDefault Log](#FamDefaultLog) | Reports: Revit Version number, Edited last time stamp, and whether a family uses a catalogue file |
| [FamilySubCategory Log](#FamSubCatLog) | Reports Revit subcategories present in a family. |
| [Family Types Log](#FamTypesLog) | Reports all family types defined in a family file and, if present, in its associated catalogue file. |
| [Host Families Log](#FamHostLog) | Reports all families which contain nested families |
| [Materials Log](#MaterialsLog) | Reports all materials defined in family file. |
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

### <a id="FamCategoryLog"></a> Family Category Log

| FamilyFilePath | FamilyName | Category |
|--------|----------|-----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The Revit category of a family. |

The 'Category' field can be changed via the drop down. Please note that there are some combinations of current family category and new family category selections which will result in an exception reported when attempting to update a family file:

| Current Category | Selection | why? |
|--------------|---------------|------|
| Non annotation category | Generic Annotation, tag of any type, detail component | This action is not available through the standard Revit user interface. |
| Annotation Category (generic annotation, tag of any type, detail component) | Any family category which may contain 3D elements | This action is not available through the standard Revit user interface. |

### <a id="FamDefaultLog"></a> Family Default Log

| FamilyFilePath | FamilyName | Family Edited Last | Revit Version | Uses Catalogue File |
|----------------|------------|--------------------|---------------|---------------------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The OS generated time stamp indicating when a file was edited last. | The Revit version this file is in. | 'TRUE' if there is a catalogue file or 'FALSE' if there isn't |

None of the reported properties in this report can be used to update Revit family files.

### <a id="FamSubCatLog"></a> Family Subcategory Log

| FamilyFilePath | FamilyName | Category | Id | Line Weight Cut | Line Weight Projection | Colour As RGB | Material Name | Line Pattern Name | SubCategory Action | SubCategory Action Parameter |
|----------------|------------|--------------------|---------------|---------------------|--------|----------|-----------|-----------|---------|----------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The Revit category the subcategory belongs to. | Line weight used for cut elements. | Line weight used for projected elements.  | The colour of a subcategory as an comma separated RGB (range 0 to 255) | The assigned material name. 'Default' if none is assigned. | The line pattern name assigned to this subcategory. | SubCategory Action describing what to do with this subcategory. | Additional information required to execute an action. |

For a detailed list of Subcategory actions and associated Subcategory Action Parameters refer to 'Family Updater' document.

### <a id="FamTypesLog"></a> Family Types Log

| FamilyFilePath | FamilyName | Family Type Name | Family Type Name Action | Family Type Name Action Parameter |
|----------------|------------|------------------|-------------------------|-----------------------------------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | Family type name action describing what to do with this type. | Additional information required to execute an action |

For a detailed list of Family Type actions and associated Family Type Action Parameters refer to 'Family Updater' document.

### <a id="FamHostLog"></a> Host Family Log

| FamilyFilePath | FamilyName | Nested Family Count |
|----------------|------------|---------------------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The number nested families within the family. |

None of the reported properties in this report can be used to update Revit family files.

### <a id="MaterialsLog"></a> Materials Log

| FamilyFilePath | FamilyName | Materials ID | Material Name | Material Colour | Cut Pattern Name | Cut Pattern Colour | Surface Pattern Name | Surface Pattern Colour | Material Shininess | Material Smoothness | Material Transparency |
|----------------|------------|--------------|---------------|-----------------|------------------|--------------------|---------------------|-------------------------|--------------------|---------------------|----------------------|
| The fully qualified file path of a family file | The file name, including file extension, of a family file. | The material ID used to identify a particular material | The material name. | The material colour as a comma separated RGB value. | The name of the cut pattern assigned to a material. | The cut pattern colour as a comma separated RGB value. | The name of the surface pattern assigned to a material. | The surface pattern colour as a comma separated RGB value. | The material shininess as an integer value ranging from 0 to 100. | The material smoothness as an integer value ranging from 0 to 100. | The material transparency as an integer value ranging from 0 to 100. |

No actions are available yet for this report type.
