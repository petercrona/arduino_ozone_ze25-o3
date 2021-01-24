# arduino_ozone_ze25-o3

Coded this for a blog post on https://www.babyfriendlyair.com where I played
around with this sensor.

## Sensor

Code for Arduino, you can open the ino file, connect the sensor to the digital pin 2.

The data is just written to "Serial" so that it can easily be stored
by `cat /dev/ttyACM0 > data` for instance (on Arch Linux at least).

Sorry if I offend anyone by not following Arduino or C++ conventions,
this is the first time I play around with an Arduino and first time
in many years I code C++.

The sensor used is Winsen ZE25-O3, see: https://www.winsen-sensor.com/sensors/o3-gas-sensor/ze25-o3.html

## Analysis

Some trivial analysis and plotting of the data with Python.
