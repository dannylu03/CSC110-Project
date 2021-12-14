"""CSC110 Final Project: Regression Regression

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
import pandas as pd
import plotly.express as px
from entities.QuarterlyCovidCases import QuarterlyCovidCases
from entities.QuarterlyUnemployment import QuarterlyUnemployment
from entities.QuarterlyShipping import QuarterlyShipping
from entities.QuarterlyGdp import QuarterlyGdp


class Regression:
    """Contains methods to create graphs"""

    def __init__(self, quarterly_covid_cases: list[QuarterlyCovidCases], quarterly_unemployment: list[QuarterlyUnemployment],
                 quarterly_shipping: list[QuarterlyShipping], quarterly_gdp: list[QuarterlyGdp]) -> None:
        self._quarterly_covid_cases = quarterly_covid_cases
        self._quarterly_unemployment = quarterly_unemployment
        self._quarterly_shipping = quarterly_shipping
        self._quarterly_gdp = quarterly_gdp

    def run_phase_1(self) -> None:
        """Creates graphs for phase 1"""

        quarterly_unemployment = [quarter.calculate_average_quarterly_unemployment() for quarter in
                                  self._quarterly_unemployment if 2011 <= quarter.get_year() < 2020]
        quarterly_shipping = [quarter.quarterly_value for quarter in self._quarterly_shipping if 2011 <= quarter.year < 2020]
        quarterly_gdp = [quarter.growth for quarter in self._quarterly_gdp if 2011 <= quarter.year < 2020]

        quarterly_unemployment = {'Quarterly Unemployment Rate': quarterly_unemployment}
        quarterly_shipping = {'Quarterly Shipping': quarterly_shipping}
        quarterly_gdp = {'Quarterly GDP': quarterly_gdp}

        # Merge all the dictionaries into one.
        data = {**quarterly_unemployment, **quarterly_shipping, **quarterly_gdp}

        # Convert the data dictionary into a variable called df which is a pandas dataframe.
        df = pd.DataFrame(data)

        # Plot two graphs with a linear regression line.
        plot_graph_with_linear_regression(df, 'Quarterly Shipping', 'Quarterly GDP', 0.65)
        plot_graph_with_linear_regression(df, 'Quarterly Unemployment Rate', 'Quarterly GDP', 0.65)

    def run_phase_2(self) -> None:
        """Creates graphs for phase 2"""

        quarterly_covid_cases = [quarter.calculate_average_daily_increase() for quarter in self._quarterly_covid_cases]
        quarterly_unemployment = [quarter.calculate_average_quarterly_unemployment() for quarter in
                                  self._quarterly_unemployment if quarter.get_year() >= 2020]
        quarterly_shipping = [quarter.quarterly_value for quarter in self._quarterly_shipping if quarter.year >= 2020]

        # Convert lists into dictionary mappings and the keys will represent columns in a dataframe.
        quarterly_covid_cases = {'Quarterly New Covid Cases': quarterly_covid_cases}
        quarterly_unemployment = {'Quarterly Unemployment Rate': quarterly_unemployment}
        quarterly_shipping = {'Quarterly Shipping': quarterly_shipping}

        quarterly_covid_cases['Quarterly New Covid Cases'].pop()
        quarterly_unemployment['Quarterly Unemployment Rate'].pop()

        # Merge the quarterly_covid_cases and quarterly_shipping dictionaries together.
        data1 = {**quarterly_covid_cases, **quarterly_shipping}

        # Convert dictionary into dataframe
        df1 = pd.DataFrame(data1)

        for i in range(len(quarterly_unemployment['Quarterly Unemployment Rate']) - 1):
            if quarterly_unemployment['Quarterly Unemployment Rate'][i] > 12:
                quarterly_unemployment['Quarterly Unemployment Rate'].pop(i)
                quarterly_covid_cases['Quarterly New Covid Cases'].pop(i)

        # Merge the quarterly_covid_cases and quarterly_unemployment dictionaries together.
        data2 = {**quarterly_covid_cases, **quarterly_unemployment}
        df2 = pd.DataFrame(data2)

        plot_graph_with_linear_regression(df1, 'Quarterly New Covid Cases', 'Quarterly Shipping', 0.65)
        plot_graph_with_linear_regression(df2, 'Quarterly New Covid Cases', 'Quarterly Unemployment Rate', 0.65)

def plot_graph_with_linear_regression(dataframe: DataFrame, x_axis: str, y_axis: str, opacity: float) -> None:
    """Creates scatter plot and best fit line"""

    fig = px.scatter(
        dataframe, x_axis, y_axis, opacity,
        trendline='ols', trendline_color_override='darkblue'
    )

    fig.show()