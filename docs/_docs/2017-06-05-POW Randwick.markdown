---
title:  "Revit setup of POW Hospital"
date:   2017-05-31 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "Everything relating to Revit on POW"
modified:
layout: "confidential"
---

# Existing Emergency Department Transitional Works

## Site set-out

The survey reference point choosen for the POW ED refurbishments works is SSM51804  as per survey cover sheet 'Randwick', refernce number 43147DT, project number 30744, dated 15/06/15.
This survey point is located at (M.G.A) : North 6245643.193, East 337291.821 , R.L. 65.572 (A.H.D.) on High Street, Randwick.

![six Maps]({{ site.baseurl }}/assets/s1606008_rcr/2017-06-05 11_05_48-SIX Maps.png){:class="img-responsive"}{: height="1200px" width="1800px"}

Note: The Site survey point in s1606008-AR-RCR-ED Transitional Works.rvt Revit file is not pinned! Revit moves the point to  North 6245643.193, East 337291.8231  when attempting to pin it...

## Revit File linking

Consultants are to link the s1606008-AR-RCR-ED Transitional Works.rvt Revit file using the 'Auto - Origin to Origin' option and aquire shared coordinates from it. This will enable linking of the following files via 'Auto - By Shared Coordinates' option.

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

