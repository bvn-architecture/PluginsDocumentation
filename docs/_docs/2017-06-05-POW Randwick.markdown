---
title:  "Revit setup of POW Hospital"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Everything relating to Revit on POW"
modified:
layout: "sample"
categories: Revit
---

# Document Numbering

## <a id="ZoneIdentifier"></a> ZONE / BUILDING

The documentation packages are set up by building. Below is a map showing the existing campus with building number.

![KeyMap]({{ site.baseurl }}/assets/s1606008_rcr/KeyPlan.svg){:class="img-responsive"}{: height="546px" width="309px"}

| Building Number | Building Description |
|--------------|---------------|
| 07 | PARKES & CSB |
| 09 | HYPERBARIC UNIT |
| 15 | DICKINSON - Emergency Department - Transitional Works |
| 15R | DICKINSON - Renal |
| 16 | CAMPUS CENTRE |
| 17 | RHW |
| 50 | NEW ACUTE SERVICES BUILDING |
| 51 | CAR PARK |
| 52 | TEMPORARY BUILDING |

## <a id="PackageIdentifier"></a> CATEGORY / PACKAGES AVAILABLE

Each individual zone is than broken up in documentation packages as follows:

| Package Number | Package Description | Links |
|--------------|---------------|---|
| A1 - INTRODUCTORY | Introductory documents. ie. drawing lists, cover page | |
| A2 - SITE | Anything site related including site works | |
| A3 - STAGING | Anything related to staging of works |  |
| B1 - EXISTING | Plans describing the existing conditions | |
| B2 - PROPOSED | Plans describing the proposed conditions | |
| B3 - FIRE COMPARTMENT | Fire compartment drawings as required | |
| B4 - PARTITIONS | Partition plans | |
| B5 - WALL PROTECTION | Wall protection plans | |
| C1 - EXTERNAL ELEVATIONS | External elevations overall | |
| C2 - FACADE DETAILS | All details relating to the building envelope | |
| D1 - BUILDING SECTIONS | Overall building sections | |
| E1 - REFLECTED CEILING PLANS | Ceiling plans | |
| F1 - FLOOR FINISHES | Floor finishes plans | |
| F2 - WALL FINISHES | Wall finishes plans | |
| G0 - ROOM LAYOUT SHEETS - GENERIC | The required generic room layout sheets |[RLS Sheet numbering](#RLSGenericNumbering), Refer also Nepean Hospital Documentation: [RLS Generic Sheet](#RLSGenerics), [RLS Sheet content](#RLSSheetContent) |
| G1 - ROOM LAYOUT SHEETS - SPECIFIC | Room layout sheets of all rooms not matching a generic room | |
| G2 - LINE OF HEIGHTS | Typical line of heights drawings | |
| J1 - INTERNAL DOORS AND WINDOWS | Plans showing internal doors and windows codes and location | |
| J2 - DOOR AND WINDOW SCHEDULE | Schedules of internal doors and windows | |
| K1 - INTERFACE DETAILS PARTITIONS | Typical internal partition details | |
| K2 - INTERFACE DETAILS - CEILINGS | Typical internal ceiling details | |
| M1 - JOINERY | Joinery scoping plans | |
| M2 - JOINERY DETAILS | Joinery details | |
| M3 - METALWORKS DETAILS | Metal works details | |
| S1 - SIGNAGE | Signage plans | |
| T1 - LANDSCAPE | Landscape plans | |
| Q1 - MEMBRANE DRAWINGS | Membrane scoping plans | |
| U1 - DEMOLITION DRAWINGS | Demolition scoping plans | |
| V1 - CONCRETE SETOUT DRAWINGS | Concrete setout plans | |
| Z1 - SPECIFICATION | Specification sections , T-Sheet | |

## Model Numbering - Acute Service Building

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | [Model Type](#ModelType) | - | XXXX |

 <a id="ModelTtpe"></a> Model Type:

| Code | Model Type |
|------|----------|
| RVT | Revit model |
| NWC | NavisWorks NWC file |
| IFC | Industry Foundation Class file |

Sample model number: RCR-BVN-AR-50-RVT-0001 : New Acute Services Building - Revit Model

## Model Numbering - ED Transitional Works

| Project Code | - | Organization Code | - | Discipline Code | - | Document Type | - | Zone / Building | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [Model Type](#ModelType) | - | [refer here](#ZoneIdentifier)| - | XXXX |

These model differ in numbering since they where issued prior to implementing a consultant wide numbering scheme. Once the that scheme was approved it was to late to go back and renumber the documents on Aconex.
Sample model number: RCR-BVN-AR-RVT-15-0001:ED Transitional Works

Overview of current models and their Aconex document number:

![RevitFilesMap]({{ site.baseurl }}/assets/s1606008_rcr/REVIT MODELS BY ZONE.svg){:class="img-responsive"}{: height="476px" width="821px"}

## Standard Doc's

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Category / Package | - | Level | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | [refer here](#DocType) | - | [refer here](#PackageIdentifier) | - | [refer here](#LevelList) | - | 01 |

### <a id="DocType"></a> DOCUMENT TYPE

| Code | Type |
|------|----------|
| DWG | Drawing |
| SCH | Schedule |
| SPC | Specification |
| RPT | Report |

For further Document type codes refer to POW Redevelopment [Project Configuration Manual](https://au1.aconex.com/FileDownload?_action=downloadFile&projectId=1476398068&controlledDocumentId=949133621552704703&accessReason=IMPORTANT_DOCUMENT) on Aconex Task page.

### <a id="LevelList"></a> LEVEL

| Level | Number |
|------|------|
| Basement X | Bx |
| Ground Floor | 00 |
| Levels 1 to 9 above ground | 01-09 |
| Levels 10 and above | 10 - |
| Non Level | XX |

List of sample document numbers:

| Sample number | Document description |
|---------------|------------|
| RCR-BVN-AR-50-DWG-A1-XX-01 | New Acute Services Building : Introductory document : Multi Level : drawing no 1. |
| RCR-BVN-AR-50-DWG-A1-XX-01-DWG | Autocad DWG file of RCR-BVN-AR-50-DWG-A1-00-01 pdf file |
| RCR-BVN-AR-50-SCH-J2-00-01-XLS | Original Excel file of RCR-BVN-AR-50-SCH-J2-00-01 pdf file containing door schedule|
| RCR-BVN-AR-50-SPC-Z1-0555 | ARCHITECTURAL SPECIFICATION - SANITARY APPLIANCES/FITTINGS which is NatSpec section 0555| 

## Sketches

| Project Code | - | Discipline Code | - | Document Type| - | Sequential Number |
| -------------|---|-----------------|---|--------------|---|-------------------|
| RCR | - | AR | - | SK | - | 001 |

Sample Sketch number: RCR-AR-SK-001

## <a id="RLSGenericNumbering"></a> Room Layout Sheets - Generics

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type| - | Category / Package | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | DWG | - | G0 | - | 001 |

Sample Generic Room Layout sheet number: RCR-BVN-AR-50-DWG-G0-001 :

## Room Layout Sheets - Specifics

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Category / Package | - | Room Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | DWG | - | G1 | - | as per dRofus |

Sample Specific Room Layout sheet number: RCR-BVN-AR-50-DWG-G1-TBC :

## User Group related drawings

| Discipline Code | - | Zone / Building | - | Document Type | - | User group | - | Level | - | Number |
| ----------------|---|---------------|---|-----------------|---|------------|---|-------|---|--------|
| AR | - | [refer here](#ZoneIdentifier) | - | SK | - | UG | - | 01 | - | 000 |

Sample number : AR-50-SK-UG-01-000

## Revisions

File names show the revisions right behind the document number in square brackets to allow for [supersede candidate](https://protect-eu.mimecast.com/s/zM1FB7zDRiZ) function to work in Aconex.
RCR-BVN-AR-50-DWG-A1-XX-01[01] - Document Name.pdf

Revisions are alphanumeric up until a document gets issued for construction. After that the revision changes to numerics.

Drawings are only clouded once they have been issued for construction.


## Title blocks - Room Layout sheets

These title blocks come in A2 and A3 sizes and have a sign off bar for SD and one for DD incorporated. Both title blocks have properties adjusting the sign off bar as follows:

| Property | use |
|----------|-----|
| SignOff_HealthPlanningConsultant | Contains the name of the health planning consultant to be shown in the sign off bar. |
| SignOff_LHD Name | Contains the name of the Local Health District to be shown in the sign off bar. |
| Sign_Off_ProjectManager | Contains the name of the Project Manager to be shown in the sign off bar. |

Families used:

* Titleblock_C_SHEET_A3_ANN_RCR
* Titleblock_C_SHEET_A2_ANN_RCR
* Titleblock_Landscape_Vertical_A1_ANN_RCR
* Titleblock_Landscape_Vertical_B1_ANN_RCR

Note: These families use catalogue files to handle the different options available.

Type naming:

| Project Prefix | Building | Sheet Size | Description | Note |
|----------------|----------|------------|-------------|------|
| RCR | 50 | B1 | no privilege no sign off| privilege: displays "CONFIDENTIAL & COMMERCIAL-IN-CONFIDENCE", Sign Off shows a sign off bar for user group consultation. |

Sample: RCR - 50 - B1 no privilege no sign off:  Randwick Hospital, Buildings 50 (new acute services building), B1 sheet size, no privileges shown, no sign off bar shown.

# Existing Emergency Department Transitional Works

## Site set-out

The survey reference point chosen for the POW ED refurbishments works is SSM51804  as per survey cover sheet 'Randwick', reference number 43147DT, project number 30744, dated 15/06/15.
This survey point is located at (M.G.A) : North 6245643.193, East 337291.821 , R.L. 65.572 (A.H.D.) on High Street, Randwick.

![six Maps]({{ site.baseurl }}/assets/s1606008_rcr/2017-06-05 11_05_48-SIX Maps.png){:class="img-responsive"}{: height="1200px" width="1800px"}

Note: The Site survey point in RCR-BVN-AR-RVT-15-0001 - ED Transitional Works.rvt Revit file is not pinned! Revit moves the point to  North 6245643.193, East 337291.8231  when attempting to pin it...

## Revit File linking

Consultants are to link the RCR-BVN-AR-RVT-15-0001 - ED Transitional Works.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* RCR-BVN-AR-RVT-15-0022 - ED CAD Link File.rvt
* RCR-BVN-AR-RVT-15-0021 - ED Existing Building File.rvt
* RCR-BVN-AR-00-RVT-0001 - Site File.rvt

![Model Linking]({{ site.baseurl }}/assets/s1606008_rcr/ModelLinking.svg){:class="img-responsive"}{: height="230px" width="750px"}

Consultants are also to 'Copy Monitor' levels and grids from RCR-BVN-AR-RVT-15-0001 - ED Transitional Works.rvt Revit file.

# New Acute Services Building

## Site set-out

The survey reference point chosen for the POW New Acute Services Building works is the boundary corner of the newly acquired lots indicated as the red rectangle in the the below image. The coordinates of that corner are (M.G.A) : North 6245409.520, East 337066.416 , R.L. 0.0 (A.H.D.)

![Overall Site]({{ site.baseurl }}/assets/s1606008_rcr/Building50_SiteOverall.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

The closest grid intersection is located relative to the above point as per image below:

![GridSetout]({{ site.baseurl }}/assets/s1606008_rcr/Building50_Setout.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

## Revit File linking

Consultants are to link the RCR-BVN-AR-50-RVT-0001 - New Acute Services Building.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* RCR-BVN-AR-50-RVT-0002 - Facade.rvt
* RCR-BVN-AR-50-RVT-0021 - Existing Buildings.rvt
* RCR-BVN-AR-50-RVT-0022 - CAD Links.rvt

Consultants are also to 'Copy Monitor' levels and grids from RCR-BVN-AR-50-RVT-0001 - New Acute Services Building.rvt Revit file.

### Facade Rhino Linking

The Rhino file was set up based on the City of Sydney Rhino model with a little translation to move the origin close to Randwick:

0,0,0 equals (M.G.A.): North: 6245509.425, East: 337284.698

In order to incorporate the different origin points of the Rhino files and Revit building file (refer above) the Revit facade file was located as follows:

* Create a new project file from BVN template
* Cleaned Project file
* Activate Model Management / True North View
* Imported Rhino model using Revit 2018 Import CAD file dialogue 
	* This will import the Rhino model using Origin to Origin
* Select 'Generic Model' as host

![RhinoLinking_01]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_01_justLinked.svg){:class="img-responsive"}{: height="467px" width="1084px"}

* Linked Base Building Revit model using 'Auto - Origin to Origin' option into Facade file.

![RhinoLinking_02]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_02_BaseBuildLinked_NotMoved.svg){:class="img-responsive"}{: height="655px" width="1084px"}

* Moved Base Building File Revit model within the Facade file to suite location of imported Rhino model in plan and section.

![RhinoLinking_03]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_03_BaseBuildLinked_Moved.svg){:class="img-responsive"}{: height="524px" width="997px"}

* Acquired Coordinates from Base Building model.

![RhinoLinking_04]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_04_BaseBuildLinked_CoordinatesAcquired.svg){:class="img-responsive"}{: height="471px" width="1085px"}

* done

This means Base Building File and Facade file do not share the same origin and require linking using Shared Coordinates. A new revit model should be ideally be created when translating the Rhino model to Revit to allow Origin to Origin linking.

### Updating the Facade from Rhino

The current Rhino facade export is located here:

![RhinoExport_01]({{ site.baseurl }}/assets/s160x00x_common/RhinoExportWorkFlow.svg){:class="img-responsive"}{: height="500px" width="600px"}

### Exporting to 3DS Max

There is a 3D view setup in the Facade file: EXPORT TO MAX which displays the linked base build model and the imported Rhino model over layed in the same location.

## Worksets

| Name | Description |
|------|-------------|
| 00_FACADE | EXTERIOR ELEMENTS SUCH AS ROOF, EXTERIOR WALLS, DOORS, WINDOWS, SHADING DEVICES |
| 10_STRUCTURE | STRUCTURAL ELEMENTS SUCH AS FOUNDATIONS, FLOOR SLABS, COLUMNS, FRAMING AND BEAMS |
| 20_VERTICAL CIRCULATION | STAIRS, RAMPS, RAILINGS, LIFTS, SERVICE RISERS |
| 30_INTERIOR | INTERIOR ELEMENTS SUCH AS INTERIOR WALLS/ PARTITIONS, LININGS, INTERIOR DOORS AND WINDOWS, CEILINGS |
| 40_FF&E | ALL FURNITURE, FIXTURES AND EQUIPMENT |
| 50_SITE | TOPOGRAPHY, PLANTS AND TREES, EXISTING BUILDINGS |
| 51_ENTOURAGE | PEOPLE, ANIMALS, VEHICLES |
| 60_MASSING | CONCEPTUAL MASSING OBJECTS (EXCL. EXISTING BUILDINGS) |
| 70_SPARE | SPARE |
| 80_SPARE | SPARE |
| 91_LINK_CONSULTANT_XXX | REVIT LINK FROM STRUCTURAL, MECHANICAL OR ELECTRICAL CONSULTANT  |
| 98_LINK_CAD_XXX | REVIT LINK HOSTING CAD LINKS  |
| 98_LINK_BVN_XXX | REVIT LINK WITHIN BVN PROJECT (EACH REVIT LINK REQUIRES ITS OWN WORKSET  |
| 99_LEVELS AND GRIDS | ALL LEVELS, GRIDS AND/OR SCOPE BOXES |


# Rooms

## <a id="RLSGenerics"></a> Generic Rooms

Generic Rooms for the Schematic Design stage are located in s1607004-AR-INH-GENRIC.rvt Revit file.

The following rooms will be captured:

| Room Code | Room Name |
|-----|------|
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

## Room Numbering

Proposal is to number rooms as follows:

| Department Number | . | Sub Department Number | . | Sequential Number | Use | Sample Number |
|-----------------------------------------------------------------| ---|-----|
| 01 - 90 as per dRofus | . | 01-90 as per dRofus | . | 000-999 as per dRofus | standard rooms | 01.02.099 |
| 01 - 90 as per dRofus | . | 99 | . | 000-999 as required | corridors within a department | 01.99.001 |
| 98 | . | level e.g. 07 | . | 600-699 as required | EDB's in and outside a department| 98.07.601 |
| 98 | . | level e.g. 06 | . | 700-799 as required | FHR's in and outside a department| 98.06.701 |
| 99 | . | level e.g. 05 | . | 000-799 as required | corridors outside a department | 99.05.001 |
| 99 | . | level e.g. 05 | . | 800-899 as required | stairs | 99.05.801 |
| 99 | . | level e.g. 05 | . | 900-999 as required | lifts | 99.05.901 |

## Room Properties

The following room properties are used when creating Room Layout Sheets (RLS) either to donate a finish or use and briefed vs designed area:

| Name | Type | Usage |
|---------|
| Area | build in | The designed area of a room measured to centre line walls |
| Base Finish | build in | not used |
| Ceiling Finish | build in | not used |
| Ceiling Height | 7edd1d61-613f-4f38-a458-4a23e2b48624 | Populated by dRofus to check against the modelled |
| Comments | build in  | not used |
| Department | build in | not used at generics |
| Department Code | bb1df597-4d80-4530-8a20-b4c13c2bcd28 | not used at generics |
| FFETemplateMatch | ceaa812a-d84c-4f5d-a40c-6b13ffc6ff77 | Indicates whether a room matches a generic room exactly in terms of FFE |
| Floor Finish | build in | Used to show the floor finish via a room tag (Room Finishes Tag_ANN.rfa) |
| Name | build in | The briefed name of the room. |
| Number | build in | The briefed code of the room. |
| Sub-Department  | d2222bf6-3335-4ba5-9856-7ea6506002d6 | TBC |
| Flux Id | | not used |
| Wall Finish | build in | not used |

## <a id="RLSSheetContent"></a> Room Layout Sheets

Room layout sheets show the arrangement of equipment and fixtures within a room. They comprise of:

* Floor plan
	* does not show wall finishes (e.g. wall vinyl)
	* shows corner guards and crash rails
* Elevations of all walls 
	* does not show  loose furnitures (chairs) -> work out a filter system to switch them off
* 3D Axo to convey the layout in 3D during the user group process
* FFE schedule
	* Sorted by DetailedCategory Parameter
	* Shows:
		* Item Code
		* Item Description
		* Item Quantity
		* Wall protection with quantity for the time being (check against dRofus briefed quantity)
	* Does not show yet
		* Item Group -> might not be know at this point or not required by client (tbc)

All plans and elevations are in scale 1 to 50. Ideally all room layout sheets are on the same size sheets (A3). This might require 2 or more sheets for larger rooms.

### Tagging

Tag family to be used: FF&E Tag_ANN.rfa

Tagged in floor plan:

* Floor Finish
* Loose furniture & Joinery
* Assemblies (Bed heads or wash hand basins)
* Corner Guards (but not crash rails)

Tagged in Elevations:

* Services items placed on walls
* Same items as floor plans
* Wall finishes if modelled
* Wall protection

### Additional Graphics

As a separate item a 300 x 300 set out grid is to be placed on all elevations. Revit Family: Elevation_Setout_Grid_ANN.rfa 
There are 3 types available:

* 2400mm High Ceiling
* 2700mm High Ceiling
* 3000mm High Ceiling

## FFE Library (Unifi)

 BVN is using [Unifi](http://unifilabs.com/) in order to avoid having to maintain multiple revit family libraries in their respective project folders.
 The following process is proposed to work with unifi:
 
A single library on I drive : ''I:\BIM\2.0 Project_Revit Library\__ClinicalLibrary'' is  maintained as the source for any upload to unifi. Families will be created and amended in this folder. After a family has been uploaded to the Health_FF&E library on Unifi it becomes available in all project files.

![Unifi_workflow]({{ site.baseurl }}/assets/s160x00x_common/Unifi_process.svg){:class="img-responsive"}{: height="644px" width="1394px"}

## dRofus

### Team structure

### Technical issues
In the moment there is technical limitations to dRofus:
To make our work as easy as possible, BVN uses what is called Items with sub items in dRofus. An example would be a TV (the item) with a power point and data outlet (both sub items):

![drofus_subItems]({{ site.baseurl }}/assets/s160x00x_common/Drofus_Item_SubItem.svg){:class="img-responsive"}{: height="237px" width="171px"}

Where blue belongs to architecture and orange to services in terms of responsibility. The catch is that dRofus currently does not allow a split like the above without some work around. They are working on it to fix it but have not committed to a time frame.

### dRofus - New Build workflow

Nepean and Randwick SD phase (new builds -> generic rooms only)

* BVN will take control and therefore responsibility of all items (including services). 
* Services consultants however will be asked to export Services to Excel and furnish BVN with the completed Excel document which we will import back into dRofus. As per the below diagram. Again blue is BVN and orange the consultants.

![drofus_workflow_new]({{ site.baseurl }}/assets/s160x00x_common/Drofus_NewBuild_Works.svg){:class="img-responsive"}{: height="328px" width="1387px"}

# Fire Compartment Drawings

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

## Custom shared parameter properties

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

## Fire compartment numbering

For ease of identification the following numbering scheme has been applied to the fire / smoke compartments.

| Building | - | Level | - | seq Number |
|-----------------------------------|
| 50 | - | 01 | - | 1 |
| 50 | - | XX (multi storey department) | - | 2a (sub compartment 'a' of compartment '2') |

## Compartment Schedules

In order to show the overall size of a fire compartment, which can be made up of multiple smoke departments on the same floor or spanning multiple floors, schedules have been placed summarizing the compartment area. These schedules call up the following properties:

| Property | Formatting | Comments|
|-------------------|
| AREA_COMPARTMENT_GROUP_BVN  | Hidden field | used for filtering areas belonging to a particular fire department only|
| Number | as is | - |
| Area | 0 decimal places| calculate totals enabled|

The schedule name contains the area type e.g. 'Patient Care and Treatment'. This is important since different area types allow for different maximum compartment area.

![Typical Fire Department Schedule]({{ site.baseurl }}/assets/s160x00x_common/FireDepartmentSchedule.svg){:class="img-responsive"}{: height="200px" width="300px"}

## Tags

The following tags are used to indicate location of fire fighting equipment as well as required fire egress and egress direction.

| Purpose | Family | Image |
|--------------------------|
| Area Tag | 083 - Fire Area Tag.rfa | |
| FH/ FHR New | 0831 - FHR FH Tag - NEW.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s160x00x_common/083_FH_FHR_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH New | 0831 - FH Tag - NEW.rfa | ![FH NEW]({{ site.baseurl }}/assets/s160x00x_common/083_FH_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FHR New | 0832 - FHR Tag - NEW.rfa | ![FHR NEW]({{ site.baseurl }}/assets/s160x00x_common/083_FHR_NEW.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH/ FHR Existing | 0831 - FHR FH Tag - EX.rfa | ![FH FHR EX]({{ site.baseurl }}/assets/s160x00x_common/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FH Existing | 0831 - FH Tag - EX.rfa |  ![FH FHR NEW]({{ site.baseurl }}/assets/s160x00x_common/083_FH_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| FHR Existing | 0832 - FHR Tag - EX.rfa | ![FH FHR NEW]({{ site.baseurl }}/assets/s160x00x_common/083_FH_FHR_EX.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| Required Fire Egress Tag | 083 - Required Fire Exit Tag.rfa | ![Required Fire Egress]({{ site.baseurl }}/assets/s160x00x_common/083_RequiredExit.svg){:class="img-responsive"}{: height="70px" width="70px"} |
| Required door swing direction | 083 - Required Direction Tag.rfa | ![Required Swing Direction]({{ site.baseurl }}/assets/s160x00x_common/083_RequiredSwingDirection.svg){:class="img-responsive"}{: height="70px" width="70px"} |

# Doors

## Door Types and Sizes

For a more in depth explanation of the varies door types ans sizes available refer to this [post]({{ site.baseurl }}/_docs/2017-06-02-Doors)

## Door numbering

Doors numbers are made up of two parts: the number of a room a doors belongs to and an instance counter of doors placed in a room.

Sample: 1234-D01 refers to a door belonging to room 1234 with instance counter of D01 (door number one).

In general a door belongs to the room it opens into. There are however a few exceptions of this rule:

* External doors opening outwards
* Doors to EDB's or similar in corridors
* Doors to en-suites opening into the bed room

One questions raised from time to time is: why do we show the room number in a big space consuming door tag if there is a room tag showing the same information adjacent? Two reasons:

* To avoid ambiguity in situations like doors opening into corridors (refer to door numbering exceptions above)
* To avoid the requirement to re-code a door if the swing direction changes after the door schedule has been issued for the first time.

## Door Families

The following Revit door families are used:

| Door family name | Use | Graphic |
|---------------------------|
| 045_SINGLELEAF_GENERIC | single leaf internal door | ![DoorSingle_Graphic]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoor_Single.svg){:class="img-responsive"}{: height="90px" width="90px"} |
| 045_DOUBLELEAF_GENERIC | double leaf (equal and un-equal size) | ![DoorDouble_Equal]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoor_Double.svg){:class="img-responsive"}{: height="90px" width="90px"} ![DoorDouble_UnEqual]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoor_DoorHalf.svg){:class="img-responsive"}{: height="90px" width="90px"} |
| DOR-SINGLE EXISTING-L300-BVN | single leaf existing door | ![DoorExistingSingle_Graphic]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoorsExisting_Single.svg){:class="img-responsive"}{: height="90px" width="90px"} |
| DOR-DOUBLE EXISTING-L300-BVN | double leaf existing door | ![DoorExistingDoubleEq_Graphic]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoorsExisting_DoubleEqual.svg){:class="img-responsive"}{: height="90px" width="90px"} ![DoorExistingDoubleUnEq_Graphic]({{ site.baseurl }}/assets/s160x00x_common/TypicalDoorsExisting_Double_unequal.svg){:class="img-responsive"}{: height="90px" width="90px"}|

Revit door properties used to number a door:

| Property | GUID | Use |
|----------------------|
| Door Room Reference | 8ede47f8-0912-46e7-a94e-276e517d887c | the number of the room the door belongs to.  |
| Door Instance By Room | 8232f501-0c37-45a2-af93-97c8c707c928 | instance counter of doors placed in a room. e.g. D01 |
| Door Finish External | 3210bfb2-7735-4be7-bdbc-3f27cf6fe618 | Finish of door opening to side. |
| Door Finish Internal | c72ee8d5-5681-43f5-9bb8-dddd9773f26b | Finish of door opening from side. |

The two door finish properties are used (tagged) on the wall protection series of drawings. The default field (when the same finsih is to be used on both sides) is Door Finish External.

There has also an additional filter been added to the F2 Wall Finishes template which will colour all doors red if there is a value in the Door Finish External field.

## AS 1428

The door family (single leaf) has approach clearances as per AS 1428 build in. These are accessible via the 1428_Diagram property:

| 1428_Diagram Property Value | Approach Graphic |AS 1428 Figure Code |
|----------|----------|--------------------|
| 1 | ![AS1428_1]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_1.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (a) |
| 2 | ![AS1428_2]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_2.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (b) |
| 3 | ![AS1428_3]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_3.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (c) |
| 4 | ![AS1428_4]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_4.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (d) |
| 5 | ![AS1428_5]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_5.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (e) |
| 6 | ![AS1428_6]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_6.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (f) |
| 7 | ![AS1428_7]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_7.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (g) |
| 8 | ![AS1428_8]({{ site.baseurl }}/assets/s160x00x_common/Doors_AS1428_8.svg){:class="img-responsive"}{: height="90px" width="90px"} | Figure (h) |

## Door Tags

Revit door tag: Door Tag_ANN.rfa is used to display the door number.

This tag has a couple of types:

| Tag Type | Usage | Graphics |
|-----------|-----|----|
| Internal | For internal doors | ![DoorTagInternal]({{ site.baseurl }}/assets/s160x00x_common/Doors_Tag_Internal.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| External | For external doors, usually covered in a separate schedule | ![DoorTagExternal]({{ site.baseurl }}/assets/s160x00x_common/Doors_Tag_External.svg){:class="img-responsive"}{: height="200px" width="200px"} |

Door Finish External Tag_ANN is used to display the external door finish code.
Door Finish Internal Tag_ANN is used to display the internal door finsih code.

![DoorTagFinish]({{ site.baseurl }}/assets/s160x00x_common/Tag_Door Finish.svg){:class="img-responsive"}{: height="200px" width="200px"}

## Existing Door Family Properties

The existing door families have some extra properties to allow to indicate that they

* Require painting
* Require to be re-hang
* Require additional door protection

# Internal Windows

## Window numbering

Window numbers are made up of two parts: the number of a room a window belongs to and an instance counter of windows placed in a room.

Sample: 1234-W01 refers to a window belonging to room 1234 with instance counter of W01 (window number one).

In general windows can be randomly assigned to a room if they are in between two rooms as opposed to a  window between a corridor and a room. In that situation the window belongs to the room not the corridor.

| Property | GUID | Use |
|------|-------------|------|
| Window Comments | 7289c039-4d33-49e5-ab72-d34c5cd61599 | Any comments |
| Window Room Reference Number| 1601011a-378c-4edd-999a-9c2ca99630af | The number of the room the window belongs to. |
| Window Instance By Room | 0d5020a5-1c5c-4e57-a004-83b82997f7f4 | Instance counter of windows placed in a room. e.g. W01 |

Revit window tag: Window Tag_ANN.rfa

# Annotation

## Dimension Styles

In summary:

* default text size for dimensions is 2.0mm
* default font is Arial Narrow

Below is a table of our default dimension styles:

| Name | Type | Description | Comments |
|------|------|-------------|----------|
| 45 Diagonal Line_2.0mm Text_BVN | Linear Dim style | Text size 2mm, tick mark: 45 Diagonal_BVN, no CL Symbol | Should be used as default if no CL is required |
| BVNDH 2.0mm with CL | Linear Dim style | Text size 2mm, tick mark: 45 Diagonal_BVN, CL Symbol: Centreline_ANN : Type 1| Should be used as default if CL is required |
| 45 Arrow_2.0mm Text_BVN | Linear Dim style | Text size 2mm, tick mark: 45 Arrow_Line_BVN, no CL Symbol | Should be used as only if extent is shown |
| 45 Arrow_2.0mm Text_BVN | Angular Dim style | Text size 2mm, tick mark: 45 Arrow_Line_BVN, no CL Symbol | Should be used as default when arrows are required as tick mark |
| 45 Diagonal Line_2.0mm Text_BVN | Angular Dim style | Text size 2mm, tick mark: 45 Diagonal_BVN, no CL Symbol | Should be used as default when diagonal lines are required as tick mark |
| 45 Arrow_2.0mm Text_BVN | Radial Dim style | Text size 2mm, tick mark: 45 Arrow_Line_BVN, no CL Symbol | Should be used as default when arrows are required as tick mark |
| 45 Diagonal Line_2.0mm Text_BVN | Radial Dim style | Text size 2mm, tick mark: 45 Diagonal_BVN, no CL Symbol | Should be used as default when diagonal lines are required as tick mark |
| 45 Arrow_2.0mm Text_BVN |Diameter Dim style | Text size 2mm, tick mark: 45 Arrow_Line_BVN, no CL Symbol | Should be used as default when arrows are required as tick mark |
| 45 Diagonal Line_2.0mm Text_BVN | Diameter Dim style | Text size 2mm, tick mark: 45 Diagonal_BVN, no CL Symbol | Should be used as default when diagonal lines are required as tick mark |
| Spot Elevation_BVN | Spot Elevation | Text size 2mm | Default spot elevation |
| Spot Coordinate_BVN | Spot Coordinate | Text size 2mm | Default spot coordinate |
| Spot Slope_BVN | Spot Slope Text size 2mm | Default slope dimension |