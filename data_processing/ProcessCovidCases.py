from datetime import datetime
from entities.QuarterlyCovidCases import QuarterlyCovidCases
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases
from Utilities.Utils import QUARTERS

class ProcessCovidCases:
    _monthly_covid_cases: list[DailyCases]
    _quarterly_covid_cases: list[MonthlyCovidCases]

    def __init__(self) -> None:
        self._monthly_covid_cases = []
        self._quarterly_covid_cases = []

    def process_monthly_cases(self, raw_covid_data: list[(datetime, str, int, int, int, int)]) -> None:
        """ Processes the raw_covid_data by instantiating a monthly covid case object using the data from each row in the raw covid data.

        The monthly covid case objects will then be appended to private attribute: _monthly_covid_cases


        Preconditions:
            - raw_covid_data != []
        """

        # Dictionary that holds dates in the form of year-month as a string. Each key has a value of a list of
        # Daily Covid Case objects which represents every row in the raw covid data. 
        dates_and_daily_cases = {}

        for data in raw_covid_data:
            # Initialize variables for each part of the row tuple data.
            date_reported = data[0]
            country_code = data[1]
            new_cases = data[2]
            cumulative_cases = data[3]

            # Initialize the attributes of the datetime object.
            year = date_reported.year
            month = date_reported.month

            # Convert datetime object into a string used as keys for the dates_and_daily_cases dictionary. 
            year_month = str(year) + '-' + str(month)

            # If the date is not in the dates_and_daily_cases dictionary, intialize it with a list of a daily case object.
            if year_month not in dates_and_daily_cases:
                dates_and_daily_cases[year_month] = [DailyCases(country_code, cumulative_cases, new_cases, date_reported)]
            
            # If the date is already a key, add to it's list value with a daily case object.
            else:
                dates_and_daily_cases[year_month].append(DailyCases(country_code, cumulative_cases, new_cases, date_reported))

        
        # Iterate through every key (strings in the form of year-month) in the dates_and_daily_cases dictionary
        for date in dates_and_daily_cases:
            monthly_cases = dates_and_daily_cases[date]

            # The cumulative cases for the month will be equal to the total cases in the last day of the month.
            # In this case, the last day of the month represents the last Daily Case object in the dictionary list value.
            cumulative_cases = dates_and_daily_cases[date][-1].cumulative_cases

            # Since all daily cases belong in the same month and year for each key, taking the date.month and date.year attributes of any daily case object will work.
            month = dates_and_daily_cases[date][0].date.month
            year = dates_and_daily_cases[date][0].date.year

            # create a monthly covid case object for each iteration and then append it to the _monthly_covid_cases list attribute.
            monthly_covid_case = MonthlyCovidCases(monthly_cases, cumulative_cases, month, year)
            self._monthly_covid_cases.append(monthly_covid_case)
    
    def process_quarterly_cases(self) -> None:
        """Process Covid data into Quarters.
        
        Preconditions:
            - self._monthly_covid_cases != []
        """
        # Maps year-quarter to a list of their monthly covid case objects.
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

            quarterly_covid_cases = QuarterlyCovidCases(quarter_list_cases, cumulative_cases, quarter, years_and_quarters[quarter][0].year)

            self._quarterly_covid_cases.append(quarterly_covid_cases)
