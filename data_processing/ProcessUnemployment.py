"""CSC110 Final Project: Data Processing Process Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from entities.MonthlyUnemployment import MonthlyUnemployment
from entities.QuarterlyUnemployment import QuarterlyUnemployment
from Utilities.Utils import QUARTERS


class ProcessUnemployment:
    """Processes the raw unemployment data from LoadUnemployment"""

    def __init__(self) -> None:
        self._monthly_unemployment = []
        self._quarterly_unemployment = []

    def process_quarterly_unemployment(self, raw_unemployment_data: list[(str, int)]) -> None:
        """ Processes raw data into list of QuarterlyUnemployment objects"""
        # Create dict mapping year and quarter to list of MonthlyUnemployment objects
        date_to_list_monthly = {}

        # Populate the dictionary mapping
        for data in raw_unemployment_data:
            date_list = data[0].split('-')  # date[0] is string representation of the date
            year = int(date_list[0])
            month = int(date_list[1])
            quarter = QUARTERS[month]  # mapping the month to the different quarters in Utilities
            year_quarter = str(year) + '~' + str(quarter)
            unemployment_rate = data[1]

            # Adding to date_to_list_monthly dictionary, mapping year_quarter to a MonthlyUnemployment object
            if year_quarter not in date_to_list_monthly:
                date_to_list_monthly[year_quarter] = [MonthlyUnemployment(month, year, unemployment_rate)]
            else:
                date_to_list_monthly[year_quarter].append(MonthlyUnemployment(month, year, unemployment_rate))

        # Create and append QuarterlyUnemployment objects to the _quarterly_unemployment list
        for year_quarter in date_to_list_monthly:
            list_monthly = date_to_list_monthly[year_quarter]
            quarter = QUARTERS[list_monthly[0].month]
            year = list_monthly[0].year
            self._quarterly_unemployment.append(QuarterlyUnemployment(list_monthly, quarter, year))
