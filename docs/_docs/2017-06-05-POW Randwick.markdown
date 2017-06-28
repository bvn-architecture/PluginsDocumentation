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

* 07 - PARKES & CSB
* 09 - HYPERBARIC UNIT
* 15 - DICKINSON - Emergency Department - Transitional Works
* 15R - DICKINSON - Renal
* 16 - CAMPUS CENTRE
* 17 - RHW
* 50 - NEW ACUTE SERVICES BUILDING
* 51 - CAR PARK
* 52 - TEMPORARY BUILDING

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
| G0 - ROOM LAYOUT SHEETS - GENERIC | The required generic room layout sheets |[RLS Sheet numbering](#RLSGenericNumbering), [RLS Generic Sheet](#RLSGenerics), [RLS Sheet content](#RLSSheetContent), |
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
| Z1 -SPECIFICATION | Specification sections , T-Sheet | |

## Model Numbering

| Project Code | - | Organization Code | - | Discipline Code | - | Document Type | - | Zone / Building | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | [Model Type](#ModelType) | - | [refer here](#ZoneIdentifier) | - | XXXX |

 <a id="ModelTtpe"></a> Model Type:

| Code | Model Type |
|------|----------|
| RVT | Revit model |
| NWC | NavisWorks NWC file |

Sample model number: RCR-BVN-AR-RVT-50-0001 : New Acute Services Building - Revit Model

Overview of current models and their Aconex document number:

![RevitFilesMap]({{ site.baseurl }}/assets/s1606008_rcr/REVIT MODELS BY ZONE.svg){:class="img-responsive"}{: height="900px" width="800px"}

## Standard Doc's

| Project Code | - | Organization Code | - | Discipline Code | - | Document Type | - | Zone / Building | - | Category / Package | - | Level | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | DWG | - | [refer here](#ZoneIdentifier) | - | [refer here](#PackageIdentifier) | - | 01 | - | 01 |

### <a id="DocType"></a> DOCUMENT TYPE

* DWG - Drawing
* XXX - Schedule
* YYY - Specification

### LEVEL

* XX:  non level (Section/ Elevations/ typical details)
* 01: Level 01

Sample document number: RCR-BVN-AR-DWG-50-A1-XX-01 : New Acute Services Building : Introductory document : Multi Level : drawing no 1.

## <a id="RLSGenericNumbering"></a> Room Layout Sheets - Generics

| Project Code | - | Organization Code | - | Discipline Code | - | Document Type | - | Zone / Building | - | Category / Package | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | DWG | - | [refer here](#ZoneIdentifier) | - | G0 | - | 001 |

Sample Generic Room Layout sheet number: RCR-BVN-AR-DWG-50-G0-001 :

## Room Layout Sheets - Specifics

| Project Code | - | Organization Code | - | Discipline Code | - | Document Type | - | Zone / Building | - | Category / Package | - | Room Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| RCR | - | BVN | - | AR | - | DWG | - | [refer here](#ZoneIdentifier) | - | G1 | - | as per dRofus |

Sample Specific Room Layout sheet number: RCR-BVN-AR-DWG-50-G1-TBC :

## User Group related drawings

| Discipline Code | - | Document Type | - | Zone / Building | - | User group | - | Level | - | Number |
| ----------------|---|---------------|---|-----------------|---|------------|---|-------|---|--------|
| AR | - | SK | - | [refer here](#ZoneIdentifier) | - | UG | - | 01 | - | 000 |

Sample number : AR-SK-50-UG-01-000

## Title blocks - Room Layout sheets

These title blocks come in A2 and A3 sizes and have a sign off bar for SD and one for DD incorporated. Both titleblocks have properties adjusting the sign off bar as follows:

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

Family type Prefixes used:

* RCR - Randwick

# Existing Emergency Department Transitional Works

## Site set-out

The survey reference point chosen for the POW ED refurbishments works is SSM51804  as per survey cover sheet 'Randwick', reference number 43147DT, project number 30744, dated 15/06/15.
This survey point is located at (M.G.A) : North 6245643.193, East 337291.821 , R.L. 65.572 (A.H.D.) on High Street, Randwick.

![six Maps]({{ site.baseurl }}/assets/s1606008_rcr/2017-06-05 11_05_48-SIX Maps.png){:class="img-responsive"}{: height="1200px" width="1800px"}

Note: The Site survey point in s1606008-AR-RCR-ED Transitional Works.rvt Revit file is not pinned! Revit moves the point to  North 6245643.193, East 337291.8231  when attempting to pin it...

## Revit File linking

Consultants are to link the s1606008-AR-RCR-ED Transitional Works.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* s1606008-AR-RCR-ED CAD Link File.rvt
* s1606008-AR-RCR-Existing Building File.rvt
* s1606008-AR-RCR-Site File.rvt

![Model Linking]({{ site.baseurl }}/assets/s1606008_rcr/ModelLinking.svg){:class="img-responsive"}{: height="800px" width="400px"}

Consultants are also to 'Copy Monitor' levels and grids from s1606008-AR-RCR-ED Transitional Works.rvt Revit file.

## Fire Compartment Drawings

The Fire Compartment drawings are done as Area Plans of type: 'FIRE COMPARTMENT'. 

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


# New Acute Services Building

## Site set-out

The survey reference point chosen for the POW New Acute Services Building works is the boundary corner of the newly acquired lots indicated as the red rectangle in the the below image. The coordinates of that corner are (M.G.A) : North 6245409.520, East 337066.416 , R.L. 0.0 (A.H.D.)

![Overall Site]({{ site.baseurl }}/assets/s1606008_rcr/Building50_SiteOverall.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

The closest grid intersection is located relative to the above point as per image below:

![GridSetout]({{ site.baseurl }}/assets/s1606008_rcr/Building50_Setout.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

## Revit File linking

Consultants are to link the S1606008-AR-RCR-NewBuild File.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* s1606008-AR-RCR-Site File.rvt

Consultants are also to 'Copy Monitor' levels and grids from S1606008-AR-RCR-NewBuild File.rvt Revit file.

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

![RhinoLinking_01]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_01_justLinked.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

* Linked Base Building Revit model using 'Auto - Origin to Origin' option into Facade file.

![RhinoLinking_02]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_02_BaseBuildLinked_NotMoved.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

* Moved Base Building File Revit model within the Facade file to suite location of imported Rhino model in plan and section.

![RhinoLinking_03]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_03_BaseBuildLinked_Moved.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

* Acquired Coordinates from Base Building model.

![RhinoLinking_04]({{ site.baseurl }}/assets/s1606008_rcr/RhinoLinking_04_BaseBuildLinked_CoordinatesAcquired.svg){:class="img-responsive"}{: height="1200px" width="1800px"}

* done

This means Base Building File and Facade file do not share the same origin and require linking using Shared Coordinates. A new revit model should be ideally be created when translating the Rhino model to Revit to allow Origin to Origin linking.

### Updating the Facade from Rhino

The current Rhino facade export is located here:

![RhinoExport_01]({{ site.baseurl }}/assets/s1606008_rcr/RhinoExportWorkFlow.svg){:class="img-responsive"}{: height="500px" width="600px"}

### Exporting to 3DS Max

There is a 3D view setup in the Facade file: EXPORT TO MAX which displays the linked base build model and the imported Rhino model over layed in the same location.
