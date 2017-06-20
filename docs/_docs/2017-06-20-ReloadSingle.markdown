---
title:  "Revit - Reload Families"
date:   2017-06-21 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "This describes how to reload multiple families into a project file."
modified:
layout: "sample"
categories: Revit
---

# Family Reloader - Preface

The ‘Reload Families” app is meant to be used in project environments where the same families are used across multiple Revit Project files and it is mandatory to have the same version of any given family across all project files. This usually requires a lot of time consuming reloading of amended families into each of the project files.
An example would be Health Care projects with multiple buildings in separate Revit files which require the same equipment families.

## User Interface

The Family Updater is located within the BVN Tab on the Families Panel:
![FamilyReloaderSingleIcon]({{ site.baseurl }}/assets//Reloader/Icon-ReloadFamily.png){:class="img-responsive"}{: height="90px" width="80px"}

The user interface comprises of a single window:

![FamilyReloaderSingleMain]({{ site.baseurl }}/assets/Reloader/GUI-ReloadFamilies-Main-doc.png){:class="img-responsive"}{: height="600px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Family List | The family list window displays all families loaded in the current project file. This list can be filtered via 3 – Filter Settings. Only highlighted families will be re-loaded into the project file. |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. The option ‘Select from List’ allows for families to be selected from a pre-defined list file. The list file is a simple text file containing on a by row basis the full file path of any number of Revit families. The Family Reporter App creates such a list. |
| 3 – Filter Settings | This button will bring up the Filter Settings dialogue. Refer below. |
| 4 / 5 – Reload Options | When re-loading families one can choose between: 4) including only family types already loaded into a project or 5) load all family types existing in the family file in the library. For example: a family in a project files contains types A and B, but the same family in the library contains types A, B and C. With option 4) selected only types A and B will be loaded. Option 5 will load types A, B and C into the project file. |
| 6 – Revit Library Location | The root folder of your project Revit library. All sub folders will be included when searching for families in your library. |
| 7 – Browse to Library Location | 1 - The path to your project library folder. In can directly be copied and paste from windows explorer. |
| 8 - Cancel | Cancels any user input and returns to Revit |
| 9 – Reload (x) | Will start the process of reloading all highlighted families. The number of families to be reloaded is shown in brackets. After completion a ‘Finished’ Message will be displayed. |

![FamilyReloaderSingleFilterSettings]({{ site.baseurl }}/assets/Reloader/GUI-ReloadFamilies-Settings-doc.png){:class="img-responsive"}{: height="600px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Available Family Categories | Only family of categories checked here will appear in the main Family List. |
| 2 – Selection Options | Default highlight options. |
| 3 - Check / Un-check | This will either check or un-check highlighted family categories. |
| 4 - Cancel | Will cancel any user input and returns to the main Reload Families window. |
| 5 - OK | Applies the selected family categories as filters to the family list in the main window. |

Notes:

* Do not place any superseded family files into your Revit library. The family re-loader will not be able to differentiate between your current family XYZ and your superseded family XYZ with the same name and will display a warning containing the locations identified for a particular family.