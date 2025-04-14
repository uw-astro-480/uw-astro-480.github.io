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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Let's now draw a circle that is parallel to the fundamental circle and intersects the surface of the sphere at $A$. Finally, let's define another point $D$ on the fundamental circle.

```{figure} ./images/defs2.png
:width: 100%
:align: center
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

The point $A$ can now be defined using two angles: the angle $\angle ACB$ and the angle $\angle DCB$. We can also define and important concepts: a _great circle_ is one defined by a plane that passes through the centre of the sphere. All great circles have equal length and are the largest possible circle than can be drawn on the sphere. A _small circle_ is a circle defined on the sphere that is not a great circle. In our example above the circles $PABP'$ and $PDP'$ are great circles, as well as the fundamental circle. The circle that is parallel to the fundamental circle and passes through $A$ is a small circle. The shortest distance between two points on the surface of a sphere is always along a great circle, a concept that is sometimes counter-intuitive. The length of a small circle that is parallel to the fundamental circle decreases with the cosine of the angle (e.g., $\cos(ACB)$).

### Spherical trigonometry

_Spherical trigonometry_ is the branch of mathematics that studies with the relationships between angles and distances on the surface of a sphere. While many concepts may seem similar to planar (or Euclidean) trigonometry, there are important differences. Let's start by defining a triangle from the intersection of three great circles:

```{figure} ./images/sph-trig.png
:width: 60%
:align: center
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

#### Hour angle

