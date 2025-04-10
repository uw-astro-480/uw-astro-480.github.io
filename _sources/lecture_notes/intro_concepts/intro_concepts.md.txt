# Introductory concepts

This section covers a series of introductory concepts that are important for the course and for observational astronomy in general. It is not intended to be thoroughly exhaustive, but rather to provide a basic understanding of the topics that will be covered in more detail later in the course. Further reading is provided at the end of the section and as links throughout the text.

## Coordinate systems

Anybody who has spent some time looking at the sky in a dark place at night has noticed that the stars, planets, and other astronomical objects seem to be arranged on the "surface" of a sphere that rotates around a point. If we take a long-exposure photograph centred around that "celestial pole" we will see that the stars move in arcs.

[![North star traces](https://i0.wp.com/digital-photography-school.com/wp-content/uploads/2010/07/WindowsLiveWriterHowToFindTheNorthStarAndWhyYoudWantTo_E333070317-194557-6308_070317-203720-6344_3.jpg?w=600&h=1260&ssl=1){align=center}](https://digital-photography-school.com/how-to-find-the-north-star-and-why-youd-want-to/)

Of course, we understand why this is happening: the sky rotates as a result of the rotation of the Earth, with the Earth's axis of rotation —when projected on the sky— defining the point around which the celestial sphere rotates. And the stars are not all really on the same plane, but rather at different distances from us. But those distances are so vast that perspective renders them all on a what appears to be a single surface.

That said, it is convenient for many purposes to think of the sky as a sphere that rotates around a given axis, and the celestial objects being placed on the surface of that sphere.

### Definitions

Let's start with some basic definitions. Imagine a spherical surface with unit radius. We draw a line that passes through the centre of the sphere, $C$ and intersects the surface at two points, $P$ and $P'$ which we will call the _poles_. Next we define a plane that passes through the centre of the sphere and is perpendicular to the line that connects the two poles. This plane intersects the surface of the sphere at a circle which we will call the _fundamental circle_.

Now let's define a point $A$ on the surface of the sphere. We can draw a circle that passes through both poles and $A$ (note that this circle is centred on $C$). This circle intersects the fundamental circle at a point $B$.

```{figure} ./images/defs1.png
:width: 50%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Let's now draw a circle that is parallel to the fundamental circle and intersects the surface of the sphere at $A$. Finally, let's define another point $D$ on the fundamental circle.

```{figure} ./images/defs2.png
:width: 100%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

The point $A$ can now be defined using two angles: the angle $\angle ACB$ and the angle $\angle DCB$. We can also define and important concepts: a _great circle_ is one defined by a plane that passes through the centre of the sphere. All great circles have equal length and are the largest possible circle than can be drawn on the sphere. A _small circle_ is a circle defined on the sphere that is not a great circle. In our example above the circles $PABP'$ and $PDP'$ are great circles, as well as the fundamental circle. The circle that is parallel to the fundamental circle and passes through $A$ is a small circle. The shortest distance between two points on the surface of a sphere is always along a great circle, a concept that is sometimes counter-intuitive. The length of a small circle that is parallel to the fundamental circle decreases with the cosine of the angle (e.g., $\cos(ACB)$).

### Spherical trigonometry

_Spherical trigonometry_ is the branch of mathematics that studies with the relationships between angles and distances on the surface of a sphere. While many concepts may seem similar to planar (or Euclidean) trigonometry, there are important differences. Let's start by defining a triangle from the intersection of three great circles:

```{figure} ./images/sph-trig.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Angles on a spherical triangle are denoted with capital latin letters. In our case $A$, $B$, and $C$ are the angles at the vertices of the triangle. $A$ (and $B$ and $C$) is the angle between the two planes that intersect the sphere at vertex $A$. Angles are measured in radians

The sides of the triangle are also measured in radians and measured by the angle that it subtends at the centre. The sides are denoted with lower case letters, so $a$ is the side opposite to angle $A$, $b$ is the side opposite to angle $B$, and $c$ is the side opposite to angle $C$.

By definition a spherical triangle angle is less than $\pi$ radians so

$$
\pi < A+ B+ C < 3\pi
$$

while the sides are less than $\pi$ radians, so

$$
0 < a+ b+ c < 2\pi
$$

The most important rule of spherical trigonometry is the _law of cosines_. A proof of this law (and other relationships that we will see below) can be found in many textbooks on spherical astronomy, for example in Chapter 1 of Smart's Textbook on Spherical Astronomy. The law of cosines applies to each angle so we can write three expressions such as:

$$
\begin{eqnarray*}
\cos a &=& \cos b \cos c + \sin b \sin c \cos A \\
\cos b &=& \cos a \cos c + \sin a \sin c \cos B \\
\cos c &=& \cos a \cos b + \sin a \sin b \cos C
\end{eqnarray*}
$$

From the law of cosines we can derive the _law of sines_:

$$
\frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c}
$$

These two expressions are the base of spherical trigonometry can be used to derive any additional relationships. For right spherical triangles (triangles in which one angle is formed by the intersection of two perpendicular planes) we can also make use of [Napier's rules](https://en.wikipedia.org/wiki/Spherical_trigonometry#Napier's_rules_for_right_spherical_triangles) which we won't cover here but that are essential for solving problems in astronomical spherical trigonometry, where many triangles are right triangles.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Spherical_trigonometry_Napier_quadrantal_01.svg/2880px-Spherical_trigonometry_Napier_quadrantal_01.svg.png
:width: 60%
:align: center
:class: white-background
:target: https://en.wikipedia.org/wiki/Spherical_trigonometry#Napier's_rules_for_right_spherical_triangles
```

:::{important}
Spherical trigonometry applies only to spherical triangles, that is, triangles defined by the intersection of three **great circles**. Triangles formed by the intersection of small circles do not follow these rules.
:::

#### Separations on the sphere

A typical problem in spherical trigonometry consists on measuring the distance (_separation_) between two points on the surface of a sphere. In particular, consider the distance $\beta$ in the following case:

```{figure} ./images/sph-sep.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

As we will see, $A$ and $B$ are defined using reference points that are natural in spherical coordinate systems. While the sides labelled with $\alpha$ and $\beta$ make reference to an equatorial coordinate system, this is a general case and the solution is generally valid. We'll leave the proof of this experiment to the reader (hint: consider the triangle defined by the ${\rm NCP}-B$ and $AB$ great circles and the fundamental plane, and use the Napier's rules).

$$
\begin{eqnarray*}
\beta^2 &=& \Delta\delta^2 + \cos^2 \bar\delta \Delta\alpha^2 \\
\bar\delta &=& \dfrac{\delta_A + \delta_B}{2} \\
\end{eqnarray*}
$$

### Horizontal coordinates

The simplest type of coordinates is called horizontal (also altitude-azimuth or alt-az). Imagine that you are standing on the surface of the Earth in a place where you can all the way to the horizon. The point just above your head is called the _zenith_. The one just below your feet is called the _nadir_. These two points defined the poles of the horizontal coordinate system while the horizon is the fundamental circle. If we have a point $S$ on the sky, we can define its position with two coordinates: _altitude_ ($h$) and _azimuth_ ($A$). Altitude is the simplest one and is just the angle, perpendicular to the horizon, between the horizon and the point. For the azimuth we need to define an arbitrary reference point on the horizon. We chose the North cardinal point (the direction of the North pole) and measure the angle from there, going clockwise (azimuth angles increase from North towards East).

```{figure} ./images/altaz.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

:::{warning}
There is no strong convention on how to define the azimuth angle. Some people define it as the angle from the South cardinal point, going clockwise. When dealing with alt-az coordinates always make sure that you know how the azimuth angle is defined. Similarly, the letters $h$ and $A$ are not universally used to denote altitude and azimuth, respectively.
:::

A critical thing to realise is that the horizontal coordinates of an object change during the night as the sky rotates. Because of that we need an additional datum, the time of observation, to fully define the position of such object. The coordinates of the object will also depend on the location of the observer on the Earth. Imagine an observer on the equator observing a star that is at the zenith. That observer will measure an altitude of 90 degrees. Now imagine an observer at the North (or South) pole observing the same star at the same time: they will measure an altitude of 0 degrees!

Before we move on, we can introduce a few additional concepts based on the horizontal coordinate system. The _zenith distance_ ($z$) is the distance between the point we are trying to measure and the zenith. _Twilights_ are defined as the moment in which the Sun reaches a certain point below the horizon. The most common definitions are _civil twilight_ (when the Sun is 6 degrees below the horizon), _nautical twilight_ (12 degrees below the horizon), and _astronomical twilight_ (18 degrees below the horizon).

### Equatorial coordinates

While horizontal coordinates are easy to understand but are not practical to define the position of celestial object in a way that is independent of the observer's location and time. For that we need to define a coordinate system that is fixed with respect to the stars. The most common system that meets this requirement is the _equatorial coordinate system_.

As we did before, let's imagine a celestial sphere, centred on the Earth, but in this case the poles will be the North and South celestial poles (NCP, SCP), that is, the points on the celestial sphere that are aligned with the Earth's axis of rotation. The fundamental circle in this system is called the _celestial equator_. For a given point $S$ on the sphere we define its position with two angles: _declination_ (Dec or $\delta$) and _right ascension_ (RA or $\alpha$). The declination is measured from the celestial equator following the great circle that passes through $S$ and the poles (declination is positive towards the NCP). As with horizontal coordinates we now need to define a reference point for the right ascension. We chose the point on the celestial equator on which the Sun is at the vernal (Spring) equinox, which we call the _vernal point_. RA increases along the celestial equator clockwise when looking from the NCP. The units of RA are usually hours, minutes, and seconds (1 hour = 15 degrees) and declination is always measured in degrees.

```{figure} ./images/eq1.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Since the sky rotates around the polar axis, the declination of an object never changes, and as the vernal point also rotates, the right ascension of the object is also constant. The equatorial coordinates of an object are fixed regardless of the observer's location or time of observation (as we'll see, things are a bit more complicated, but for now we can assume that this is true).

:::{note}
Technically the equatorial system that we have defined is called _Geocentric Celestial Reference System_ since the centre of the coordinate system is assumed to be the centre of mass of the Earth. As we'll see later, other equatorial systems can be defined with centres at other points, such as the barycentre of the Solar System.
:::

We can put the horizontal and equatorial coordinate systems together in a single diagram to see how they relate to each other. Here the celestial equator and horizon form an angle equal to the latitude of the observer's location on the Earth. The angle $ZS$ is the zenith distance and the angle $PS$ along the great circle perpendicular to the celestial equator is the _hour angle_. The circle that passes through the zenith and the poles is called the _local meridian_.

```{figure} ./images/eq-altaz.png
:width: 60%
:align: center
:name: fig-eq-altaz
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

#### Hour angle

We will more properly introduce sidereal time later, but for now let's just define _local sidereal time_ (LST) as the angle between the local meridian and the vernal point. LST is measured in hours and is zero when the vernal point crosses the local meridian.

```{figure} ./images/hour-angle.png
:width: 60%
:align: center
:class: white-background
:target: http://math_research.uct.ac.za/~siphelo/admin/interferometry/3_Positional_Astronomy/3_2_Hour_Angle.html
```

We then define the _hour angle_ ($H$) as the angle between the local meridian and the object. From the diagram above it's clear that the H and the LST are related by $H={\rm LST}-\alpha$. The hour angle is measured in hours and increases towards the West. Since an object on the sky will move from East to West, a negative hour angle indicates that the object is rising and a positive hour angle indicates that the object is setting. The hour angle is zero when the object crosses the local meridian, at which point the local sidereal time is the same as the right ascension of the object.

### Other coordinate systems

The horizontal and equatorial coordinate systems are the most commonly used in astronomy, but there are many other coordinate systems that can be defined. Here we quickly introduce a few of them.

#### Ecliptic coordinates

Ecliptic coordinates are defined using the plane of the ecliptic (the average plane of the Earth's orbit around the Sun) as the fundamental circle. The ecliptic longitude $\lambda$ is measured along the ecliptic from the vernal point, and the ecliptic latitude $\beta$ is measured perpendicular to the ecliptic plane. The ecliptic coordinates are useful for defining the position of objects in the Solar System, such as planets and comets.

```{figure} ./images/ecliptic.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

#### Galactic coordinates

Galactic coordinates provide a more natural way to specify the position of objects in the Milky Way. The fundamental circle is defined from the plane of the Milky Way (this is not trivial and a convention is used) with the Galactic Poles as the axis of the system. The Galactic latitude $b$ is measured perpendicular to this plane and indicates the angle of the object with respect to the disk of the Milky Way (and so, most stars have relatively small Galactic latitudes). The Galactic longitude $l$ is measured with respect to the direction of the Galactic centre.

```{figure} ./images/galactic.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

### Precession of the equinoxes

The gravitational pull of the Sun and the Moon on the Earth causes it axis of rotation to wobble over time. The polar axis describes a circle on the celestial sphere with a period of about 26,000 years. This phenomenon is called _precession of the equinoxes_. The effect of the precession in the equatorial coordinate system is that as polar axis changes so does the celestial equator and the location of the vernal point (which is defined as one of the point in which the ecliptic intersects the celestial equator). Although the change due to precession may seem small, it is in the order of $\sim 50$ arcseconds per year, which is significant for many astronomical applications. This means that the equatorial coordinates of an object will change over time as the vernal point changes. To account for this effect, astronomers refer to the equatorial coordinates of an object at a given epoch. Most coordinates these days are referred to the position of the vernal point in the Julian date 2000 (usually referred as J2000) but older catalogues may use B1950 ([Besselian epoch](<https://en.wikipedia.org/wiki/Equinox_(celestial_coordinates)#Besselian_equinoxes_and_epochs>) 1950.0).

```{figure} ./images/precession.png
:width: 60%
:align: center
_Credit:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Additional effects such as [nutation](https://en.wikipedia.org/wiki/Nutation) also affect the alignment of the celestial pole, but usually these effects are small enough that they can be ignored for most applications.

The inconvenience of the shifting of the vernal equinox has lead to the establishment of the _International Celestial Reference System_ (ICRS) and other systems that are defined with respect to very stable reference points (usually distant radio sources). The ICRS is centred on the barycentre of the Solar System while the Geocentric Celestial Reference System (GCRS) is centred on the centre of mass of the Earth and is useful for calculating the position of near-Earth objects.

The ICRS is defined so that its orientation matches the direction of the vernal point in J2000 within approximately 23 milliarcseconds. Because of that, for most applications one can ignore differences between J200 and ICRS. These differences are important, however, when carrying out transformations to other coordinate systems.

### Coordinate transformations

We often need to transform from one coordinate system to another. Coordinate transformations can be derived using the basic rules of spherical trigonometry, and transformations between many common coordinate systems can be found in textbooks and online. By far the most common coordinate transformation is between equatorial and horizontal coordinates, which is especially useful when planning observations to determine the altitude of an object at the site of observation during the night. Ig we refer to the [figure](#fig-eq-altaz) relating equatorial and horizontal coordinates, we can write the following equations:

$$
\begin{eqnarray*}
\sin h &=& \sin \delta \sin \phi + \cos \delta \cos \phi \cos {\rm HA} \\
\tan A &=& \dfrac{\sin {\rm HA}}{\cos {\rm HA} \sin \phi - \tan \delta \cos \phi} \\
\end{eqnarray*}
$$

where ${\rm HA} = {\rm LST}-\alpha$, $h$ is the altitude, $A$ is the azimuth, $\delta$ is the declination, and $\phi$ is the latitude of the observer. There is an implicit ambiguity in the azimuth angle, which can be resolved by using the two-argument arctangent function, ${\rm atan2}(y,x)$. In this form $A=-{\rm atan2}(y, x)$ with

$$
\begin{eqnarray*}
y &=& \sin {\rm HA}\cos\delta \\
x &=& -\sin\phi \cos\delta \cos {\rm HA} - \cos\phi \sin\delta \\
\end{eqnarray*}
$$

#### Using `astropy` to convert coordinates

Many astronomical libraries allow to convert between different coordinate systems but [astropy](https://www.astropy.org/) has a especially comprehensive set for tool for this purpose and automatically takes care of all the steps required to convert between many coordinate systems. The documentation for the [astropy.coordinates](https://docs.astropy.org/en/stable/coordinates/index.html) module describes how to define and transform coordinates.

Here we will just show the usual case of transforming from equatorial (ICRS in this case) to horizontal coordinates. Let's imagine that we want to determine the altitude of an object with $\alpha=100^\circ$ and $\delta=10^\circ\,30'$ at the current time at Apache Point Observatory. Here's the snipped to do that:

```{code-block} python
:lineno-start: 1

from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.time import Time

now = Time.now()
apo = EarthLocation.of_site('Apache Point Observatory')

coords = SkyCoord(ra=100, dec=10.5, unit='deg', frame='icrs')
altaz_frame = AltAz(obstime=now, location=apo)
altaz = coords.transform_to(altaz_frame)

print(f"Altitude: {altaz.alt:.2f}")
print(f"Azimuth: {altaz.az:.2f}")
```

In line 3 with define the current time. `astropy` defaults to using the UTC scale, but for the current time (and for most applications, see below) we don't need to worry too much about that. In line 4 we define the location of the observatory. In this case we are using the internal list of locations that `astropy` knows, but we could also define it from latitude, longitude, and altitude. Next we define the coordinates of our target. Note that we need to specify the units and the frame. Here we use the ICRS coordinate system, which is the default one for `SkyCoord`. As we have discussed, the difference between ICRS and J2000 is negligible and `astropy` will take care of the conversion. This is fine of far away objects. However, for near-Earth objects like the Moon or planets things may be different!

In line 8 we define an alt-azimuthal frame using the time and location of the observer. This frame is not associated with a specific coordinate and just defined the orientation of the alt-az frame. In the following line is we actually transform the coordinates. Here `altaz` will be a new `SkyCoord` object but this time in the `AltAz` frame. Finally, we print the altitude and azimuth of the object.

:::{admonition} Exercise
:class: tip

As an exercise, try to convert the same coordinates using the equations that we derived above. You will need the latitude of Apache Point Observatory, which is $32.78^\circ$ North and the LST of the current time (hint: you can use the [sidereal_time](https://docs.astropy.org/en/stable/time/index.html#sidereal-time-and-earth-rotation-angle) method of the `Time`). Do you get the same result? What is the origin of the difference?
:::

## Time

Coming soon.

## Measuring light

Coming soon.

## Optics and telescopes

Coming soon.

## Further reading

- Birney, D. S., Gonzalez, R. A., & Oesper, D. (2006). Observational Astronomy (2nd ed.)
- Smart, W. M. (1977). Textbook on Spherical Astronomy (6th ed.)
- [International Celestial Reference System](https://aa.usno.navy.mil/faq/ICRS_doc)
