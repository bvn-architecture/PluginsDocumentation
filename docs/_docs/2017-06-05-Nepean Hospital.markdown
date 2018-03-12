---
title:  "Revit setup of Nepean Hospital"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Everything relating to Revit on Nepean Hospital"
modified:
layout: "sample"
categories: Revit
---

# Document Numbering - New build, including the car park

![KeyMap_NewNumbers]({{ site.baseurl }}/assets/s1607004_inh/KeyPlan_CPB_Numbers.svg){:class="img-responsive"}{: height="609px" width="529px"}

## Document Number Overview

| PROJECT NAME | - | ORGANISATION | - | DOC / DRAWING TYPE | - | DISCIPLINE | - | AREA | - | ELEMENTS / PACKAGE | DRAWING / INFORMATION SERIES | - | LEVEL* | ZONE | SEQUENCE   | - | REVISION |
|+------------+|+-+|+------------+|---|--------------------|---|------------|---|------|--------------------|------------------------------|---|--------|------|------------|---|----------|
| NHR | - | BVN | - | [doc type](#Drawing_DocType) | - | ARC | - | [Area List](#Drawing_AreaList) | - | [Element List](#Drawing_Elements) | [Series List](#Drawing_Series) | - | [Level List](#Drawing_Level) | [Zone List](#Drawing_Zone) | [Sequence List](#Drawing_Sequence) | - | [Revision](#Drawing_Revision) |

## <a id="Drawing_DocType"></a> Document and Drawing Types

List of document types:

| Document Type | Description |
|--------------|---------------|
| DRW | DRAWING |
| REP | REPORT |
| SKT | SKETCH |
| SCH | SCHEDULE |
| SPE | SPECIFICATION |
| MOD | MODEL |

## <a id="Drawing_AreaList"></a> Area List

List of areas:

| Area | Area Description |
|--------------|---------------|
| CHC | Child Care Centre |
| CMW | Construction works Management |
| COM | Commercial |
| DOC | Doctors Accomodation |
| EBL | East Block |
| GEN | General (all areas) |
| HOP | Hope Cottage |
| MSC | Multistorey Car Park |
| NBL | North Block |
| PCT | Precinct |
| REF | Refurbishment |
| SBL | South Block |
| STM | St Mary's |
| STE | STES |
| TB1 | Tower Building 1 |
| WBL | West Block |

## <a id="Drawing_Elements"></a> Elements and Packages

List of elements and packages

| Element and Packages | Description | Proposed Series |
|--------------|---------------|
| 00 | COVER SHEETS / LEGEND | 00M - SERIES - MODELS |
| 01 | INTRODUCTORY I.E. LOCATION PLANS, SITE PLANS EXISTING AND PROPOSED | 01A - SERIES - INTRODUCTORY |
| 10 | GENERAL ARRANGEMENT OR OVERALL DRAWING - 1:200 (AT CAR PARK) 1:500 OR BIGGER AT HOSPITAL TOWER | 10B - SERIES - DEPARTMENT PLANS 1 TO 500 |
| 11 | GENERAL ARRANGEMENT DRAWING - 1:200 AT HOSPITAL TOWER | 11B - SERIES - GA PLANS 1 TO 200, 11L - SERIES - FIRE COMPARTMENT PLANS |
| 12 | SPARE | |
| 13 | SPARE | |
| 14 | SPARE | |
| 15 | GENERAL ARRANGEMENT OR OVERALL DRAWING - 1:100 | 15A - SERIES - GA PLANS INTRODUCTORY, 15B - SERIES - GA PLANS 1 to 100, 15C - SERIES - ELEVATIONS, 15D - SERIES - SECTIONS |
| 20 | SITE COMBINED | |
| 21 | DEMOLITION | |
| 22 | PREPARATION AND GROUNDWORK | |
| 23 | SPARE | |
| 24 | LANDSCAPE  STRUCTURES | |
| 25 | LANDSCAPE CULTIVATION | |
| 26 | LANDSCAPE FINISHES (COMBINED) | |
| 30 | STRUCTURE COMBINED | |
| 31 | CONCRETE | 31A - SERIES - CONCRETE INTRODUCTORY, 31B - SERIES - CONCRETE SETOUT PLANS, 31E - SERIES - CONCRETE SETOUT ASSEMBLY DRAWINGS, 31F - SERIES - CONCRETE SETOUT DETAILS |
| 32 | EARTH |
| 33 | MASONRY | 33B - SERIES - MASONRY SETOUT PLANS, 33C - SERIES - MASONRY SETOUT ELEVATIONS, 33D - SERIES - MASONRY SETOUT SECTIONS, 33F - SERIES - MASONRY DETAILS |
| 34 | STEEL |
| 38 | TIMBER |
| 40 | ENCLOSURE COMBINED | 40A - SERIES - FACADE INTRODUCTORY, 40B - SERIES - FACADE SETOUT PLANS, 40C - SERIES - FACADE ELEVATIONS, 40D - SERIES - FACADE SECTIONS, 40E- SERIES - FACADE SYSTEMS ASSEMBLY DRAWINGS, 40F - SERIES - COURTYARDS, 40H - SERIES - HELIPAD SETOUT, 40Y - SERIES - FACADE SCHEDULES |
| 41 | TANKING AND WATERPROOFING |
| 42 | ROOFING COMBINED | 42B - SERIES - ROOF PLAN, 42F - SERIES - ROOF DETAILS |
| 43 | FACADE, EXTERNAL WALLS AND CLADDING | 43B - SERIES - FACADE RCP, 43F - SERIES - FACADE DETAILS |
| 44 | SPARE |
| 46 | WINDOWS, LOUVRES AND GLAZING |
| 47 | INSULATION | 47A - SERIES - INSULATION INTRODUCTORY, 47B - SERIES - INSULATION SETOUT PLANS |
| 48 | STAIRS, RAMPS, BALUSTRADES AND HANDRAILS | 48G - SERIES - STAIR, RAMPS, LIFTS, ESCALATORS, HANDRAILS AND BALUSTRADE ASSEMBLY DRAWINGS, 48H - SERIES - INTERIOR LAYOUTS AND DETAILS, 48J - SERIES - BALUSTRADE DETAILS |
| 49 | EXTERNAL PAINT FINISHES & LINE MARKINGS |
| 50 | INTERIORS COMBINED | 50H - SERIES - GENERIC ROOM LAYOUT SHEETS, 50H - SERIES - INTERIOR LAYOUTS, 50H - SERIES - INTERIOR LIFT DETAILS, 50H - SERIES - SPECIFIC ROOM LAYOUT SHEETS, 50H - SERIES - TYPICAL SETOUT DRAWINGS |
| 51 | PARTITIONS | 51A - SERIES - PARTITION INTRODUCTORY, 51B - SERIES - PARTITION SET OUT PLANS, 51E - SERIES - PARTITION ASSEMBLY DRAWINGS, 51J - SERIES - PARTITION DETAILS, 51Y - SERIES - PARTITION RELATED SCHEDULES |
| 52 | INTERIOR WALLS / PARTITIONS | 52A - SERIES - BLOCKWORK INTRODUCTORY, 52B - SERIES - BLOCKWORK SET OUT PLANS, 52J - SERIES - BLOCKWORK DETAILS |
| 53 | CEILINGS | 53A - SERIES - REFLECTED CEILING INTRODUCTORY, 53B - SERIES - REFLECTED CEILING SETOUT PLANS, 53H - SERIES - REFLECTED CEILING ASSEMBLY DRAWINGS, 53J - SERIES - REFLECTED CEILING DETAILS |
| 54 | ACCESS FLOORS |
| 55 | FABRICATED METALWORK | 55A - SERIES - ARCHITECTURAL METALWORK INTRODUCTORY, 55B - SERIES - ARCHITECTURAL METALWORK SET OUT PLANS, 55F - SERIES - ARCHITECTURAL METALWORK DETAILS, 55Y - SERIES - ARCHITECTURAL METALWORK SCHEDULES |
| 56 | JOINERY | 56A - SERIES - JOINERY INTRODUCTORY, 56B - SERIES - JOINERY PLANS, 56H - SERIES - JOINERY ASSEMBLY DRAWINGS, 56J - SERIES - JOINERY DETAILS, 56Y - SERIES - JOINERY SCHEDULES |
| 57 | LOOSE FURNITURE, FIXTURES, FITTINGS AND EQUIPMENT | 57A - SERIES - FFE INTRODUCTORY, 57B - SERIES - FFE PLANS |
| 58 | SIGNAGE |
| 59 | DOORS AND DOOR HARDWARE | 59A - SERIES - DOORS INTRODUCTORY, 59B - SERIES - DOORS / DOOR FRAMES / HARDWARE 1 to 100, 59J - SERIES - DOORS DETAILS, 59Y - SERIES - DOOR SCHEDULES |
| 60 | INTERNAL FINISHES COMBINED | 60J - SERIES - FINISHES COMBINED DETAILS, 60Y - SERIES - INTERIOR COLOUR SCHEDULES |
| 64 | APPLIED WALL FINISHES COMBINED | 64A - SERIES - WALL FINISHES INTRODUCTORY, 64B - SERIES - WALL FINISHES PLANS, 64H - SERIES - WALL FINISHES ASSEMBLY DRAWINGS, 64J - SERIES - WALL FINISHES DETAILS |
| 65 | APPLIED FLOOR FINISHES COMBINED | 65A - SERIES - FLOOR FINISHES INTRODUCTORY, 65B - SERIES - FLOOR FINISHES PLANS, 65J - SERIES - FLOOR FINISHES DETAILS |
| 66 | WATERPROOFING AND SCREED | 66A - SERIES - WATERPROOFING AND SCREEDS INTRODUCTORY, 66B - SERIES - WATERPROOFING AND SCREEDS PLANS, 66H - SERIES - WATERPROOFING AND SCREENS ASSEMBLY DRAWINGS |
| 67 | PAINTING |
| 68 | WALL PROTECTION | 68A - SERIES - WALL PROTECTION INTRODUCTORY, 68B - SERIES - WALL PROTECTION PLANS |
| 99 | PREMISES | 99L - SERIES - PREMISES PLANS |
| xxZ | SPECIFICATIONS | i.e. NHR-BVN-SPE-ARC-50-31Z-NL00001 - CONCRETE FINISHES SPECIFICATION |


## <a id="Drawing_Series"></a> Drawing and Information Series

List of types:

| Information Series | Description |
|--------------|---------------|
| A | INTRODUCTORY  DRAWINGS |
| B | 1:500 / 1:200 / 1:100 FLOOR PLANS |
| C | 1:1500 / 1:200 / 1:100 ELEVATIONS |
| D | 1: 200 / 1:100 SECTIONS |
| E | 1:50 / 1:20 ASSEMBLY DRAWINGS ( DETAIL PLANS /SECTIONS / ELEVATIONS) |
| F | 1: 10 / 1:5 CONSTRUCTION DETAILS |
| G | CIRCULATION DRAWINGS (STAIRS, RAMPS, LIFTS, ESCALATORS, HANDRAILS & BALUSTRADES) |
| H | 1:50 / 1:20 INTERIOR LAYOUT AND DETAILS DRAWINGS |
| J | 1:10/1:5 INTERIOR DETAILS |
| K | DRAWN SCHEDULES |
| L | AREA PLAN AND ANALYSIS DIAGRAMS I.E. FIRE COMPARTMENT or STAGING DRAWINGS|
| M | MODEL |
| P | PRESENTATION |
| R | REPORT |
| S | SKETCH |
| W | ROOM DATA SHEET |
| X | SCHEDULE OF ACCOMMODATION |
| Y | SCHEDULES |
| Z | SPECIFICATIONS |

## <a id="Drawing_Level"></a> Level Acronyms

List of level acronyms:

| Level | Description |
|--------------|---------------|
| NL | NON- LEVEL SPECIFIC  - ELEVATION / SECTION / GLOBAL DETAILS |
| 00 | GROUND FLOOR |
| 01 | FIRST FLOOR |
| 0x | LEVEL x (SINGLE DIGITS) |
| B1 | BASEMENT LEVEL 1 |

## <a id="Drawing_Zone"></a> Zone List

List of drawing zones:

| Zone | Description |
|--------------|---------------|
| 00 | ENTIRE FLOOR |
| 10, 20, 30, 40 ... | FLOOR DIVISION ZONES SCALE 1 TO 100 |
| 11, 21, 31, 41 ... | FLOOR DIVISION ZONES SCALE 1 TO 50 |

## <a id="Drawing_Sequence"></a> Sequence List

This is a three digits field. First number should always be 001.

## <a id="Drawing_Revision"></a> Revision

Revision methodology 

| Zone | Description |
|--------------|---------------|
| A, B, C, ... | PRE-CONSTRUCTION ISSUE |
| 1, 2, 3, 4 ... | CONSTRUCTION ISSUE |


## Sample Numbers

| Number | Name |
|---|---|
| NHR-BVN-DRW-ARC-PCT-10B-B100001 | HOSPITAL - PRECINCT PLAN - LEVEL B1 |
| NHR-BVN-DRW-ARC-PCT-20L-B100001 | HOSPITAL - PRECINCT STAGING PLAN - LEVEL B1 |
| NHR-BVN-DRW-ARC-TB1-00A-NL00001 | HOSPITAL - COVER SHEET (DRAWING LIST) |
| NHR-BVN-DRW-ARC-TB1-10A-NL00001 | HOSPITAL - GA COVER SHEET |
| NHR-BVN-DRW-ARC-TB1-10B-NL00001 | HOSPITAL - DEPARTMENT DRAWINGS LEVELS B1 TO 03 |
| NHR-BVN-DRW-ARC-TB1-11B-B100001 | HOSPITAL - GENERAL ARRANGEMENT PLAN - LEVEL B1 |
| NHR-BVN-DRW-ARC-TB1-11L-B100001 | HOSPITAL - FIRE COMPARTMENT PLAN - LEVEL B1 |
| NHR-BVN-DRW-ARC-TB1-15B-B110001 | HOSPITAL - GENERAL ARRANGEMENT PLAN - LEVEL B01 - ZONE 1 |
| NHR-BVN-DRW-ARC-TB1-15C-NL00001 | NORTH ELEVATION |
| NHR-BVN-DRW-ARC-TB1-15D-NL00001 | EAST WEST SECTION 1 |
| NHR-BVN-DRW-ARC-TB1-40A-NL00001 | FACADE PACKAGE COVER SHEET |
| NHR-BVN-DRW-ARC-TB1-40E-NL00010 | FACADE SYSTEM SHEET EWS-XX |
| NHR-BVN-DRW-ARC-TB1-48E-NL00001 | METAL WORK - STAIR BALUSTRADES |
| NHR-BVN-DRW-ARC-TB1-50H-XXXXXXX | SPECIFIC ROOM LAYOUT SHEET ROOM XXXXXXX |
| NHR-BVN-DRW-ARC-TB1-50H-NL00001 | BAY - MOBILE EQUIPMENT (4M2) |
| NHR-BVN-DRW-ARC-TB1-50H-NL10001 | TYPICAL SETOUT DRAWING - HANDWASH FACILILTY - TYPE A / TYPE B |
| NHR-BVN-DRW-ARC-TB1-53B-B110001 | CEILING FINISHES PLAN - LEVEL B01 - ZONE 1 |
| NHR-BVN-DRW-ARC-TB1-64B-B110001 | WALL FINISHES PLAN - LEVEL B01 - ZONE 1 | 
| NHR-BVN-DRW-ARC-TB1-65B-B110001 | FLOOR FINISHES PLAN - LEVEL B01 - ZONE 1 |
| NHR-BVN-SPC-ARC-TB1-10Z-NL00001 | ARCHITECTURAL SPECIFICATION |
| NHR-BVN-MOD-ARC-TB1-00M-0010001 | NEW ACUTE SERVICES BUILDING - L00 - REVIT MODEL |

# Document Numbering - Refurb (Cancer Care only)

## <a id="ZoneIdentifier"></a> ZONE / BUILDING

The documentation packages are set up by building. Below is a map showing the existing campus with building number.

![KeyMap]({{ site.baseurl }}/assets/s1607004_inh/KeyPlan.svg){:class="img-responsive"}{: height="609px" width="529px"}

| Building Number | Building Description |
|--------------|---------------|
| A | Block A |
| B | Block B |
| B2 | IPU block above car park |
| C | Block C |
| D | Block D |
| E | Block E |
| I | Block I |
| H | Block H |
| K | New Build - Stage 1 |
| Z1 | Cancer Centre |
| Z2 | Demountable |

## <a id="PackageIdentifier"></a> CATEGORY / PACKAGES AVAILABLE

Each individual zone is than broken up in documentation packages as follows:

| Package Number | Package Description | Links |
|--------------|---------------|---|
| A0 - DA	| DA drawing package | |
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
| G0 - ROOM LAYOUT SHEETS - GENERIC | The required generic room layout sheets |[RLS Sheet numbering](#RLSGenericNumbering), [RLS Generic Sheet](#RLSGenerics), [RLS Sheet content](#RLSSheetContent) |
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

## Model Numbering

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NHR | - | BVN | - | AR | - |  [refer here](#ZoneIdentifier) | - | [Model Type](#ModelType)| - | XXXX |

<a id="ModelTtpe"></a> Model Type:

| Code | Model Type |
|------|----------|
| RVT | Revit model |
| NWC | NavisWorks NWC file |
| IFC | Industry Foundation Class file |

Sample model number: NHR-BVN-AR-K-RVT-0001 : New Building - Stage 1 - Revit Model

Overview of current models and their Aconex document number:

![RevitFilesMap]({{ site.baseurl }}/assets/s1607004_inh/REVIT MODELS BY ZONE_Nepean.svg){:class="img-responsive"}{: height="1261px" width="1944px"}

### Model Notes

| Model | Note |
|-----|----|
| NHR-BVN-AR-ZX-RVT-0001 - Template | Contains: line of height, kit of parts documentation of the cancer centre |

## Standard Doc's

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Category / Package | - | Level | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NHR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | [refer here](#DocType) | - | [refer here](#PackageIdentifier) | - | [refer here](#LevelList) | - | 01 |

### <a id="DocType"></a> DOCUMENT TYPE

| Code | Type |
|------|----------|
| DWG | Drawing |
| SCH | Schedule |
| SPC | Specification |
| RPT | Report |

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
| NHR-BVN-AR-K-DWG-A1-XX-01 | New Acute Services Building : Introductory document : Multi Level : drawing no 1. |
| NHR-BVN-AR-K-DWG-A1-XX-01-DWG | Autocad DWG file of NHR-BVN-AR-K-DWG-A1-00-01 pdf file |
| NHR-BVN-AR-K-SCH-J2-00-01-XLS | Original Excel file of NHR-BVN-AR-K-SCH-J2-00-01 pdf file containing door schedule|
| NHR-BVN-AR-K-SPC-Z1-0555 | ARCHITECTURAL SPECIFICATION - SANITARY APPLIANCES/FITTINGS which is NatSpec section 0555| 

## Development Application (DA) Doc's

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type | - | Category / Package | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NHR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | [refer here](#DocType) | - | A0 | - | XXX |

| Sample number | Document description |
|---------------|------------|
| NHR-BVN-AR-K-DWG-A0-100 | New Acute Services Building : DA drwaing : introductory drawings. |
| NHR-BVN-AR-K-DWG-A0-200 | New Acute Services Building : DA drwaing : floor plan drawings. |
| NHR-BVN-AR-K-DWG-A0-300 | New Acute Services Building : DA drwaing : elevation, section, 3D drawings. |
| NHR-BVN-AR-K-DWG-A0-400 | New Acute Services Building : DA drwaing : facade system drawings. |

## Sketches

| Project Code | - | Discipline Code | - | Document Type| - | Sequential Number |
| -------------|---|-----------------|---|--------------|---|-------------------|
| NHR | - | AR | - | SK | - | 001 |

Sample Sketch number: NHR-AR-SK-001

## <a id="RLSGenericNumbering"></a> Room Layout Sheets - Generics

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type| - | Category / Package | - | Sequential Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| NHR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | DWG | - | G0 | - | 001 |

Sample Generic Room Layout sheet number: XXXX-BVN-AR-K-DWG-G0-001 :

## Room Layout Sheets - Specifics

| Project Code | - | Organization Code | - | Discipline Code | - | Zone / Building | - | Document Type| - | Category / Package | - | Room Number |
| -----------------|---------------|---|---|---|---|---|---|---|---|---|---|---|---|
| NHR | - | BVN | - | AR | - | [refer here](#ZoneIdentifier) | - | DWG | - | G1 | - | as per dRofus |

## User Group related drawings

| Discipline Code | - | Zone / Building | - | Document Type| - | User group | - | Level | - | Number |
| ----------------|---|---------------|---|-----------------|---|------------|---|-------|---|--------|
| AR | - | [refer here](#ZoneIdentifier) | - | SK | - | UG | - | 01 | - | 000 |

Sample number : AR-SK-K-UG-01-000

## Revisions

File names show the revisions right behind the document number in square brackets to allow for [supersede candidate](https://protect-eu.mimecast.com/s/zM1FB7zDRiZ) function to work in Aconex.
NHR-BVN-AR-K-DWG-A1-XX-01[01] - Document Name.pdf

Revisions are alphanumeric up until a document gets issued for construction. After that the revision changes to numerics.

Drawings are only clouded once they have been issued for construction.

## Titleblocks - Room Layout sheets

These titleblocks come in A2 and A3 sizes and have a sign off bar for SD and one for DD incorporated. Both title blocks have properties adjusting the sign off bar as follows:

| Property | use |
| SignOff_HealthPlanningConsultant | Contains the name of the health planning consultant to be shown in the sign off bar. |
| SignOff_LHD Name | Contains the name of the Local Health District to be shown in the sign off bar. |
| Sign_Off_ProjectManager | Contains the name of the Project Manager to be shown in the sign off bar. |

Families used:

* Titleblock_C_SHEET_A3_ANN_NHR
* Titleblock_C_SHEET_A2_ANN_NHR
* Titleblock_Landscape_Vertical_A1_ANN_NHR
* Titleblock_Landscape_Vertical_B1_ANN_NHR

Note: These families use catalogue files to handle the different options available.

Type naming:

| Project Prefix | Building | Sheet Size | Description | Note |
|----------------|----------|------------|-------------|------|
| NHR | K | B1 | no privilege no sign off| privilege: displays "CONFIDENTIAL & COMMERCIAL-IN-CONFIDENCE", Sign Off shows a sign off bar for user group consultation. |

Sample: NHR - Z1 and Z2 - B1 no privilege DD sign off:  Nepean Hospital, Buildings Z1 (Cancer Care) and Z2 (Demountable), B1 sheet size, no privileges shown, no sign off bar shown.

# Site set-out

The survey reference point chosen for the Nepean Hospital redevelopment works is SSM14758  as per survey cover sheet 'Nepean Hospital - Detail Survey', reference number 118117502, rev 3, dated 24/11/2016.
This survey point is located at (M.G.A) : North 6262211.157, East 288023.511 , R.L. 51.585 (A.H.D.) on Parker St, Nepean.

![six Maps]({{ site.baseurl }}/assets/s1607004_inh/2017-07-26 18_15_56-SIX Maps.png){:class="img-responsive"}{: height="1200px" width="1800px"}

# Refurbishment Works

The early refurbishment works comprises of

* Existing Cancer Centre building refurbishment
* Adding a demountable to the North of the existing Cancer Centre

## Refurbishment Works - Site set-out

With the exception of the demountable added to the existing Cancer Centre all refurbishment works are located within the envelope of existing buildings and therefore do not require site set out.

The new demountable for the Cancer centre will be set out in relative to the existing Cancer Care building.

Consultants are to link the NHR-BVN-AR-Z1-RVT-0001 - Cancer Services.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* NHR-BVN-AR-0-RVT-0001 - New Acute Services Building - Site.rvt
* NHR-BVN-AR-Z2-RVT-0001 - Demountable.rvt

# New Acute Services Building

The new build comprises of a new hospital entry point linking the varies existing buildings on level (x) and a new bed tower.

## New Build - Site set-out

The new building is set out as per the graphic below:

(TODO: add set out graphic)

Consultants are to link the NHR-BVN-AR-K-RVT-0001 - New Acute Services Building.rvt Revit file using the 'Auto - Origin to Origin' option and acquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

* NHR-BVN-AR-K-RVT-0002 - New Acute Services Building - Main Entry.rvt
* NHR-BVN-AR-Z2-RVT-0001 - Demountable.rvt

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

Another issue is the way Health Infrastructure has set up the actual function structure of their database. Whilst the structure itself is 3 levels deep, the actual room function number only reflects the first two of those levels and Functional Group has been excluded:

![drofus_FunctionStructure]({{ site.baseurl }}/assets/s160x00x_common/dRofusFunctionStructure.svg){:class="img-responsive"}{: height="259px" width="482px"}

Unfortunately this default Health infrastructure seetting can not be changed by BVN. We can, however inforce the use of two digits to identify a level.

### dRofus - New Build workflow

Nepean and Randwick SD phase (new builds -> generic rooms only)

* BVN will take control and therefore responsibility of all items (including services). 
* Services consultants however will be asked to export Services to Excel and furnish BVN with the completed Excel document which we will import back into dRofus. As per the below diagram. Again blue is BVN and orange the consultants.

![drofus_workflow_new]({{ site.baseurl }}/assets/s160x00x_common/Drofus_NewBuild_Works.svg){:class="img-responsive"}{: height="217px" width="925px"}

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
| Room reference | | the number of the room the door belongs to.  |
| Door Instance By Room | | instance counter of doors placed in a room. e.g. D01 |
| Door Finish External | 3210bfb2-7735-4be7-bdbc-3f27cf6fe618 | Finish of door opening to side. |
| Door Finish Internal | c72ee8d5-5681-43f5-9bb8-dddd9773f26b | Finish of door opening from side. |

### Defining door paint scope in refurb

The wall finishes drawings contain a filter which will colour all doors red which have the ''Door Finish External'' property set. Or in other words: all doors coloured red are within the paint scope of the refurb project. 

Default paint colour of doors can be defined through a cover note: All doors shown red are to be painted with PT-XXX unless noted otherwise.

If a door has the same finish applied to both sides use the ''Door Finish External'' property to show (tag) that finish only. In any other case use the ''Door Finish External'' and ''Door Finish Internal'' property and tag as required. 

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

## Door Tag

## Door Tags

| Tag Family | Tag Type | Usage | Graphics |
|-----------|-----|----|----|
| Door Tag_ANN.rfa | Internal | For internal doors. Shows door room reference and door instance number. | ![DoorTagInternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Doors_Internal.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Tag_ANN.rfa | External | For external doors, usually covered in a separate schedule. Shows door room reference and door instance number. | ![DoorTagExternal]({{ site.baseurl }}/assets/s160x00x_common/Tag_Doors_External.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Finish External Tag_ANN | Colour | Is used to display the external door finish code. | ![DoorTagFinish]({{ site.baseurl }}/assets/s160x00x_common/Tag_Door Finish.svg){:class="img-responsive"}{: height="200px" width="200px"} |
| Door Finish Internal Tag_ANN | Colour | Is used to display the internal door finish code. | ![DoorTagFinish]({{ site.baseurl }}/assets/s160x00x_common/Tag_Door Finish.svg){:class="img-responsive"}{: height="200px" width="200px"} |

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
