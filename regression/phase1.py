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
process_unemployment_data.process_quarterly_unemployment()
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
quarterly_unemployment = [quarter.calculate_average_quarterly_unemployment() for quarter in quarterly_unemployment]
quarterly_shipping = [quarter.calculate_quarterly_value() for quarter in quarterly_shipping]
quarterly_gdp = [quarter.growth for quarter in quarterly_gdp]


X = [[quarterly_covid_cases], [quarterly_unemployment], [quarterly_shipping]]
y = [quarterly_gdp]

x_train, x_test, y_train, y_test = train_test_split(X, ytest_size=0.2, random_state=0)

# Train model on training set
train_regr = linear_model.LinearRegression()
train_regr.fit(x_train, y_train)

# Predicting Test Set Results
y_pred = train_regr.predict(x_test)

# Evaluating coefficient of determination
r2_score = r2_score(y_test, y_pred)


regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
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