from datetime import datetime
from entities import MonthlyCases
from entities.QuarterlyCovidCases import QuarterlyCovidCases
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases
from Utilities.Utils import QUARTERS

class ProcessCovidCases:

    def __init__(self) -> None:
        self._monthly_covid_cases = []
        self._quarterly_covid_cases = []

    def process_monthly_cases(self, raw_covid_data: list[(str, str, int, int, int, int)]) -> None:
        # Maps datetime objects in the form of year-month to a list of Daily Case objects
        date_to_cases = {}

        for data in raw_covid_data:
            date_reported = data[0]
            country_code = data[1]
            new_cases = data[2]
            cumulative_cases = data[3]
            new_deaths = data[4]
            cumulative_deaths = data[5]

            # Initialize the attributes of the datetime object.
            year = date_reported.year
            month = date_reported.month
            day = date_reported.day

            # Convert datetime object into a string used for the dictionary mapping.
            year_month = str(year) + '-' + str(month)

            # If the date is not in the dictionary, intialize it with a list of a daily case object.
            if year_month not in date_to_cases:
                date_to_cases[year_month] = [DailyCases(country_code, cumulative_cases, new_cases, day)]
            
            # If the date is already a key, add to it's list value with a daily case object.
            else:
                date_to_cases[year_month].append(DailyCases(country_code, cumulative_cases, new_cases, day))

        
        # Iterate through every key in the date_to_cases dictionary
        for date in date_to_cases:
            month_list_cases = date_to_cases[date]
            cumulative_cases = date_to_cases[date][-1].cumulative_cases
            
            # create a monthly covid case object for each iteration and then append it to the _monthly_covid_cases list attribute.
            monthly_covid_case = MonthlyCovidCases(month_list_cases, cumulative_cases, date.year, date.month)
            self._monthly_covid_cases.append(monthly_covid_case)
    
    def process_quarterly_cases(self) -> None:
        """Process Covid data into Quarters."""
        years_and_quarters = {}
        
        for monthly_case in self._monthly_covid_cases:
            quarter = QUARTERS[monthly_case.month]
            year = monthly_case.year

            # Convert datetime object into string to be used as a key in dictionary.
            year_quarter = str(year) + '-' + str(quarter)

            if year_quarter not in years_and_quarters:
                years_and_quarters[year_quarter] = [monthly_case]
            
            else:
                years_and_quarters[year_quarter].append(monthly_case)
        
        for quarter in years_and_quarters:
            quarter_list_cases = years_and_quarters[quarter]
            cumulative_cases = years_and_quarters[quarter][-1].cumulative_cases
            quarter = QUARTERS[years_and_quarters[quarter][0].month]

            quarterly_covid_cases = QuarterlyCovidCases(quarter_list_cases, cumulative_cases, quarter)

            self._quarterly_covid_cases.append(quarterly_covid_cases)
