---
title:  "Revit Family Apps"
date:   2017-05-18 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Varies Revit Apps centering around family management"
modified:
layout: "sample"
---

# How To - Revit Family Apps

| Release Date | Version | Comments |
| --- | --- | --- |
| 08/01/2013 | 0.1 | Draft |
| 17/06/2013 | 0.2 | Icon Updates |
| 18/05/2017 | 0.3 | Update to markdown document |

1. 1.00Summary – Families Tab

The Revit Family Apps are a collection of add-ins meant to improve family management in a Revit project. The collection is comprised of:

| App Name | Icon | App Usage |
| --- | --- | --- |
|
- Reload Families
 |


 | Reload multiple families into a single project / family file. |
|
- Reload Families - Batch
 |


 | Reload all families found in multiple
- --Revit project files (only limited support for work shared project files)
- --Revit family files
 |
|
- Family Reporter
 |


 | Provides an easy way to report on:
- --Number and name of nested families
- --Parameter names/ values depending on family type
It also allows to:
- --Purge unused nested families
- --Set a 3D preview thumbnail for easy family browsing in windows explorer
 |
|
- Family Updater
 |

 | This app can update family parameter values depending on family type. |
|
- Add Shared Parameter
 |


 | This app adds any number of given shared parameters to any number of Revit families |

Within the Revit user interface the family apps can be found under the BVN Tools tab:


1. 1.00Reload Families - PReface

The &#39;Reload Families&quot; app is meant to be used in project environments where the same families are used across multiple Revit Project files and it is mandatory to have the same version of any given family across all project files. This usually requires a lot of time consuming reloading of amended families into each of the project files.

An example would be Health Care projects with multiple buildings in separate Revit files which require the same equipment families.

1. 2.00Reload Families - User Interface


| 1 – Family List | The family list window displays all families loaded in the current project file. This list can be filtered via 3 – Filter Settings. Only highlighted families will be re-loaded into the project file. |
| --- | --- |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. The option &#39;Select from List&#39; allows for families to be selected from a pre-defined list file. The list file is a simple text file containing on a by row basis the full file path of any number of Revit families. The Family Reporter App creates such a list. |
| 3 – Filter Settings |


This button will bring up the Filter Settings dialogue.


 | 1 – Available Family Categories1 - Only family of categories checked here will appear in the main Family List2 – Selection Options2 - Highlights family categories3 - This will either check or un-check family categories4 - Cancels any user input and returns to the main Reload Families window5 - Filters the Family List by family categories selected and returns to the main Reload Families window |
| 4 / 5 – Reload Options | When re-loading families one can choose between: 4) including only family types already loaded into a project or 5) load all family types existing in the family file in the library. For example: a family in a project files contains types A and B, but the same family in the library contains types A, B and C. With option 4) selected only types A and B will be loaded. Option 5 will load types A, B and C into the project file. |
| 6 – Revit Library Location | The root folder of your project Revit library. All subfolders will be included when searching for families in your library.Note: Do not place any superseded family files into your Revit library. The family re-loader will not be able to differentiate between your current family XYZ and your superseded family XYZ with the same name and might re-load the wrong version. |
| 7 – Browse to Library Location |


1 - The path to your project library folder. In can directly be copied and paste from windows explorer.2 – Browse via the Open Folder dialogue3 - Cancels any user input and returns to the main Reload Families window4 – Confirms chosen library location and returns to main Reload Families window. |
| 8 - Cancel | Cancels any user input and returns to Revit |
| 9 – Reload (x) | Will start the process of reloading all highlighted families. The number of families to be reloaded is shown in brackets. After completion a &#39;Finished&#39; Message will be displayed. |

1. 1.00Reload Families - Batch- PReface

The &#39;Reload Families - Batch&quot; app is meant to be used in project environments where a large amount of nested families are used and it is mandatory to have the same version of any nested family across all host families. This usually requires keeping track of which host families contain which nested families. (See Family Reporter) During the reload process all unused family types and definitions in host families will be purged.

An example would be Health Care projects with multiple equipment families or medical service panel families containing all the same power outlet and or data outlet families

