# Analysis with Python

Calculates correlation between data collected with a Winsen ZE25-O3 and nitrogen dioxide (NO2) measured by
Berlin Air Quality station MC174 (https://luftdaten.berlin.de/station/mc174).

A simple linear model is also created using linear regression. This model
can be used to given the voltage (represented by a integer between 0 and 1023)
predict the outdoor NO2 concentration.

# NO2? Shouldn't it be O3?
During the experiment we found stronger correlation between the sensor's voltage and NO2 than O3.
This is not completely surprising, as electrochemical ozone sensor are known to be cross sensitive with NO2,
this is also stated in the sensor's datasheet.

We also observed a negative correlation between voltage and ozone in fact, despite that the datasheet
states it should be positive. We suspect this comes from the fact that as O3 increases, NO2 decreases.
Something that can clearly be seen at for instance https://luftdaten.berlin.de/station/mc174 (2021-01-28).
