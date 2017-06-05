---
title:  "Revit setup of Nepean Hospital"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Everything relating to Revit on Nepean Hospital"
modified:
layout: "sample"
---

# Existing Cancer Center refurbishment Works

## Site set-out


# New Acute Services Building

## Generic Rooms

Generic Rooms for the Schematic Design stage are located in s1607004-AR-INH-GENRIC.rvt Revit file.

The following rooms will be captured:

| Room Code | Room Name |
|-----|
| BMEQ-4 | Bay- Mobile Equiment  4sqm |
| BMEQ-6 | Bay- Mobile Equiment  6sqm |
| BHWS-A | Bay - Handwash Basin Type A |
| BHWS-B | Bay - Handwash Basin Type B |
| BHWS-PPE | Bay - Handwash Basin & PPE |
| BS-1 | Bay - Storage 1sqm |
| BPTS | Bay - Pneumatique Tube |
| BLIN | Bay - Linen |
| BRES | Bay - Resus Trolley |
| BMT-4 | Bay - Meal Trolley |
| WCPU-3 | Toilet - Public  3sqm |
| WCAC | Toilet - Accessible |
| WCPT | Toilet - Patient |
| WCST | Toilet - Staff |
| EN-ST-AS | Ensuite ( Toilet and shower patient - Not ensuited to room) |

Room properties and their use:

| Area | The designed area of a room measured to centre line walls |
| Base Finish | TBC |
| Ceiling Finish | TBC |
| Ceiling Height | TBC |
| Comments | TBC |
| Department | TBC |
| Department Code | TBC |
| FF_1 | TBC |
| FF_Specific 1 | TBC |
| FFETemplateMatch | TBC |
| Floor Finish | TBC |
| Name | The briefed name of the room. |
| Number | The briefed code of the room. |
| Sub-Department  | TBC |
| TemplateMatch | TBC |
| Unique Id | TBC |
| Wall Finish | TBC |


## Fire Compartment Drawings

The Fire Compartment drawings are done as Area Plans of type: 'FIRE COMPARTMENT'.

### Custom shared parameter properties

The areas have the following properties:

| Property | GUID | use |
|-----|
| Area Type | build in | not used |
| AREA_COLOUR_BVN  | acac3c63-7165-4dd9-b648-c086e0ddde48 | Area colour fill scheme uses this property to colour in areas |
| AREA_COMPARTMENT_GROUP_BVN  | 4955f5a0-86fb-4fee-8184-7ae85716bebe| Used when a fire department spreads across multiple levels and therefore requires a number of areas to be drawn to capture its full extent. |
| | | Fire compartment schedule filters all area instance with the same fire compartment group number |
| AREA_TYPE_BVN  | 1bcf8295-93ea-4c10-85ce-40b879fd31d5 | Can be used to differentiate between 'Patient Care and Treatment' vs 'Ancillary' areas. |
| | | This parameter is more flexible than the build in 'Area Type' which only has a fixed non changeable number of values | 
| Name | build in |type of department: e.g. SMOKE |
| Number | build in | Fire compartment number: e.g. AXX-2a-L1|

### Fire compartment numbering

| Building | - | Level | - | seq Number |
|-----------------------------------|
| 50 | - | 01 | - | 1 |
| 50 | - | XX (multistorey department) | - | 2a (sub compartment 'a' of compartment '2') | 


### Schedules

Schedules which are placed on sheets call up the following properties:

| Property | Formatting | Comments|
|-------------------|
| AREA_COMPARTMENT_GROUP_BVN  | Hidden field | used for filtering areas belonging to a particular fire department only|
| Number | as is | - |
| Area | 0 decimal places| calculate totals |

The schedule name contains the area type e.g. 'Patient Care and Treatment'

![Typical Door Jamb Detail_A]({{ site.baseurl }}/assets/s1607004_inh/FireDepartmentSchedule.svg){:class="img-responsive"}{: height="400px" width="600px"}

### Tags

| Purpose | Family | Image |
|--------------------------|
| Area Tag | 083 - Fire Area Tag.rfa | |
| FH/ FHR New | 0831 - FHR FH Tag - NEW.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_NEW.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| FH New | 0831 - FH Tag - NEW.rfa | ![FH NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_NEW.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| FHR New | 0832 - FHR Tag - NEW.rfa | ![FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FHR_NEW.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| FH/ FHR Existing | 0831 - FHR FH Tag - EX.rfa | ![FH FHR EX]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| FH Existing | 0831 - FH Tag - EX.rfa |  ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_EX.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| FHR Existing | 0832 - FHR Tag - EX.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| Required Fire Egress Tag | 083 - Required Fire Exit Tag.rfa | ![Required Fire Egress]({{ site.baseurl }}/assets/s1607004_inh/083_RequiredExit.svg){:class="img-responsive"}{: height="100px" width="100px"} |
| Required door swing direction | 083 - Required Direction Tag.rfa | ![Required Swing Direction]({{ site.baseurl }}/assets/s1607004_inh/083_RequiredSwingDirection.svg){:class="img-responsive"}{: height="100px" width="100px"} |








