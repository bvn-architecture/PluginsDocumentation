---
title:  "Revit - Export Schedules in bulk"
date:   2017-06-22 13:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "This describes how to export multiple Revit schedules to text files."
modified:
layout: "sample"
categories: Revit
---

# Export Schedules - Preface

The ‘Export Schedules’ app is meant to be used when multiple Revit schedules need to be exported to text files at the same time. This could be useful when those text files are in turn linked into Excel files for further processing.

ToDo: Add process graphics: 

## User Interface

The 'Export Schedules' app is located within the BVN Tab on the Views Panel:
![ExportScheduleIcon]({{ site.baseurl }}/assets/ExportSchedules/Icon-ExportSchedules.png){:class="img-responsive"}{: height="50px" width="80px"}

The user interface comprises of a single window:

![ExportScheduleMain]({{ site.baseurl }}/assets/ExportSchedules/GUI-Export Schedules-Main-doc.png){:class="img-responsive"}{: height="600px" width="900px"}

| Item | Function |
|------|----------|
| 1 – Schedules | Displays all schedules in the model. Schedules in ‘<>’ are System schedules. Highlight all schedules you want to export. |
| 2 – Show System Schedules | Hides or shows system schedules. |
| 3 - Folder Path | Select the folder where the schedules will be exported to. |
| 4 - Folder browse | A folder browse dialogue will be displayed. |
| 5 - Cancel | Cancels any user input and returns to Revit. |
| 6 – Export Schedules (x) | Will start the process of exporting the highlighted schedules. |