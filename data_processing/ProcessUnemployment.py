from entities.MonthlyUnemployment import MonthlyUnemployment
from entities.QuarterlyUnemployment import QuarterlyUnemployment
from Utilities.Utils import QUARTERS


class ProcessUnemployment:
    """Process the raw data from LoadUnemployment"""

    def __init__(self) -> None:
        self._monthly_unemployment = []
        self._quarterly_unemployment = []

    def process_quarterly_unemployment(self, raw_unemployment_data: list[(str, int)]) -> None:
        """
            Processes raw data into months
        """
        # Create dict mapping year and quarter to list of MonthlyUnemployment
        date_to_list_monthly = {}

        # Populate the dictionary mapping
        for data in raw_unemployment_data:
            date_list = data[0].split('-')  # date is list of strings
            # the year and months from date_list from above
            year = int(date_list[0])
            month = int(date_list[1])
            quarter = QUARTERS[month]  # mapping the month to the different quarters in Utilities
            year_quarter = str(year) + '~' + str(quarter)
            unemployment_rate = data[1]

            # adding to date_to_list_monthly dictionary, mapping year_quarter to a MonthlyUnemployment object
            if year_quarter not in date_to_list_monthly:
                date_to_list_monthly[year_quarter] = [MonthlyUnemployment(month, year, unemployment_rate)]
            else:
                date_to_list_monthly[year_quarter].append(MonthlyUnemployment(month, year, unemployment_rate))

        # Create list of QuarterlyUnemployment objects
        for year_quarter in date_to_list_monthly:
            list_monthly = date_to_list_monthly[year_quarter]
            quarter = QUARTERS[list_monthly[0].month]
            year = list_monthly[0].year
            # appenging data to quarterly_unemployment
            self._quarterly_unemployment.append(QuarterlyUnemployment(list_monthly, year, quarter))
