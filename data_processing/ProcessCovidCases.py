from datetime import datetime
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases


class ProcessCovidCases:
    def __init__(self) -> None:
        self._monthly_covid_cases = []

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

            # Convert the date reported value from a string into a datetime object.
            date = datetime.strptime(date_reported, 'Y-%m')

            # Get the day value for creating daily case instances.
            day = datetime.strptime(date_reported, '%d')

            # If the date is not in the dictionary, intialize it with a list of a daily case object.
            if date not in date_to_cases:
                date_to_cases[date] = [DailyCases(country_code, cumulative_cases, new_cases, day)]
            
            # If the date is already a key, add to it's list value with a daily case object.
            else:
                date_to_cases[date].append(DailyCases(country_code, cumulative_cases, new_cases, day))

        
        # Iterate through every key in the date_to_cases dictionary
        for month in date_to_cases:
            month_list_cases = date_to_cases[month]
            cumulative_cases = date_to_cases[month][-1]
            
            # create a monthly covid case object for each iteration and then append it to the _monthly_covid_cases list attribute.
            monthly_covid_case = MonthlyCovidCases(month_list_cases, cumulative_cases, month.month)
            self._monthly_covid_cases.append(monthly_covid_case)
