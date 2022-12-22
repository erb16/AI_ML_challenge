# import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

data = pd.read_csv('share-vehicle-electric.csv')
data.dropna(inplace=True)
selection = input('Country: ')
year = input('Year: ')
year = int(year)
country = data[data.Entity == selection]

y = country['battery_electric_share']
X = country[['Year']]
slope, intercept, r_value, p_value, std_err = linregress(country["Year"], country["battery_electric_share"])
predict_y = intercept + slope * int(year)
predict_y = round(predict_y, 2)
print(f'Prediction: {predict_y}% by {year}')

g, ax = plt.subplots()
sns.scatterplot(x="Year", y="battery_electric_share", ax=ax, data=country)
slope, intercept, r_value, p_value, std_err = linregress(country["Year"], country["battery_electric_share"])
ax.plot(range(2005, year), [i*slope + intercept for i in range(2005, year)], color="blue")
ax.set_title(f"New registrations of electric battery cars in {selection} (% of total car registrations)")
ax.set(ylabel="New electric battery car registrations (%)")
g.show()