We will more properly introduce sidereal time [later](#sidereal-time), but for now let's just define _local sidereal time_ (LST) as the angle between the local meridian and the vernal point. LST is measured in hours and is zero when the vernal point crosses the local meridian.

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
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

#### Galactic coordinates

Galactic coordinates provide a more natural way to specify the position of objects in the Milky Way. The fundamental circle is defined from the plane of the Milky Way (this is not trivial and a convention is used) with the Galactic Poles as the axis of the system. The Galactic latitude $b$ is measured perpendicular to this plane and indicates the angle of the object with respect to the disk of the Milky Way (and so, most stars have relatively small Galactic latitudes). The Galactic longitude $l$ is measured with respect to the direction of the Galactic centre.

```{figure} ./images/galactic.png
:width: 60%
:align: center
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

### Precession of the equinoxes

The gravitational pull of the Sun and the Moon on the Earth causes it axis of rotation to wobble over time. The polar axis describes a circle on the celestial sphere with a period of about 26,000 years. This phenomenon is called _precession of the equinoxes_. The effect of the precession in the equatorial coordinate system is that as polar axis changes so does the celestial equator and the location of the vernal point (which is defined as one of the point in which the ecliptic intersects the celestial equator). Although the change due to precession may seem small, it is in the order of $\sim 50$ arcseconds per year, which is significant for many astronomical applications. This means that the equatorial coordinates of an object will change over time as the vernal point changes. To account for this effect, astronomers refer to the equatorial coordinates of an object at a given epoch. Most coordinates these days are referred to the position of the vernal point in the Julian date 2000 (usually referred as J2000) but older catalogues may use B1950 ([Besselian epoch](<https://en.wikipedia.org/wiki/Equinox_(celestial_coordinates)#Besselian_equinoxes_and_epochs>) 1950.0).

```{figure} ./images/precession.png
:width: 60%
:align: center
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

Additional effects such as [nutation](https://en.wikipedia.org/wiki/Nutation) also affect the alignment of the celestial pole, but usually these effects are small enough that they can be ignored for most applications.

The inconvenience of the shifting of the vernal equinox has lead to the establishment of the _International Celestial Reference System_ (ICRS) and other systems that are defined with respect to very stable reference points (usually distant radio sources). The ICRS is centred on the barycentre of the Solar System while the Geocentric Celestial Reference System (GCRS) is centred on the centre of mass of the Earth and is useful for calculating the position of near-Earth objects.

The ICRS is defined so that its orientation matches the direction of the vernal point in J2000 within approximately 23 milliarcseconds. Because of that, for most applications one can ignore differences between J200 and ICRS. These differences are important, however, when carrying out transformations to other coordinate systems.

### Coordinate transformations

We often need to transform from one coordinate system to another. Coordinate transformations can be derived using the basic rules of spherical trigonometry, and transformations between many common coordinate systems can be found in textbooks and online. By far the most common coordinate transformation is between equatorial and horizontal coordinates, which is especially useful when planning observations to determine the altitude of an object at the site of observation during the night. If we refer to the [figure](#fig-eq-altaz) relating equatorial and horizontal coordinates, we can write the following equations:

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

As an exercise, try to convert the same coordinates using the equations that we derived above. You will need the latitude of Apache Point Observatory, which is $32.78^\circ$ North and the LST of the current time (hint: you can use the [sidereal_time](https://docs.astropy.org/en/stable/time/index.html#sidereal-time-and-earth-rotation-angle) method of the `Time` object). Do you get the same result? What is the origin of the difference?
:::

## Time

We move now to a closely related topic: the measurement of times and dates. During our discussion of coordinate systems we have already mentioned that the coordinates of an object, as seen from a location on Earth, depend on the time of observation, a concept that in the case of equatorial coordinates we encoded in the hour angle.

### Solar time

The first an most natural way to measure time is to look at the Sun, and as such many cultures have defined their calendars based on the position of the Sun in the sky. We can defined the _apparent solar day_ (or _true solar day_) as the time measured by the successive passes of the Sun over the local median (which can be measured, for example, by looking at the shadow cast by a stick or _gnomon_). By a convention that we owe to the Egyptians we divide the solar day into 24 equal parts, or _hours_, and into smaller time units.

The problem with the apparent solar day is that the Sun does not move at a perfectly constant speed across the sky over a full year. This is due to two facts: the ellipticity of the Earth's orbit and the tilt of the Earth's axis with respect to the plane of the ecliptic. The result is that the length of the solar day varies over the year: an apparent solar day in March is about 18 seconds short of 24 hours, while on in late December is longer by almost 30 seconds. To account for the variability in the true solar time we introduce the _mean solar day_, which moves at constant speed. Mean solar time can be defined as the time measured by a fictitious Sun that moves at constant speed along the celestial equator and coincides with the true Sun at the perigee and apogee.

The difference between the mean solar time and the apparent solar time is called the _equation of time_. The equation of time is a periodic function, which resets over the period of a year (i.e., the difference between true time and mean time does not accumulate past a year).

```{figure} ./images/equation-time.png
:width: 80%
:align: center
_Source:_ Observational Astronomy, Birney et al. (2nd ed.)
```

These days the mean solar time is defined based on the position of far away sources using very long baseline interferometry, and as such a mean solar day is 24.0000006 hours (based on the SI definition of a second).

The solar mean time needs to be measured with respect to a given location on Earth, which for historical reason is chosen to the the Greenwich meridian (and as such called the _Greenwich Mean Time_ or GMT, also often referred as _Universal Time_ or UT). The time at a given location is then defined as the difference between the local mean solar time and the GMT based on the latitude of the place

$$
{\rm local mean time} = {\rm GMT} - {\rm longitude}
$$

### Dynamical time

The mean solar time is not a perfect measure of time. The rotation of the Earth is not constant and is affected by many factors, such as the gravitational pull of the Moon and the Sun, the tides, and the motion of the Earth's crust. To account for these variations we need to define a new time scale, called _dynamical time_. Dynamical time has had multiple iterations over the years, from the original Ephemeris Time or ET to the Terrestrial Dynamical Time (TDT) or the current _Terrestrial Time_ (TT). In all cases the dynamical time unit is the SI second. Dynamical time definitions are complex but they are designed to be free of the variations that affect the mean solar time.

Starting in 1970 a new time, the _International Atomic Time_ (TAI) was introduced based on the combined measurements of over 450 atomic clocks distributed around the world. At the time of its inception TAI was defined to be (and remains) $\rm TAI=TT-32.184\,s$.

Universal Time (UT or GMT) differs from TT or TAI by a factor $\Delta T$ such that $UT=TT - \Delta T$. The value of $\Delta T$ cannot be predicted over a long period of time as it depends on precise measurements of the Earth's Orientation Parameter, which are released by the [International Earth Rotation and Reference Systems Service](https://www.iers.org/IERS/EN/Home/home_node.html) (in reality IERS releases the value of _DUT1_, a closely related concept). The following image shows the variation of $\Delta T$ over the years.

```{figure} ./images/delta-t.png
:width: 80%
:align: center
:class: white-background
_Source:_ Wikipedia
```

Since $\Delta T$ is a complicated function of time, a new time was introduced the UTC or _Coordinated Universal Time_ which has an offset with respect to TAI that is an integer number of seconds. Given that the rate of rotation of the Earth is continuously decreasing due to the influence of the Moon, UTC keeps diverging from TAI. By convention the difference between UTC and TAI is kept within 0.9 seconds by introducing _leap seconds_ when necessary. Currently $\rm UTC=TAI-37\,s$. UTC is commonly referred as the _Civil Time_ and is the one used for most applications, including astronomical observations. It is important, however, to know what time scale we are using and whether it is the appropriate one for our purposes. Many astronomical libraries like [astropy.time](https://docs.astropy.org/en/stable/time/index.html) allow to convert between different time scales and are able to query the IERS Bulletins for updated values of the $\Delta T$ or `DUT1` parameters.

### Sidereal time

We have already introduced the concept of `sidereal time`, but let's define it properly now. So far our definition of day and time has been based (albeit mostly from a historical perspective) in the successive transits of the Sun over the local median. However, if we were to do the same exercise using a distant star (say, Deneb, $\alpha\ \rm Cyg$), a precise watch would measure that the time between two consecutive transits is less than 24 hours (about 23 hours and 56 minutes).

The reason is that in the time between the two transits the Earth has moved a bit along its orbit around the Sun. Since the Earth completes an orbit around the Sun in approximately 365 days, the Earth moves a bit under a degree in one day, or about 4 minutes.

```{figure} ./images/sidereal-time.png
:width: 80%
:align: center
:target: https://www.linkedin.com/pulse/sidereal-time-solar-standard-dr-m-elangovan
```

The sidereal time is defined based on the movement of the vernal equinox (or any fixed point on the celestial sphere). As with the apparent solar time, the sidereal time is affected by the ellipticity and inclination of the Earth's orbit. Because of this a _mean sidereal time_ (MST) is analogously defined. The mean sidereal time refers to the the time measured at the Greenwich meridian; the _local sidereal time_ (LST) is related to the MST by the longitude of the location, ${\rm LST} = {\rm MST} - {\rm longitude}$.

### Julian dates

The _Julian date_ (JD) is a continuous count of days and fractions of days since the beginning of the Julian Period at 12h UT on January 1, 4713 BC. The Julian date is widely used in astronomy because it provides a simple and unambiguous way to specify dates and times. A Julian day is defined as 86,400 SI seconds, which is the same as a mean solar day. Note that Julian dates change at noon UT unlike civil time. For example, the Julian date corresponding to 12h UT on April 10th 2025 is 2460776.0.

:::{hint}
Here is how to use `astropy.time` to determine the Julian date of a given time:

```{code-block} python
>>> from astropy.time import Time
>>> time = Time('2025-04-10 12:00:00', scale='utc')
>>> time.jd
2460776.0
```

We can also convert from a Julian date to a calendar date:

```{code-block} python
>>> time = Time(2460776.0, format='jd', scale='utc')
>>> time.iso
'2025-04-10 12:00:00.000'
```

:::

A variation on the Julian date is the _Modified Julian Date_, which is defined as

$$
\rm MJD=JD-2400000.5
$$

Note that not only are MJDs more compact, they also start at midnight UT. Here is an [MJD calendar](http://leapsecond.com/java/mjdcal.htm) for 2025.

## Measuring light

Astronomy can be justifiably be described as the science of light. While other sciences are able to probe their subjects matters via a number of different means, astronomy mainly relies on the study of the light that astronomical sources emit, reflect, or otherwise process. Fortunately for us, electromagnetic radiation (light) encodes a wealth of information about the sources that emit it which we can study by means of photometry, spectroscopy, polarimetry, and other techniques.

### The electromagnetic spectrum

Due to its wave-particle duality, the energy of a photon is related to its frequency or wavelength by the expression

$$
E = h \nu = \frac{hc}{\lambda}
$$

where $E$ is the energy of the photon, $h$ is Planck's constant ($6.626 \times 10^{-34}\ \rm J\ s$), $\nu$ is the frequency of the photon, $c$ is the speed of light in vacuum, and $\lambda$ is the wavelength of the photon. Also note that

$$
d\nu=d\lambda\cdot\dfrac{c}{\lambda^2}\\
\dfrac{d\nu}{\nu}=\dfrac{d\lambda}{\lambda}
$$

For convenience we often refer to the different parts of the spectrum by their wavelength ranges. While there is no strict definition the following ranges are commonly used:

| Name      | Wavelength                   |
| --------- | ---------------------------- |
| Gamma     | 0.1-10 $\unicode{x212B}$     |
| X-ray     | 10-100 $\unicode{x212B}$     |
| Far UV    | 100-1000 $\unicode{x212B}$   |
| Near UV   | 1000-3500 $\unicode{x212B}$  |
| Optical   | 3500-10000 $\unicode{x212B}$ |
| Near IR   | 1-10 $\rm \mu m$             |
| Mid IR    | 10-100 $\rm \mu m$           |
| Far IR    | 100-1000 $\rm \mu m$         |
| Microwave | 1-100 $\rm mm$               |
| Radio     | > 0.1 m                      |

As you can see, the units we typically use for for wavelength change depending on the type of radiation we are studying. Wavelength and frequency are related as $\nu=c/\lambda$. Traditionally astronomers have used wavelength units for optical and infrared radiation, while radio astronomers use frequency units. In the case of X-ray and gamma-ray astronomy, both units are used.

Astronomers have many ways to quantify the amount of electromagnetic radiation emitted by an object. We can defined the _specific intensity_ $I_\nu$ (sometime called radiance) as the energy emitted by a surface per unit of area per unit of time per unit of frequency (or wavelength) and per unit of solid angle. The units of specific intensity are watts per steradian per square metre per hertz (or, in CGS, ergs per square centimetre per steradian per hertz per second). For an angle $\theta$ that is measured from the normal to the surface

```{figure} ./images/specific-intensity.png
:width: 80%
:align: center
```

$$
I_\nu=\dfrac{dE}{\cos\theta dA\,dt\,d\nu\,d\Omega}
$$

and $I_\lambda=c/\lambda^2 I_\nu$.

The _monochromatic flux_ (also called _brightness_ or irradiance) is the amount of energy that passes through a unit surface from all directions

$$
F_\nu=\int I_\nu \cos\theta d\Omega
$$

where we can often assume $\cos\theta\approx 1$ since our detectors only collect photons from a small solid angle perpendicular to its surface.

Note that as with the specific intensity, the monochromatic flux (sometimes called flux density) is defined per unit of frequency or wavelength. We can integrate over the entire wavelength range to get the total flux $F$.

The _luminosity_ is the total amount of energy emitted by a source per unit of time and is related to the total flux by the distance to the source

$$
L = 4\pi d^2 F
$$

:::{note}
Astronomers normally measure flux for unresolved sources (point source, for example stars) and specific intensity (often called surface brightness in this context) for extended sources (like galaxies).
:::

While some types of detectors (for example bolometers) are able to measure the spectrum of the light (the specific intensity), most detectors measure the number of photons received over time. Because of this we need to define the _photon flux_ $F_{{\rm photon}}$ as

$$
F_{{\rm photon}}=\int F_\lambda\dfrac{\lambda}{hc}d\lambda
$$

## Magnitudes

The quantities defined in the previous section express the amount of light emitted by a source. Astronomers, however, tend to use a different system to measure flux (brightness): _magnitudes_. The magnitude system was first defined by the Greek astronomer Hipparchus in the 2nd century BC. In this system start of magnitude 1 are the first ones visible to the naked eye just after sunset, while the faintest starts visible at the end of the twilight are of magnitude 6. Intermediate magnitudes were defined by dividing the twilight in equal parts. The magnitude system remained in used for many centuries and, while imprecise, it was not until the advent of photography and detectors that could measure light more quantitatively that the system was redefined.

The modern magnitude system takes into account that the human eye responds to stimuli in an approximately [logarithmic way](https://en.wikipedia.org/wiki/Weber–Fechner_law). From that, the difference in _apparent magnitude_ between two sources is defined as proportional to the logarithm of the ratio of their fluxes:

$$
m_1 - m_2 \propto \log\left( \dfrac{F_1}{F_2} \right)
$$

In the 19th century the English astronomer Pogson further refined this definition by requiring a start of magnitude 6 to be 100 times fainter than one of magnitude 1. This is equivalent to

$$
m_1 - m_2 = -2.5 \log\left( \dfrac{F_1}{F_2} \right)
$$

and also equivalent to saying that a star of magnitude 2 is $100^{1/5}\approx2.512$ times fainter than a star of magnitude 1. Note the minus sign that is encodes the fact that larger magnitudes mean fainter sources. Apparent magnitudes defined this way are called _Pogson magnitudes_.

:::{important}
Pogson magnitudes are always defined using photon fluxes.
:::

Apparent magnitudes are defined for a given passband or wavelength range (more on this later). _Bolometric magnitudes_ account for the electromagnetic flux received from a source in all wavelengths. The difference between the apparent magnitude in a bandpass $X$ and the total bolometric magnitude is called the _bolometric correction_, ${\rm BC}_X$ and is defined as

$$
{\rm BC}_X = m_{\rm bol} - m_X
$$

In practice bolometric magnitudes are very difficult to measure and the bolometric correction is usually estimated from the spectral energy distribution (SED) of the source, which are in turn determined from models for a given astronomical object (for example, for a start of a certain spectral type).

The _absolute magnitude_ $M$ is defined as the apparent magnitude of a source at a distance of 10 parsecs. It is related to the apparent magnitude $m$ and the distance $d$ (in parsecs) to the source by

$$
m - M = 5 \log d - 5
$$

Finally, the _absolute bolometric magnitude_ is directly related to the luminosity of a source using the solar luminosity as a reference:

$$
M_{\rm bol} = -2.5 \log \left( \dfrac{L}{L_\odot} \right) + 4.74
$$

where $L_\odot$ is the luminosity of the Sun. The absolute bolometric magnitude is a measure of the total energy emitted by a source and is independent of distance.

### Photometric systems

So far all the the apparent magnitudes we have defined have been in reference to another magnitude, that is to the ratio of their fluxes. We can do

$$
m - m_0 = -2.5 \log\left( \dfrac{F}{F_0} \right)
m = -2.5 \log F + C(\lambda)
$$

where $C(\lambda)$ is called a _zero-point_ and refers to the flux that corresponds to a magnitude of 0 for a given wavelength. The choice and characterisation of $C(\lambda)$ is what define a _photometric system_.

Historically most photometric systems where defined so that the zero-point corresponds to the flux of Vega at each wavelength, and as such are called VEGAMAG systems. Later the average spectrum of a group of A0V stars such as Vega was used. Vega was used as a reference for two reasons: it's one of the brightest stars on the sky and A-type stars have relatively smooth, well understood spectra.

One of the most common photometric systems, the UBVRI system or Johnson can be defined for each bandpass as

$$
m_{UBVRI} = -2.5 \dfrac{\int_{UBVRI}F_{UBVRI}\lambda d\lambda}{\int_{UBVRI}F_{UBVRI}({\rm Vega})\lambda d\lambda}
$$

where the integrals are over the bandpass of the filter and the $\lambda$ factor is included to convert from flux to photon flux.

A conceptually different photometric system is the AB magnitude system. Here we assume a constant zero-point flux $F_{0,\nu}=3631\, {\rm Jy}$ which is the flux density of Vega at $5500\,\unicode{x212B}$ in [Jankys](https://en.wikipedia.org/wiki/Jansky). With this

$$
m_{AB}=-2.5\log F_\nu-48.6
$$

when $F_\nu$ is in Jy. Normally we defined an AB magnitude for a certain filter bandpass so that

$$
m_{AB}=-2.5\log\left(\dfrac{\int (F_\nu / \nu) d\nu}{\int (F_{0,\nu}/\nu) d\nu}\right)
$$

where again the $1/\nu$ factor is included to convert from flux to photon flux.

The [STMAG](https://www.stsci.edu/hst/instrumentation/acs/data-analysis/zeropoints) zero-point system makes similar assumptions to the AB system but for a constant flux per unit of wavelength and was developed primarily for the Hubble Space Telescope bandpasses.

Why are AB and STMAG systems not the one primarily used? While much more simpler to define, the AB and STMAG systems are not based on a real source (there are no sources with a constant flux density) and as such they are more difficult to calibrate. However the most common modern photometric systems are either based on the AB system or have been cross-calibrated and allow for a direct comparison with it.

### Colours

The _colour index_ or just colour is the difference between two magnitudes in different bandpasses. In this case the colour corresponds to the ratio of fluxes (a concept that is closely related to the usual definition of "colour"). For a VEGAMAG system, the colour gives the ratio of the fluxes relative to the ration of the fluxes of an A0V star.

### Surface brightness

So far we have implicitly discussed the brightness of unresolved point sources. For a resolved sources like a galaxy or a nebula we can define an equivalent concept, the _surface brightness_, $S_X$ (for a bandpass $X$) can be defined as the magnitude equivalent to the average flux per square arcsecond. If the object in question subtends an area $A$ an $\rm arcsec^2$ then

$$
S_X=-2.5\log\left(\dfrac{F_X}{A}\right)= -2.5\log F_X + 2.5\log A = m_X+2.5\log A
$$

### Filters

Photometric systems are usually defined for a set of well-defined filters, each one letting pass only a certain range of wavelengths, and with a known transmission curve. The following figure shoes the transmission curves of several common photometric systems/filter sets. Often the filters (e.g., the SDSS system) were developed for a specific telescope and project but have since become widely used.

```{figure} ./images/filters.png
:width: 80%
:align: center
:target: http://astroweb.case.edu/ssm/ASTR620/mags.html
```

Photometric systems are often defined in terms of their effective central wavelength and the equivalent width of the filter. The equivalent width is defined as that of a rectangular filter with 100% transmission centred around the effective wavelength.

```{figure} ./images/filters-table.png
:width: 80%
:align: center
:target: https://ui.adsabs.harvard.edu/abs/2005ARA&A..43..293B
```

These filters are usually called "broadband" because they have non-zero transmission over a wide range of wavelengths (hundreds or thousands of angstroms). There are also "narrow-band" filters, which have a much narrower transmission range (typically 10-100 $\unicode{x212B}$) and are used to isolate specific spectral lines. Typical narrow-band filters are H$\alpha$ [OII], [OIII], [SII], etc. For extragalactic targets the recession velocity of the source needs to be taken into account as the emission line of interest may have been red- or blue-shifted. Because of that narrow-band filters are often produced in sets to cover a range of central wavelengths.

## Optics and telescopes

Coming soon.

## Further reading

- Birney, D. S., Gonzalez, R. A., and Oesper, D. (2006). Observational Astronomy (2nd ed.)
- Smart, W. M. (1977). Textbook on Spherical Astronomy (6th ed.)
- Ryden, B., and Peterson, B. M. (2010). Foundations of Astronomy (3rd ed.)
- [International Celestial Reference System](https://aa.usno.navy.mil/faq/ICRS_doc)
