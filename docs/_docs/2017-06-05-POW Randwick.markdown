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
| B3 - FIRE COMPARTMENT | Fire compartment drawings as required | [Fire](#Fire Compartments) |
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
| J1 - INTERNAL DOORS AND WINDOWS | Plans showing internal doors and windows codes and location |[Doors](#DoorStuff) |
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
| 97 | - | 01 - 05 | - | 000-999 as required | plant rooms | 97.01.001 - Mechanical plant, 97.02.001 Electrical plant, 97.03.001 Hydraulic plant |
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

### Room Layout Sheet - Schedules

Schedules are sorte by the 'DetailedCategory' field.

* All unions will need to have the an empty 'DetailedCategory' field to avoid the actually union code showing up in the schedule.
* All items nested into a union will need their 'DetailedCategory' field linked to the 'ItemCode' field of the union itself so they schedule under the respective union code.
	* This also applies to moveable items like chairs or bins within a union!
		* Some of these nested items have 'DetailedCategory' field as type driven rathern then instance driven. In that case a switch will need to be introduced to allow selecting an instance based value.

### Tagging

Tag family to be used: FF&E Tag_ANN.rfa

Tagged in floor plan:

* Floor Finish
* Loose furniture & Joinery
* Unions (i.e. Bed heads or wash hand basins, WC's, showers) show the union code only
* MSP's show the union code only
* Corner Guards (but not crash rails)


Tagged in Elevations:

* Services items placed on walls
* Same items as floor plans
* Unions (i.e. Bed heads or wash hand basins, WC's, showers) show the nested item codes only but not the union code
* MSP's show the union code only
* Wall finishes if modelled
* Wall protection

### Additional Graphics

As a separate item a 300 x 300 set out grid is to be placed on all elevations. Revit Family: Elevation_Setout_Grid_ANN.rfa 
There are 3 types available:

* 2400mm High Ceiling
* 2700mm High Ceiling
* 3000mm High Ceiling

## <a id="Unifi"></a> Unifi

 BVN is using [Unifi](http://unifilabs.com/) in order to avoid having to maintain multiple revit family libraries in their respective project folders.
 The following process is proposed to work with unifi:
 
A single library on I drive : ''I:\BIM\2.0 Project_Revit Library\__ClinicalLibrary'' is  maintained as the source for any upload to unifi. Families will be created and amended in this folder. After a family has been uploaded to the Health_FF&E library on Unifi it becomes available in all project files.

![Unifi_workflow]({{ site.baseurl }}/assets/s160x00x_common/Unifi_process.svg){:class="img-responsive"}{: height="644px" width="1394px"}

Before uploading content to unifi please ensure that:

* Purge unused (multiple times untill nothing is left to purge)
* Ensure thumbnail preview is displaying properly 
	* 2D families: all reference planes are minimised to the extent of the tag
	* 3D families: dimensions are switched off

## dRofus

### Team structure

The current team structure is as follows:

![drofus_TeamStructure]({{ site.baseurl }}/assets/s160x00x_common/dRofusTeamStructure.svg){:class="img-responsive"}{: height="830px" width="1249px"}

### Technical issues

In the moment there is technical limitations to dRofus:
To make our work as easy as possible, BVN uses what is called Items with sub items in dRofus. An example would be a TV (the item) with a power point and data outlet (both sub items):

![drofus_subItems]({{ site.baseurl }}/assets/s160x00x_common/Drofus_Item_SubItem.svg){:class="img-responsive"}{: height="237px" width="171px"}

Where blue belongs to architecture and orange to services in terms of responsibility. The catch is that dRofus currently does not allow a split like the above without some work around. They are working on it to fix it but have not committed to a time frame.

* * Packages in dRofus are to be referred to as Unions in Revit. 
	* A Union is a generic model 'holder' for a number of nested elements (e.g. MSP or HWB)
* A sub-item in dRofus is referred to as a nested item in Revit.
	* The main family will have another family nested into it (e.g. Refrigerator with GPO)

* Generally the list Kate printed of Packages used on NBH was acceptable with a few additions as below: 
	* MSP's 
	* Services Provisions for computers and monitors etc.
	* Computers and Monitors themselves (with the services provision packages nested in) - this way we have more flexibility in documentation. 

* No longer want to nest sub-items without an alphabetic suffix (for example on NBH we nested the GPOs into a computer family without a suffix which were attached to an instance based mounting height reference plane which we could amend). Allows room for error and also isn't ideal on the FFF & E list on the RLS as lists separately. 
* Some concerns about us doing a lot of the services consultants work in the early stages (esp. electrical) as now dRofus will show logs of BVN users making changes and potentially mistakes. However we decided this was most efficient as past experience has shown us that the consultants don't have great experience with dRofus and are not involved in early user group consultation. 
* Package numbering system to be established.
* Discussions around items which can be difficult to quantify (i.e. curtain tracks along multiple bed bays). Suggestion of changing these to responsibility INDES was not ideal as could lead to conflicting approaches with other items. Possible solution could be to make quantity always '1' in dRofus.
* Child items need to be reflected in dRofus at some stage (possibly at beginning of DD) so bi-directional syncing will work.


Another issue is the way Health Infrastructure has set up the actual function structure of their database. Whilst the structure itself is 3 levels deep, the actual room function number only reflects the first two of those levels and Functional Group has been excluded:

![drofus_FunctionStructure]({{ site.baseurl }}/assets/s160x00x_common/dRofusFunctionStructure.svg){:class="img-responsive"}{: height="259px" width="482px"}

Unfortunately this default Health infrastructure seetting can not be changed by BVN. We can, however inforce the use of two digits to identify a level.

### dRofus - New Build workflow

Nepean and Randwick SD phase (new builds -> generic rooms only)

* BVN will take control and therefore responsibility of all items (including services). 
* Services consultants however will be asked to export Services to Excel and furnish BVN with the completed Excel document which we will import back into dRofus. As per the below diagram. Again blue is BVN and orange the consultants.

![drofus_workflow_new]({{ site.baseurl }}/assets/s160x00x_common/Drofus_NewBuild_Works.svg){:class="img-responsive"}{: height="217px" width="925px"}

To implement changes into made during the desing process into dRofus the leader of each Department will notify Jess D and Jan who will update dRofus accordingly. Department leaders are as per below table:

| Department | Health lead |
|----------|-----|
| 01 Emergency Department | Kim |
| 02 EDSSU | Kim |
| 03 Helipad | Joseph |
| 04 Psychiatric Emergency Care Centre (PECC) | Kim |
| 05 Front of House | Conor |
| 06 Front of House - Retail | Conor |
| 07 Front of House - ETR | Conor |
| 08 IPU P4 | Jess D |
| 09 IPU P5 | Jess D |
| 10 IPU P6 | Jess D |
| 11 IPU P7 | Jess D |
| 12 IPU P8 | Jess D |
| 13 MAU | Jess D |
| 14 ICU | Kim |
| 15 Perioperative | Kirstie |
| 16 CSSD | Kirstie |

### Logging changes

In the moment drofus allows to log changes in individual rooms against change lists. Changes to room templates however are only logged into a single log. This is a limitation dRofus is adressing in the moment.
Logging changes needs to be activated manually. All changes will be logged against the same change list until the user chooses another change list or stops logging changes alltogether. 

Change lists are named as follows: 
 
| Project Stage | _ | Date | _ | Changelist type |

|Changelist type | where to use |
|----------------|--------------|
| XX User Group Meeting No. XX | New change list to be created for each user group meeting. |
| Client Requested Change | Used when making changes resulting from client requested changes. Unless directed otherwise by BVN a single change list is to be used for all of these type of changes. |
| Consultant Advice Change | Used when making changes which result from specialist advice from disciplines. A single change list is created for all disciplines. |
| QA Check | Used to track changes made during checking processes. |

To enable us to associate a change in a template to a change list, we use the work around of starting the change log note in the room template with the change list name:

> SD_20170823_QA Check The item was deleted because of XYZ >

### dRofus coding

Joinery:

* Suffixes like .01 describe different sizes (depth, width, height) of an item 

Benches:

* Suffixes describe different mounting height only since drofus codes prescribe the bench depth, and length is variable most of the time

Equipment:

* Should not be using suffixes to describe a different item size since this will be a different product to be purchased (unlike joinery where every piece will be made according to our detail drawings)
* Different size = different product = different code
* This means that new items (not already in drofus database) will get a different code on Randwick compared to Nepean. To avoid accidental cross use of families, we will add a suffix to the family name to delineate between Randwick (RCR_ASB, RCR_ED) and Nepean(NHR_NEW, NHR_CAN) (i.e. Basin_Handwash_TypeB_RCR_HYBA_010 vs Basin_Handwash_TypeB_NHR_HYBA_010). These will also get tagged with their project name to support better searching within unifi.

Left and right version of the same item i.e. wash hand basin

* For now stays the same code for left hand and right hand product but have different Revit Families

MSP's'
Where the same items are included and it is only the physical setout that varies we would have one MMSP code in dRofus (to brief the content to the room) then Children of that Parent code to cover the different layouts in our Revit model. For example: MMSP-001 with three different setouts of the same content would be documented as MMSP-001.01, MMSP-001.02 and MMSP-001.03.

As soon as there is different content/quantities of items, it is a new MMSP code.

#### Family Parameters

| Parameter name | Parameter description | Comments|
|----------------|-----------------------|---------|
| ItemCode | The actual drofus item code plus an optional suffix describing mounting height or sizes | Shown on Room Layout sheets |
| ItemDescription | Human readable short description of the item | I.e. CUPBOARD,full height, lockable |
| ItemGroup | Purchasing group | Transfer items are described as at item group + 'T' |
| Keynote | Built in Revit family parameter. | Needs to have a value set in the family file when using text catalogue files. Otherwise Revit will display an error message: "Family XYZ Keynote does not exist in Family"

#### Transfer Items

Transfer items will require a new code and therfore a new Revit family. DRofus will assign to the transfer items the next number avaialble in the system. That means that a standard group 1 to 3 item code might vastly differ to the code of the same item when it is a transfer item.
For example standard code: FRIDGE: drugs, large code is MMGE-034. The transfer item will get a code in the 500+ range: i.e. MMGE-501. 

Family setup: 

* item code as well as family type name will show a 'T' for transfer: i.e. 'MMGE-501T' since we not always schedule out the item group which will also get a T appended i.e. '3T'
* Keynote will just point to the dRofus code :i.e. MMGE-501 (without the 'T')

#### Items outside of room

Sometimes there will be the need to place an item outside the perimeter of a room but have it showing up in the FFE schedule for a particular room. i.e. Alcohol rub dispensers mounted in the corridor adjacent to the entry door to a room.
In this case we need to create a new family where the room calculation point property is enabled and the room calculation point is placed appropriately. Families created for this type of use will have a suffix "_OutSideRoom_" in their file name i.e.: Dispenser_Soap_AlcoholRub_OutSideRoom_FIDI_001. The ItemDescription should also include "outside room".

#### Request for items process:

When requesting a new family please state:

* Whether this is: 
    * a new item ( and drofus needs to generate a code)
        * Please provide a general description of the item to be added to drofus 
		* Please provide the item group
		* Provide a screenshot of how that thing is meant to look like ( a picture says more than a 1000 words somebody famous once said )
    * An existing item: Please provide the drofus code the existing item


As a side note: drofus does only support suffixes in code when describing parent - child relationships. Lets not go there just yet.

### dRofus to PushIt

#### Filing of SOA Push It! files

In the moment we are still receiving some Excel files in addition to dRofus. These excel files as well as the Excel files used to create Push It! files are stored in their relevant Department folder. 
However Push It! files themselves are located at: 

> \Admin\01.0 Proj. Management\1.06 Design Data & Brief\_SOA PushIt >

This location may contain the push it file for the entire SOA as well as specific department push it files. They are to be named as follows:

| Department Push It! file | (Date)(Department) PushIt.txt | 20170910 ED PushIt.txt |
| Entire SOA Push It! file | (Date) PushIt (Version).txt | 20170910 PushIt v0_8.txt |

Outdated Push It files are to be moved into the superseded folder:

> \Admin\01.0 Proj. Management\1.06 Design Data & Brief\_SOA PushIt\Superseded >

#### Exporting dRofus to Push It!

The dRofus to Push It export process consists of the following steps:

* Supersede the old Push It txt file (move it into the supersede folder)
* Export the current dRofus database to Excel using a custom export
* Convert the dRofus Excel report into a Push It text file

Each dRofus database has a custom report set up which is used to export to Push It:

![dRofus Schedule Export Interface]({{ site.baseurl }}/assets/s160x00x_common/dRofus_Export_01.png){:class="img-responsive"}{: height="541px" width="811px"}

Save the file as:
'drofusExport.xlsx' .
to:
'\Admin\01.0 Proj. Management\1.06 Design Data & Brief\_SOA PushIt''

Open the Excel conversion file named: 
"dRofus to PushIt.xlsx"

![dRofus Excel conversion]({{ site.baseurl }}/assets/s160x00x_common/dRofus_Export_02.png){:class="img-responsive"}{: height="713px" width="963px"}

Make sure data gets refreshed (Enable editing and press 'Refresh All' in the Excel DATA tab )

Save As Push It file to:
'\Admin\01.0 Proj. Management\1.06 Design Data & Brief\_SOA PushIt''

![dRofus Excel conversion]({{ site.baseurl }}/assets/s160x00x_common/dRofus_Export_03.png){:class="img-responsive"}{: height="719px" width="975px"}

Select OK when Excel asks about multiple sheets:

![dRofus Excel conversion]({{ site.baseurl }}/assets/s160x00x_common/dRofus_Export_04.png){:class="img-responsive"}{: height="153px" width="770px"}

Close the Exel file (Click NO when Excel asks about keeping file type)

Reload the new SOA file into Push It.

# <a id="Fire Compartments"></a> Fire Compartment Drawings

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

# <a id="PartitioStuff"></a> Partitions

## Partition and wall types

Partition and wall types are sub divided into:

| Type | Pre - fix |
|------|-----------|
| Accoustic Rated Partitions | P |
| Fire and Smoke rated partitions | F - Fire, S - Smoke |
| Wall Linings | L |
| Blockwork | BLK-1xx |
| Panel System | BLK-2xx |

Partition types are distributed via [unifi] (#Unifi).

## Tags

| Tag Family | Tag Type | Usage | Graphics | Sample |
|-----------|-----|----|----|----|
| Impact | TBC | High impact lining on all walls -outermost lining to be impact resistant lining (IL-106) to all walls on the side of the hatched space up to 1200AFFL only. Substitue or add in accordance with the specification. | ![Tag_Wall_HighImpact_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_HighImpact.svg){:class="img-responsive"}{: height="188px" width="160px"} | ![Tag_Wall_HighImpact_Sample]({{ site.baseurl }}/assets/s160x00x_common/Tag_Impact_Sample.svg){:class="img-responsive"}{: height="188px" width="160px"} |
| Impact specfic walls| TBC | High impact lining on all specific walls -outermost lining to be impact resistant lining (IL-106) to all walls on the side of the hatched space up to 1200AFFL only. Substitue or add in accordance with the specification. | ![Tag_Wall_HighImpact_Specific_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_HighImpact_Specific.svg){:class="img-responsive"}{: height="188px" width="160px"} | TBC |
| Insulation | TBC |Thermal insulation within wall lining INS-301 50mm, UNO | ![Tag_Wall_Insulation_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_Insulation.svg){:class="img-responsive"}{: height="188px" width="160px"} | TBC |
| Riser | TBC | Acoustic rated hydraulic stack (refer partition details) | ![Tag_Wall_Riser_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_Riser.svg){:class="img-responsive"}{: height="188px" width="160px"} |![Tag_Wall_Riser_Sample]({{ site.baseurl }}/assets/s160x00x_common/Tag_Riser_Sample.svg){:class="img-responsive"}{: height="48px" width="194px"}  |
| Direct Stick | TBC | Line all masonry walls within room with 9mm fibrous cement sheet 'direct stick' to wall. All cavities and voids to be filled to prevent vermin etc. Refer masonry package for substrate types. | ![Tag_Wall_DirectStick_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_DirectStickFC.svg){:class="img-responsive"}{: height="188px" width="160px"} | TBC |
| Interior Finish | TBC | Interior finish applied over specifc part of wall (refer interiors package) | ![Tag_Wall_InteriorFinish_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_InteriorFinish.svg){:class="img-responsive"}{: height="188px" width="160px"} | TBC |
| Low Height | TBC | Low ht wall - Height in mm AFFL | ![Tag_Wall_LowHeight_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_LowHeight.svg){:class="img-responsive"}{: height="188px" width="160px"} | ![Tag_Wall_LowHeight_Sample]({{ site.baseurl }}/assets/s160x00x_common/Tag_LowHeight_Sample.svg){:class="img-responsive"}{: height="180px" width="257px"} |
| Radiation Shielding | TBC | Radiation Shielding required on all walls of room. Refer to Radiation Shielding Report for shielding scope and details. | ![Tag_Wall_Radiation_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_RadiationShielding.svg){:class="img-responsive"}{: height="188px" width="160px"} | ![Tag_Wall_Radiation_Sample]({{ site.baseurl }}/assets/s160x00x_common/Tag_Radiation_Sample.svg){:class="img-responsive"}{: height="275px" width="256px"} |
| Wet Area Lining (all walls) | TBC | Wet area lining on all walls of room. - outermost lining to be moisture resistant plasterboard (IL-102). Substitue or add in accordance with the specification. | ![Tag_Wall_WetAreaAllWalls_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_WetAreaLining.svg){:class="img-responsive"}{: height="188px" width="160px"} | ![Tag_Wall_WetAreaGen_Sample]({{ site.baseurl }}/assets/s160x00x_common/Tag_WetArea_Sample.svg){:class="img-responsive"}{: height="103px" width="127px"} |
| Wet Area Lining (specific walls) | TBC | Wet area lining on specific part of wall. See above note and details. | ![Tag_Wall_WetAreaSpecificWall_Graphic]({{ site.baseurl }}/assets/s160x00x_common/Tag_Wall_WetAreaLining_Specific.svg){:class="img-responsive"}{: height="188px" width="160px"} | TBC |

# <a id="DoorStuff"></a> Doors

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

| Tag Family | Tag Type | Usage | Graphics |
|-----------|-----|----|----|----|
| Door Tag_ANN.rfa | Internal | For internal doors. Shows door room reference and door instance number. | ![DoorTagInternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Doors_Internal.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Tag_ANN.rfa | External | For external doors, usually covered in a separate schedule. Shows door room reference and door instance number. | ![DoorTagExternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Doors_External.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Finish External Tag_ANN | Colour | Is used to display the external door finish code. | ![DoorTagFinishExternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Door Finish.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Finish Internal Tag_ANN | Colour | Is used to display the internal door finish code. | ![DoorTagFinishInternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Door Finish_Internal.svg){:class="img-responsive"}{: height="200px" width="200px"} |

### Defining door paint scope in refurb

The wall finishes drawings contain a filter which will colour all doors red which have the ''Door Finish External'' property set. Or in other words: all doors coloured red are within the paint scope of the refurb project. 

Default paint colour of doors can be defined through a cover note: All doors shown red are to be painted with PT-XXX unless noted otherwise.

If a door has the same finish applied to both sides use the ''Door Finish External'' property to show (tag) that finish only. In any other case use the ''Door Finish External'' and ''Door Finish Internal'' property and tag as required. 

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

# Colours

## Standard Department Colours

There are usually two shades, a light and and a dark, of each colour available. The light shades is usually meant to colour circulation meanwhile the darker shade is for briefed elements.

| Light | RGB | Dark | RGB |
|------|------|-------------|----------|
| ![LightGreen]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Green.svg){:class="img-responsive"}{: height="200px" width="200px"} | 217,231,203 | ![DarkGreen]({{ site.baseurl }}/assets/s160x00x_common/Colour_Dark_Green.svg){:class="img-responsive"}{: height="200px" width="200px"} | 198,211,180 |
| ![LightBlue]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Blue.svg){:class="img-responsive"}{: height="200px" width="200px"} | 227,237,244 | ![DarkBlue]({{ site.baseurl }}/assets/s160x00x_common/Colour_Dark_Blue.svg){:class="img-responsive"}{: height="200px" width="200px"} | 198,217,232 |
| ![LightRed]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Red.svg){:class="img-responsive"}{: height="200px" width="200px"} | 240,221,221 | ![DarkRed]({{ site.baseurl }}/assets/s160x00x_common/Colour_Dark_Red.svg){:class="img-responsive"}{: height="200px" width="200px"} | 226,197,184 |
| ![LightMagenta]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Magenta.svg){:class="img-responsive"}{: height="200px" width="200px"} | 236,224,243 | ![DarkMagenta]({{ site.baseurl }}/assets/s160x00x_common/Colour_Dark_Magenta.svg){:class="img-responsive"}{: height="200px" width="200px"} | 215,204,230 |
| ![LightGold]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Gold.svg){:class="img-responsive"}{: height="200px" width="200px"} | 241,226,186 | ![DarkGold]({{ site.baseurl }}/assets/s160x00x_common/Colour_Dark_Gold.svg){:class="img-responsive"}{: height="200px" width="200px"} | 241,203,118 |
| ![LightYellow]({{ site.baseurl }}/assets/s160x00x_common/Colour_Light_Yellow.svg){:class="img-responsive"}{: height="200px" width="200px"} |250,250,210 | n/a | n/a |

## Area Briefed vs Area Designed Colours

The SP families internally computate the diversion of the desinged area to the briefed as a precentage figure

Families are coloured in percentage steps as shown in the table below.

| Sample | Description |
|------|--------|
| ![Colour_Area_Equal]({{ site.baseurl }}/assets/s160x00x_common/Colour_Area_Equal.svg){:class="img-responsive"}{: height="400px" width="400px"}  | Green tones are on area within 20 percent of the briefed area (dark green 0 to +-10 percent, light green + 10 to + 20 percent) |
| ![Colour_Area_Under]({{ site.baseurl }}/assets/s160x00x_common/Colour_Area_Under.svg){:class="img-responsive"}{: height="400px" width="400px"} | Red tones are under area by more then 20 percent (20-50 percent, 50 percent and above) |
| ![Colour_Area_Over]({{ site.baseurl }}/assets/s160x00x_common/Colour_Area_Over.svg){:class="img-responsive"}{: height="400px" width="400px"} | Blue tones are above briefed area by more then 20 percent (20-50 percent, 50 percent and above) |

| Colour | RGB |
|---|---|
| Dark Green | 26,150,65 |
| Light Green | 166,217,106 |
| Orange | 253,174,97 |
| Red | 215,25,28 |
| Light Blue | 171,217,233 |
| Dark Blue | 44,123,182 |

## Floor Finishes Colours

| Colour Sample | RGB | Code | Colour Sample | RGB | Code |
|------|------|-------|------|------|------|------|
| ![FL-101a]({{ site.baseurl }}/assets/s160x00x_common/FL-101a.svg){:class="img-responsive"}{: height="200px" width="200px"} | 166, 189, 219 | FL-101a |![FL-301]({{ site.baseurl }}/assets/s160x00x_common/FL-301.svg){:class="img-responsive"}{: height="200px" width="200px"} | 199, 233, 192 | FL-301 |
| ![FL-101b]({{ site.baseurl }}/assets/s160x00x_common/FL-101b.svg){:class="img-responsive"}{: height="200px" width="200px"} | 158, 202, 225 | FL-101b |![FL-302]({{ site.baseurl }}/assets/s160x00x_common/FL-302_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 233, 239, 209 | FL-302 |
| ![FL-101c]({{ site.baseurl }}/assets/s160x00x_common/FL-101c.svg){:class="img-responsive"}{: height="200px" width="200px"} | 222, 235, 247 | FL-101c |![FL-302a]({{ site.baseurl }}/assets/s160x00x_common/FL-302a.svg){:class="img-responsive"}{: height="200px" width="200px"} | 211, 239, 234 | FL-302a |
| ![FL-102]({{ site.baseurl }}/assets/s160x00x_common/FL-102_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 191, 206, 213 | FL-102 |![FL-302b]({{ site.baseurl }}/assets/s160x00x_common/FL-302b.svg){:class="img-responsive"}{: height="200px" width="200px"} | 179, 225, 214 | FL-302b |
| ![FL-104]({{ site.baseurl }}/assets/s160x00x_common/FL-104.svg){:class="img-responsive"}{: height="200px" width="200px"} | 218, 218, 235 | FL-104 |![FL-303]({{ site.baseurl }}/assets/s160x00x_common/FL-303_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 206, 223, 215 | FL-303 |
| ![FL-105]({{ site.baseurl }}/assets/s160x00x_common/FL-105_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 236, 226, 240 | FL-105 |![FL-305]({{ site.baseurl }}/assets/s160x00x_common/FL-305.svg){:class="img-responsive"}{: height="200px" width="200px"} | 226, 243, 186 | FL-305 |
| ![FL-106]({{ site.baseurl }}/assets/s160x00x_common/FL-106_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 180, 177, 214 | FL-106 |![FL-501]({{ site.baseurl }}/assets/s160x00x_common/FL-501.svg){:class="img-responsive"}{: height="200px" width="200px"} | 253, 212, 158 | FL-501 |
| ![FL-201]({{ site.baseurl }}/assets/s160x00x_common/FL-201.svg){:class="img-responsive"}{: height="200px" width="200px"} | 252, 187, 161 | FL-201 |![FL-502]({{ site.baseurl }}/assets/s160x00x_common/FL-502_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 254, 230, 206 | FL-502 |
| ![FL-701]({{ site.baseurl }}/assets/s160x00x_common/FL-701_Series.svg){:class="img-responsive"}{: height="200px" width="200px"} | 229, 216, 189 | FL-701 | | | |
