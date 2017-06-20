---
title:  "Revit - Add Shared Parameter to Families"
date:   2017-06-20 09:00:00 +0100
permalink: #/docs/2017-04-28-PushIt
excerpt: "This describes How to add multiple shared parameters to one or multiple families in one go."
modified:
layout: "sample"
categories: Revit
---

# Add Shared Parameter - Preface

The ‘Add Shared Parameter' app is used to add shared parameters to a single or multiple families in one go.

## User Interface

The Family Updater is located within the BVN Tab on the Families Panel:
![FamilyUpdaterIcon]({{ site.baseurl }}/assets//AddSharedParameter/Icon-AddSharedparamterToFamily.png){:class="img-responsive"}{: height="45px" width="100px"}

The user interface comprises of a single window:

![FamilyUpdaterUIReports]({{ site.baseurl }}/assets/AddSharedParameter/GUI-AddSharedparamterToFamily-Main-doc.png){:class="img-responsive"}{: height="300px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Shared Parameter File | The file path to the shared parameter file containing the parameters to be added |
| 2– Open file dialogue | Displays an open file dialogue where the user can select the shared parameter file to be used. |
| 3 - Batch | This option is only available when the app is started in a project file (not a family file). Check this box if you need to add the same shared parameters to multiple families. |
| 4  – Folder path | Path to folder containing all families which require parameters to be added to. It can directly be copied and paste from windows explorer. |
| 5 – Browse to Folder | Browse to the folder containing families to which parameters are to be added. Note: the parameters will be added to all families in the specified folder.  |
| 6 – Parameter selection | Here the user can select: Which parameter is to be added, Whether it is added as instance parameter, Under which category it will appear in the properties window of an element. |
| 7 - Cancel | Cancels any user input and returns to Revit. |
| 8 – Add | Will add the shared parameters to family file open or batch process families in selected folder. |

Notes:

* Shared parameters will not be added multiple times to a family. If it already exists in a family, it will not be added again.
* This app will remember which parameters where added last in order to make repetitive adding of parameters easier.