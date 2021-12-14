"""CSC110 Final Project: Main Runfile

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
import numpy as np
import plotly.express as px
from data_processing.ProcessCovidCases import ProcessCovidCases
from data_loading.LoadCovidCases import LoadCovidCases
from data_loading.LoadUnemployment import LoadUnemployment
from data_processing.ProcessUnemployment import ProcessUnemployment
from data_loading.LoadShipping import LoadShipping
from data_processing.ProcessShippingData import ProcessShippingData
from data_loading.LoadGdp import LoadGdp
from data_processing.ProcessGdp import ProcessGdp
from regression.regression import Regression

def main():
    # Covid Cases
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

    # GDP
    gdp_file_path = '../statistic_id188185_real-gdp-growth-by-quarter-in-the-us-2011-2021.xlsx'
    load_gdp = LoadGdp(gdp_file_path)
    loaded_gdp_data = load_gdp.load_data()

    process_gdp_data = ProcessGdp()
    process_gdp_data.process_gdp(loaded_gdp_data)
    quarterly_gdp = process_gdp_data.quarterly_gdp

    Regression(quarterly_covid_cases, quarterly_unemployment, quarterly_shipping, quarterly_gdp)



# Extract for the US, and get date_reported and cumulative_cases. 
# One graph: x-axis: date, y-axis: monthly cumulative cases from 2019-present
# Second graph: x-axis: date, y-axis: average monthly covid-growth


if __name__ == "__main__":
    main()


