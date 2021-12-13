from datetime import datetime
from entities.QuarterlyCovidCases import QuarterlyCovidCases
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases
from Utilities.Utils import QUARTERS

class ProcessCovidCases:
    _monthly_covid_cases: list[MonthlyCovidCases]
    _quarterly_covid_cases: list[QuarterlyCovidCases]

    def __init__(self) -> None:
        self._monthly_covid_cases = []
        self._quarterly_covid_cases = []

    def process_monthly_cases(self, raw_covid_data: list[(str, str, int, int)]) -> None:
        """ Processes the raw_covid_data by instantiating a monthly covid case object using the data from each row in the raw covid data.

        The monthly covid case objects will then be appended to private attribute: _monthly_covid_cases


        Preconditions:
            - raw_covid_data != []
        """

        # Dictionary that holds dates in the form of year-month as a string. Each key has a value of a list of
        # Daily Covid Case objects which represents every row in the raw covid data. 
        dates_and_daily_cases = {}

        raw_covid_data = [row for row in raw_covid_data if row[1] == "US"]

        for data in raw_covid_data:
            # Initialize variables for each part of the row tuple data.
            date_reported = data[0]
            country_code = data[1]
            new_cases = data[2]
            cumulative_cases = data[3]

            date_list = date_reported.split('-')

            # Initialize the attributes of the datetime object.
            year = int(date_list[0])
            month = int(date_list[1])

            # Convert integer into a string used as keys for the dates_and_daily_cases dictionary. 
            year_month = str(year) + '-' + str(month)

            # If the date is not in the dates_and_daily_cases dictionary, intialize it with a list of a daily case object.
            if year_month not in dates_and_daily_cases:
                dates_and_daily_cases[year_month] = [DailyCases(country_code, cumulative_cases, new_cases, year, month)]
            
            # If the date is already a key, add to it's list value with a daily case object.
            else:
                dates_and_daily_cases[year_month].append(DailyCases(country_code, cumulative_cases, new_cases, year, month))

        
        # Iterate through every key (strings in the form of year-month) in the dates_and_daily_cases dictionary
        for date in dates_and_daily_cases:
            monthly_cases = dates_and_daily_cases[date]

            # The cumulative cases for the month will be equal to the total cases in the last day of the month.
            # In this case, the last day of the month represents the last Daily Case object in the dictionary list value.
            cumulative_cases = dates_and_daily_cases[date][-1].cumulative_cases

            # Since all daily cases belong in the same month and year for each key, taking the month and year attributes of any daily case object will work.
            month = dates_and_daily_cases[date][0].month
            year = dates_and_daily_cases[date][0].year

            # create a monthly covid case object for each iteration and then append it to the _monthly_covid_cases list attribute.
            monthly_covid_case = MonthlyCovidCases(monthly_cases, cumulative_cases, month, year)
            self._monthly_covid_cases.append(monthly_covid_case)
    
    def process_quarterly_cases(self) -> None:
        """Process Covid data into Quarters.
        
        Preconditions:
            - self._monthly_covid_cases != []
        """
        # Dictionary that holds dates in the form of year-quarter as a string. Each key has a value of a list of
        # Monthly Covid Case objects which represents every month in the respective year-quarter.. 
        dates_and_monthly_cases = {}
        
        for monthly_case in self._monthly_covid_cases:
            # Using the Quarters dictionary mapping from the utilities folder, we access the quarter a month
            # is in by passing in the month as an integer value. 
            quarter = QUARTERS[int(monthly_case.month)]
            year = monthly_case.year

            # Convert datetime object into a string used as keys for the dates_and_monthly_cases dictionary. 
            year_quarter = str(year) + '-' + str(quarter)

            # If the date is not in the dates_and_monthly_cases dictionary, intialize it with a list of a monthly case object.
            if year_quarter not in dates_and_monthly_cases:
                dates_and_monthly_cases[year_quarter] = [monthly_case]
            
            # If the date is already a key, add to it's list value with a monthly case object.
            else:
                dates_and_monthly_cases[year_quarter].append(monthly_case)
        
        for key in dates_and_monthly_cases:
            quarterly_cases = dates_and_monthly_cases[key]
            cumulative_cases = dates_and_monthly_cases[key][-1].cumulative_cases

            month = dates_and_monthly_cases[key][0].month
            quarter = QUARTERS[int(month)]

            quarterly_covid_cases = QuarterlyCovidCases(quarterly_cases, cumulative_cases, quarter, dates_and_monthly_cases[key][0].year)

            self._quarterly_covid_cases.append(quarterly_covid_cases)
