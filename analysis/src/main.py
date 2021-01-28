import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import scipy
from sklearn.linear_model import LinearRegression

ozoneData = pd.read_csv('../resources/home_ppb_analog_2021-01-25T07:00:00Z',
                        names=['ppb', 'analogVal'])

berlinData = pd.read_csv('../resources/ber_mc174_20210125-20210126.csv',
                         skiprows=3,
                         sep=';')

hourlyData = ozoneData.groupby(ozoneData.index // 3600).mean()

sensorAndBerlinData = pd.concat([hourlyData, berlinData], axis=1)

model = LinearRegression().fit(
    sensorAndBerlinData[['analogVal']],
    sensorAndBerlinData['no2']
)

print('\n= Fitted model:')
print("f(x) = " + str(model.coef_[0]) + "x + " + str(model.intercept_))
print('R2 score: ' + str(model.score(sensorAndBerlinData[['analogVal']], sensorAndBerlinData['no2'])))

print('\n= Correlation between analogVal and NO2:')
print("Pearson (correlation, pvalue): " +
      str(scipy.stats.pearsonr(sensorAndBerlinData['analogVal'], sensorAndBerlinData['no2']))
)
print(scipy.stats.spearmanr(sensorAndBerlinData['analogVal'], sensorAndBerlinData['no2']))
print(scipy.stats.kendalltau(sensorAndBerlinData['analogVal'], sensorAndBerlinData['no2']))

print('')

# Show fancy plot with regression line
sn.lmplot(x='analogVal', y='no2', data=sensorAndBerlinData, fit_reg=True)
plt.show()
