---
title:  "Revit setup of POW Hospital_old"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Everything relating to Revit on POW"
modified:
layout: "sample"
categories: Revit
---

# Document Numbering - Proposed

## Document Number Overview

| PROJECT NAME | - | ORGANISATION | - | DOC / DRAWING TYPE | - | DISCIPLINE | - | AREA | - | ELEMENTS / PACKAGE | DRAWING / INFORMATION SERIES | - | LEVEL* | ZONE | SEQUENCE   | - | REVISION |
|+------------+|+-+|+------------+|---|--------------------|---|------------|---|------|--------------------|------------------------------|---|--------|------|------------|---|----------|
| RCR | - | BVN | - | [doc type](#Drawing_DocType) | - | ARC | - | [Area List](#Drawing_AreaList) | - | [Element List](#Drawing_Elements) | [Series List](#Drawing_Series) | - | [Level List](#Drawing_Level) | [Zone List](#Drawing_Zone) | [Sequence List](#Drawing_Sequence) | - | [Revision](#Drawing_Revision) |


## <a id="ZoneIdentifier"></a> ZONE / BUILDING

The documentation packages are set up by building. Below is a map showing the existing campus with building number.

![KeyMap]({{ site.baseurl }}/assets/s1606008_rcr/KeyPlan.svg){:class="img-responsive"}{: height="546px" width="309px"}

## <a id="Drawing_AreaList"></a> Area List

List of buildings:

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

### Visualization Options 

non collapsible tree
https://bl.ocks.org/mbostock/4063550

collapsible tree
http://jsfiddle.net/Nivaldo/CbGh2/

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
