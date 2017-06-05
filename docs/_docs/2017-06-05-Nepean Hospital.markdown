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

TBC

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

### Room Properties

The following room properties are used when creating Room Layout Sheets (RLS) either to donate a finish or use and briefed vs designed area:
| Name | Type | Usage |
| Area | build in | The designed area of a room measured to centre line walls |
| Base Finish | build in | not used |
| Ceiling Finish | build in | not used |
| Ceiling Height | TBC | Populated by dRofus to check against the modelled |
| Comments | build in  | not used |
| Department | build in | not used at generics |
| Department Code | TBC | not used at generics |
| FFETemplateMatch |  | Indicates whether a room matches a generic room exactly in terms of FFE |
| Floor Finish | build in | Used to show the floor finish via a room tag (Room Finishes Tag_ANN.rfa) |
| Name | build in | The briefed name of the room. |
| Number | build in | The briefed code of the room. |
| Sub-Department  | | TBC |
| Unique Id | | TBC |
| Wall Finish | build in | not used |

## Room Layout Sheets

Room layout sheets show the arrangement of equipment and fixtures within a room. They comprise of:

* Floor plan
* Reflective ceiling plan
* Elevations of all walls
* 3D Axo to convey the layout in 3D
* FFE schedule

All plans and elevations are in scale 1 to 50. Ideally all room layout sheets are on the same size sheets (A3). This might require 2 or more sheets for larger rooms.

### Tagging

Tag family to be used: 

Tagged in floor plan:

* Room name and Number (tag family)
* Beds
* loose furniture

Tagged in Elevations

* Services items placed on walls


Tagged in RCP

*


## Fire Compartment Drawings

Fire Compartment drawings show smoke and fire compartmentation of a building floor by floor. They inform:

* Fire / smoke compartment sizes across a single floor or spanning multiple floors
* Which stairs are fire egress stairs
* location of smoke rated lobbies to fire egress stairs
* Which walls require a smoke or fire rating
* Which ceilings require a smoke or fire rating
* Which doors require a smoke or fire rating
* Which direction egress doors have to swing
* Where internal or external drenchers are required

In Revit the Fire Compartment drawings are done as Area Plans of type: 'FIRE COMPARTMENT'. This allows to draw areas indicating compartments on top of the proposed or existing layouts. These areas, in turn, can be coloured in to show clearly the extent of a compartment as well as tagged and scheduled out.

### Custom shared parameter properties

The following table shows the usage of Revit's build in area properties as well as the following custom properties (shared parameters).

| Property | GUID | use |
|-----|
| Area Type | build in | not used |
| AREA_COLOUR_BVN  | acac3c63-7165-4dd9-b648-c086e0ddde48 | Area colour fill scheme uses this property to colour in areas |
| AREA_COMPARTMENT_GROUP_BVN  | 4955f5a0-86fb-4fee-8184-7ae85716bebe| Used when a fire department spreads across multiple levels and therefore requires a number of areas to be drawn to capture its full extent. |
| | | Fire compartment schedule filters all area instance with the same fire compartment group number |
| AREA_TYPE_BVN  | 1bcf8295-93ea-4c10-85ce-40b879fd31d5 | Can be used to differentiate between 'Patient Care and Treatment' vs 'Ancillary' areas. This parameter is more flexible than the build in 'Area Type' which only has a fixed non changeable number of values |
| Name | build in |type of department: e.g. SMOKE |
| Number | build in | Fire compartment number: e.g. AXX-2a-L1|

### Fire compartment numbering

For ease of identification the following numbering scheme has been applied to the fire / smoke compartments.

| Building | - | Level | - | seq Number |
|-----------------------------------|
| 50 | - | 01 | - | 1 |
| 50 | - | XX (multi storey department) | - | 2a (sub compartment 'a' of compartment '2') |


### Compartment Schedules

In order to show the overall size of a fire compartment, which can be made up of multiple smoke departments on the same floor or spanning multiple floors, schedules have been placed summarizing the compartment area. These schedules call up the following properties:

| Property | Formatting | Comments|
|-------------------|
| AREA_COMPARTMENT_GROUP_BVN  | Hidden field | used for filtering areas belonging to a particular fire department only|
| Number | as is | - |
| Area | 0 decimal places| calculate totals enabled|

The schedule name contains the area type e.g. 'Patient Care and Treatment'. This is important since different area types allow for different maximum compartment area.

![Typical Door Jamb Detail_A]({{ site.baseurl }}/assets/s1607004_inh/FireDepartmentSchedule.svg){:class="img-responsive"}{: height="200px" width="300px"}

### Tags

The following tags are used to indicate location of fire fighting equipment as well as required fire egress and egress direction.

| Purpose | Family | Image |
|--------------------------|
| Area Tag | 083 - Fire Area Tag.rfa | |
| FH/ FHR New | 0831 - FHR FH Tag - NEW.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH New | 0831 - FH Tag - NEW.rfa | ![FH NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FHR New | 0832 - FHR Tag - NEW.rfa | ![FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FHR_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH/ FHR Existing | 0831 - FHR FH Tag - EX.rfa | ![FH FHR EX]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH Existing | 0831 - FH Tag - EX.rfa |  ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FHR Existing | 0832 - FHR Tag - EX.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s1607004_inh/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| Required Fire Egress Tag | 083 - Required Fire Exit Tag.rfa | ![Required Fire Egress]({{ site.baseurl }}/assets/s1607004_inh/083_RequiredExit.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| Required door swing direction | 083 - Required Direction Tag.rfa | ![Required Swing Direction]({{ site.baseurl }}/assets/s1607004_inh/083_RequiredSwingDirection.svg){:class="img-responsive"}{: height="70px" width="70px"} |








