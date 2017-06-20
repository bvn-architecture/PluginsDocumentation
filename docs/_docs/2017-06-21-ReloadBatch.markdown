---
title:  "Revit - Reload Families in bulk"
date:   2017-06-21 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "This describes how to reload multiple families into any number of project files."
modified:
layout: "sample"
categories: Revit
---

# Family Reloader Batch - Preface

The ‘Reload Families - Batch' app is meant to be used in project environments where a large amount of nested families are used and it is mandatory to have the same version of any nested family across all host families. This usually requires keeping track of which host families contain which nested families. (refer to [Family Reporter]({{ site.baseurl }}/_docs/2017-05-31-FamilyReporter)) During the reload process all unused family types and definitions in host families will be purged.

An example would be Health Care projects with multiple equipment families or medical service panel families containing all the same power outlet and or data outlet families as shared nested elements.

## User Interface

The Family Updater is located within the BVN Tab on the Families Panel:
![FamilyReloaderBatchIcon]({{ site.baseurl }}/assets//ReloaderBatch/Icon-BatchFamilyReloader.png){:class="img-responsive"}{: height="50px" width="80px"}

The user interface comprises of a single window:

![FamilyReloaderBatchMain]({{ site.baseurl }}/assets/ReloaderBatch/GUI-BatchFamilyReloader-Main-doc.png){:class="img-responsive"}{: height="600px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Family List | The family list window displays families and or project files in a folder or opened from a list. For the later refer to Family Reporter App. |
| 2 – Selection Options | These are the standard selection options aiming to help to manage larger family lists. |
| 3 / 4 – Open Options | This app can batch process 3 - all families located in a specific folder and it’s sub folders or 4 – families from a list file. The list file is a simple .txt file which contains a full file path per family to be processed per row and can be created by the Family Reporter App. |
| 5 / 6 – Reload Options | When re-loading families one can choose between: 4) including only family types already loaded into a project or 5) load all family types existing in the family file in the library. For example: a family in a project files contains types A and B, but the same family in the library contains types A, B and C. With option 4) selected only types A and B will be loaded. Option 5 will load types A, B and C into the project file. |
| 7 – Revit Library Location | The root folder of your project Revit library. |
| 8 – Browse to Library Location | The path to your project library folder. It can directly be copied and paste from windows explorer. |
| 9 - Cancel | Cancels any user input and returns to Revit. |
| 10 – Reload (x) | Will start the process of reloading all nested families in the highlighted host families. The number of families to be processed is shown in brackets. After completion a ‘Finished’ Message will be displayed. |

Notes:

* Do not place any superseded family files into your Revit library. The family re-loader will not be able to differentiate between your current family XYZ and your superseded family XYZ with the same name and might reload the family from the wrong file.