1. 3.00Reload Families Batch - User Interface


| 1 – Family List | The family list window displays families and or project files in a folder or opened from a list. For the later refer to Family Reporter App. |
| --- | --- |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3 / 4 – Open Options | This app can batch process 3 - all families located in a specific folder and it&#39;s sub folders or 4 – families from a list file. The list file is a simple .txt file which contains a full file path per family to be processed per row and can be created by the Family Reporter App.P:\11 \Project\_Revit Library\\_Codebook Families\SE-4050-Tap.rfaP:\11\s1110005.bdh\ \_Codebook Families\SE-4010-Tap, cold water outlet.rfa |
| 5 / 6 – Reload Options | When re-loading families one can choose between: 4) including only family types already loaded into a project or 5) load all family types existing in the family file in the library. For example: a family in a project files contains types A and B, but the same family in the library contains types A, B and C. With option 4) selected only types A and B will be loaded. Option 5 will load types A, B and C into the project file. |
| 7 – Revit Library Location | The root folder of your project Revit library. Note: Do not place any superseded family files into your Revit library. The family re-loader will not be able to differentiate between your current family XYZ and your superseded family XYZ with the same name and might re-load the wrong version. |
| 8 – Browse to Library Location |


1 - The path to your project library folder. It can directly be copied and paste from windows explorer.2 – Browse via the Open Folder dialogue3 - Cancels any user input and returns to the main Reload Families - Batch window4 – Confirms chosen library location and returns to main Reload Families - Batch window. |
| 9 - Cancel | Cancels any user input and returns to Revit |
| 10 – Reload (x) | Will start the process of reloading all nested families in the highlighted host families. The number of families to be processed is shown in brackets. After completion a &#39;Finished&#39; Message will be displayed. |



1. 1.00family Reporter- PReface

The &#39;Family Reporter&quot; app is used to gather the following information from families:

|
1. 1)Parameter Names and values depending on Family Type
 |
1. 2)General File information:

- Full file path
- Family Name
- When was family edited last
 |
1. 3)Nested families, types and how many instances are placed
 |
| --- | --- | --- |
|
1. 4)Parameter data:

- Is parameter formula driven?
- instance or type parameter
- reporting parameter?
- what storage type
- parameter GUID (if shared parameter)
  |
1. 5)Revit Family Category
 |
1. 6)Whether this is a host family
 |

It can also perform the following actions on families:

|
1. a)Create a 3D preview thumbnail for easy family browsing in windows explorer and save a .png file
 |
1. b)Purge unused nested family types and or entire nested families
 |
1. c)Force a change to the family file
Background: sometimes Revit refuses to acknowledge that there was a change in a family file and fails to update the family in a project file with new values from the family from the library. This option will fix that behavior |
| --- | --- | --- |

The app creates multiple report files in the &#39;Log&quot; folder on the users Desktop:

| File | Content (refer to table above for index details) |
| --- | --- |
| Family\_Report\_FamilyTypes Log.txt | 1), 2),4),5)-note: this file can be re-used in the &#39;Family Updater&#39; app. |
| Family\_Report\_Host Families Log.txt | 6)-note : this file can be re-used in the:
- --&#39;Reload Families&#39; app to select families via the &#39;Select from List&#39; button
- --&#39;Reload Families – Batch&#39; app via the &#39;Open from List&#39; button
- --&#39;Family Reporter&#39; app via the &#39;Open from List&#39; button
 |
| Family\_Report\_Nested Families Log.txt | 3) |
| Family\_Report\_Error Log.txt | Any error encountered during the processing of selected families. |



1. 4.00family Reporter - User Interface

