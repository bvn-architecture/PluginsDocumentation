---
title:  "Project Octopussy"
date:   2017-06-18 19:00:00 +1100
permalink: #/docs/2017-04-28-PushIt
excerpt: "A flexible power and data distribution"
modified:
layout: "sample"
categories: Hardware
---

# Power and Data distribution

In an open plan office environment power and data distribution usually is done (hidden) in the ceiling space which offers the flexibility required to deal with different floor plate layouts over time.

## No ceiling space...now what?

In situations where the suspended ceiling has been omitted, the flexibility in terms of workstation layouts is reduced. Usually a number of fixed ceiling drop points with in desk cabling limit the layout options available.

## Project Octopussy

This proposed solution comprises of:

* Central spine: Stackable ceiling based power and data access points
* Support net (webbing?) to guide umbilical cord close to end user
* Arms which can be used for
    * Lighting
    * Sensor pods
    * TV mounts
* Umbilical chord providing power and data to a workstation

![SampleRender]({{ site.baseurl }}/assets/Octopussy/Octopussy.rvt_2017-Jun-18_05-01-51AM-000_3D_View_1.png){:class="img-responsive"}{: height="700px" width="900px"}

### Central Spine

Depending on how many users are in the area of an octupus, the number of data and power points provided can be varied by:

* Adding more levels to the central spine. Each face of the central spine provides 1 x data and 1 x power to a single user. The single power outlet is used to supply up to x4 outlets at the users desk.

![Stack]({{ site.baseurl }}/assets/Octopussy/Octopussy_CentralSpineStack.svg){:class="img-responsive"}{: height="500px" width="900px"}

* Changing the basic central spine shape from a triangle to a quad ...

| Triangle | Square |
|----|-----|
| ![Octo_Tri]({{ site.baseurl }}/assets/Octopussy/Octopussy_TRI_SINGLE.svg){:class="img-responsive"}{: height="300px" width="500px"} | ![Octo_Quad]({{ site.baseurl }}/assets/Octopussy/OCTOPUSSY_QUAD_SINGLE.svg){:class="img-responsive"}{: height="300px" width="500px"} |

### Arms

The arms of the Octopus could be used for:

| Lighting | Sensors | Monitor |
|---------|-------|--------|
| ![Lighting]({{ site.baseurl }}/assets/Octopussy/Octupussy_Quad_Lighting.svg){:class="img-responsive"}{: height="300px" width="500px"} | ![SensorPods]({{ site.baseurl }}/assets/Octopussy/Octupussy_Quad_SensorPods.svg){:class="img-responsive"}{: height="300px" width="500px"} | ![TV]({{ site.baseurl }}/assets/Octopussy/FLATPNLCEIL.jpg){:class="img-responsive"}{: height="200px" width="500px"} |

### Webbing

The webbing between the arms is used to guide the umbilical cord from the central spine to a location above the users desk where it drops straight down. Fixing of the chord to the webbing could be via simple hooks or even cable ties.

### Umbilical Chord

The chord comprises of a single power and a single data cable of a maximum length yet to be determined. The plug connection at the central spine will need to be able to withstand accidental pulling. Both cables can be hold together via simple tubing with surplus cabling either be stored in the webbing above or at the desk connection.

![Cabling_organize]({{ site.baseurl }}/assets/Octopussy/spirala-szara-organizer_3947.jpg){:class="img-responsive"}{: height="300px" width="500px"}

An alternative solution could be to use the arms as a guide rail for these:

![RoboReel]({{ site.baseurl }}/assets/Octopussy/RoboReel.jpg){:class="img-responsive"}{: height="500px" width="500px"}

### Layout Options

Octopi can vary in size and shape to fit a given floor plate layout as shown below:

![Layout]({{ site.baseurl }}/assets/Octopussy/Octopussy_Quad_Cluster.svg){:class="img-responsive"}{: height="300px" width="500px"} 

### Wiring

There are two main options to wire the Octopi to a comms location:

| Node Based | Centralised on Floor plate |
|-----------|-------------------------|
| ![wiring_NodeBased]({{ site.baseurl }}/assets/Octopussy/Wiring_NodeBased.svg){:class="img-responsive"}{: height="300px" width="500px"} | ![wiring_centralised]({{ site.baseurl }}/assets/Octopussy/Wiring_Centralised.svg){:class="img-responsive"}{: height="450px" width="650px"} |
| Nodes to base are single fibre optics (green) with distribution to user level via copper (grey) at node | Nodes to base are copper cable (grey) with distribution to user level at central location (Nodes are just pass through points) |
| Easy to add more users at a node at a later point in time | To allow for maximum flexibility nodes will need to incorporate future user numbers at day one (maybe a factor of 1.5 or 1.75 connections per user) |

### Safe User Access

Ideally the central spine is mounted with the underside at 2700 to match the lowest point of the currently installed duct work. This would allow for a fairly short vertical lift movement of approx 500mm - 700mm to get the plugs within the reach of the end user without requiring a ladder. This in turn assumes that there is sufficient cable slack at the top of the central spine. Maybe something like the below could be implemented.

![CableDragChain]({{ site.baseurl }}/assets/Octopussy/WireChainProtection.jpg){:class="img-responsive"}{: height="300px" width="500px"} 

Having all data cables in one cable drag chain might not work due to the amount of cables. One possible option is to have one chain per side of central spine ( 4 sides) which would reduce the number of cable down to approx 11 per chain.
