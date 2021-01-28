# Analysis with Python

Calculates correlation between data collected with a Winsen ZE25-O3 (indoor) and nitrogen dioxide (NO2) measured by
Berlin Air Quality Station MC174 (https://luftdaten.berlin.de/station/mc174).

Furthermore, a simple linear model is fitted using linear regression. This model
can be used to given the voltage (represented by a integer between 0 and 1023)
predict the outdoor NO2 concentration.

This can be useful, as it can be combined with outdoor ratios
identified in studies (for instance https://link.springer.com/article/10.1007/s10653-019-00441-0?shared-article-renderer)
to estimate indoor NO2. If this is done under "normal circumstances" in the indoor environment,
it might give you a decent estimate of NO2 indoor also under non-normal cirumstances,
for instance if you are testing air purification technologies or are doing something that
might generate NO2.

# NO2? Shouldn't it be O3?
During the experiment we found stronger correlation between the sensor's voltage and NO2 than O3.
This is not completely surprising, as electrochemical ozone sensor are known to be cross sensitive with NO2,
this is also stated in the sensor's datasheet.

We actually observed a negative correlation between voltage and ozone, despite that the datasheet
states it should be positive. We suspect this comes from the fact that as O3 increases, NO2 decreases.
Something that can clearly be seen at for instance https://luftdaten.berlin.de/station/mc174 (2021-01-28).
