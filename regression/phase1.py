# Dependent: GDP
# Independent: Covid Cases, unemployment, shipping
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from data_processing.ProcessCovidCases import ProcessCovidCases
from data_loading.LoadCovidCases import LoadCovidCases
from data_loading.LoadUnemployment import LoadUnemployment
from data_processing.ProcessUnemployment import ProcessUnemployment
from data_loading.LoadShipping import LoadShipping
from data_processing.ProcessShippingData import ProcessShippingData
from data_loading.LoadGdp import LoadGdp
from data_processing.ProcessGdp import ProcessGdp
import pandas as pd
import plotly.express as px

# --- Covid Cases
covid_file_path = '../data/WHO-COVID-19-global-data.csv'
load_covid = LoadCovidCases(covid_file_path)
loaded_covid_data = load_covid.load_data()

process_covid_data = ProcessCovidCases()
process_covid_data.process_monthly_cases(loaded_covid_data)
process_covid_data.process_quarterly_cases()
quarterly_covid_cases = process_covid_data._quarterly_covid_cases

# --- Unemployment
unemployment_file_path = '../data/unemployment.csv'
load_unemployment = LoadUnemployment(unemployment_file_path)
loaded_unemployment_data = load_unemployment.load_data()

process_unemployment_data = ProcessUnemployment()
process_unemployment_data.process_quarterly_unemployment(loaded_unemployment_data)
quarterly_unemployment = process_unemployment_data._quarterly_unemployment

# Shipping
shipping_file_path = '../data/shipping.csv'
load_shipping = LoadShipping(shipping_file_path)
loaded_shipping_data = load_shipping.load_data()

process_shipping_data = ProcessShippingData()
process_shipping_data.process_monthly_trades(loaded_shipping_data)
process_shipping_data.process_quarterly_trades()
quarterly_shipping = process_shipping_data._quarterly_ship_trades

# --- GDP
gdp_file_path = '../data/statistic_id188185_real-gdp-growth-by-quarter-in-the-us-2011-2021.xlsx'
load_gdp = LoadGdp(gdp_file_path)
loaded_gdp_data = load_gdp.load_data()

process_gdp_data = ProcessGdp()
process_gdp_data.process_gdp(loaded_gdp_data)
quarterly_gdp = process_gdp_data.quarterly_gdp

quarterly_covid_cases = [quarter._cumulative_cases for quarter in quarterly_covid_cases]
quarterly_unemployment = [quarter.calculate_average_quarterly_unemployment() for quarter in quarterly_unemployment if
                          quarter._year >= 2020]
quarterly_shipping = [quarter.quarterly_value for quarter in quarterly_shipping if quarter.year >= 2020]
quarterly_gdp = [quarter.growth for quarter in quarterly_gdp if quarter.year >= 2020]

quarterly_covid_cases = {'Quarterly Covid Cases': quarterly_covid_cases}
quarterly_unemployment = {'Quarterly Unemployment Rate': quarterly_unemployment}
quarterly_shipping = {'Quarterly Shipping': quarterly_shipping}
quarterly_gdp = {'Quarterly GDP': quarterly_gdp}

# Don't want the last quarter
quarterly_covid_cases['Quarterly Covid Cases'].pop()
quarterly_unemployment['Quarterly Unemployment Rate'].pop()

data = {**quarterly_covid_cases, **quarterly_unemployment, **quarterly_shipping, **quarterly_gdp}
df = pd.DataFrame(data)

print(quarterly_covid_cases)
print(quarterly_gdp)
print(quarterly_unemployment)
print(quarterly_shipping)

X = df[['Quarterly Covid Cases', 'Quarterly Unemployment Rate', 'Quarterly Shipping']]
y = df['Quarterly GDP']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model on training set
train_regr = linear_model.LinearRegression()
train_regr.fit(x_train, y_train)

# Predicting Test Set Results
y_pred = train_regr.predict(x_test)

# Evaluating coefficient of determination
r2_score = r2_score(y_test, y_pred)

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(r2_score)
print(regr.coef_)

# GDP - Covid
covid_fig = px.scatter(
    df, x='Quarterly Covid Cases', y='Quarterly GDP', opacity=0.65,
    trendline='ols', trendline_color_override='darkblue'
)

covid_model = linear_model.LinearRegression()
regr.fit(df['Quarterly Covid Cases'], df['Quaterly GDP'])


unemployment_fig = px.scatter(
    df, x='Quarterly Unemployment Rate', y='Quarterly GDP', opacity=0.65,
    trendline='ols', trendline_color_override='darkblue'
)

shipping_fig = px.scatter(
    df, x='Quarterly Shipping', y='Quarterly GDP', opacity=0.65,
    trendline='ols', trendline_color_override='darkblue'
)

covid_fig.show()
unemployment_fig.show()
shipping_fig.show()
"""
LoadData(variables)
^ All variables will be a DataFrame object and be on a monthly basis ?
covid_cases[cumulative_cases] <- filter for desired country 
unemployment[unemployment_rate]
shipping[???] <- prob smt to do with monthly vessel worth in USD
^ Filter all so they have the same time interval (Start on the same datetime and end on the same datetime)
X = [[covid_cases['cumulative_cases'], unemployment['unemployment_rate'], shipping]]
y = [gdp]
x_train, x_test, y_train, y_test = train_test_split(X, ytest_size = 0.3, random_state=0)
# Train Model on Training Set
train_regr = LinearRegression()
train_regr.fit(x_train, y_train)
# Predicting Test Set Results
y_pred = train_regr.predict(x_test)
return y_pred
# Evaluating coefficient of determination
r2_score(y_test, y_pred)
regr = linear_model.LinearRegression() <- using sklearn library
regr.fit(X, y)
return regr.coef_
^ Important values, tells us the importance of each independent variable
"""