| 1 – Family List | The family list window displays all families in a folder selected or contained in a list file. |
| --- | --- |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3 / 4 – Open Options | This app can batch process 4 - all families located in a specific folder and its sub folders or 3 – families from a list file. The list file is a simple .txt file which contains a full file path per family to be processed per row and can be created by the Family Reporter App.P:\11 \Project\_Revit Library\\_Codebook Families\SE-4050-Tap.rfa |
| 5 – Create 3D Preview | Creates a 3D view in the family and sets it as preview image for the family. It also saves out a .png file of that 3D view. |
| 6 – Purge Unused | Purges all unused nested families from the host family |
| 7 – Force Change | This option is useful in 2 scenarios:
1. 1)Revit refuses to acknowledge there was a change made to family property values
2. 2)A project file is re-used in another project and all families need to be re-linked to the new project library location to avoid accidental changes to families in the old project.
  1. Copy all families from the old project folder to the new project library folder
  2. Run Family Reporter with force change option ticked on new project library
  3. Use Reload Families / Reload Families Batch to reload families from the new project library location
 |
| 8 - Cancel | Cancels any user input and returns to Revit |
| 9 – Process Families (x) | Will start to process all highlighted families. The number of families to be processed is shown in brackets. After completion a &#39;Finished&#39; Message will be displayed. |



1. 1.00family Updater- PReface

The &#39;Family Updater&quot; app is used to bulk change parameter values in families depending on the family type. It requires an excel sheet created from the &#39;Family\_Report\_FamilyTypes Log.txt&#39; created by the &#39;Family Reporter&#39; App.

An example would be a set of families where one want to change the parameter value of the parameter &#39;HFBS Group&#39; from let&#39;s say &#39;1&#39; to &#39;2&#39;.

1. 2.00family Updater- User Interface


| 1 – Family List | The family list window displays all families contained in a list file. |
| --- | --- |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3  – Open from List | This app can only batch process families from a list file. The list file is an Excel document derived from a  &#39;Family\_Report\_FamilyTypes Log.txt&#39; created by the &#39;Family Reporter&#39; App. |
| 7 - Cancel | Cancels any user input and returns to Revit |
| 8 – Process Families (x) | Will start to process all highlighted families. The number of families to be processed is shown in brackets. After completion a &#39;Finished&#39; Message will be displayed. |

1. 1.00Add Shared Parameter - PReface

The &#39;Add Shared Parameter&#39; app can be used in 2 scenarios:

| Scenario | Availability |
| --- | --- |
|
- --add parameters to an open family file
 | Only available when app is started in a Revit Family File |
|
- --add the same parameters to multiple families
 | Only available when app is started in a Revit Project file |

1. 2.00Add Shared Parameter – User Interface


| 1 – Shared Parameter File | The file path to the shared parameter file |
| --- | --- |
| 2/4 – Open file dialogue | Displays an open file dialogue where the user can select the file required |
| 3  – Parameter to Add File | This is a simple text file describing:
- --which parameter is to be added
- --what category to add it under
- --whether it is a type or instance parameter
For more details on this file refer to section 3 |
| 5 Batch… | This option is only available when the app is started in a project file (not a family file). |
| 6 – Enable Batch processing | Check this box if you need to add the same shared parameters to multiple families. |
| 7 – Folder Path | Path to folder containing all families which require parameters to be added to. It can directly be copied and paste from windows explorer. |
| 8 – Browse to Folder | Opens a browse to folder dialogue. |
| 9 - Cancel | Cancels any user input and returns to Revit |
| 10 – Add | Will add the shared parameters to family file open or batch process families in selected folder. |

1. 3.00Add Shared Parameter – Parameter to Add file

This file contains on a line by line base the following information:

| Parameter Name | &lt;tab&gt; | Category | &lt;tab&gt; | Parameter typetrue = instance parameterfalse= type parameter |
| --- | --- | --- | --- | --- |
| Sample: |   |   |   |   |
| **WindowFrameMaterial** |   | **PG\_TEXT** |   | **false** |

The app supports the following Categories only:

| PG\_LENGTH | PG\_CONSTRAINTS |
| --- | --- |
| PG\_VISIBILITY | PG\_MATERIALS |
| PG\_DATA | PG\_GRAPHICS |
| PG\_GENERAL | PG\_GEOMETRY ((Dimensions category in Revit User interface) |
| PG\_AREA | PG\_IDENTITY\_DATA |
| PG\_ANALYTICAL\_MODEL |   |
| PG\_ENERGY\_ANALYSIS |   |
| PG\_TEXT |   |

