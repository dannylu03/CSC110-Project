from entities.MonthlyUnemployment import MonthlyUnemployment
from entities.QuarterlyUnemployment import QuarterlyUnemployment
from Utilities.Utils import QUARTERS


class ProcessUnemployment:
    """Process the raw data from LoadUnemployment"""
    _monthly_ship_trades: []

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
            date = data[0]
            quarter = QUARTERS[data.date.month]
            year = data.date.year
            year_quarter = str(year) + '~' + str(quarter)
            unemployment_rate = data[1]

            if year_quarter not in date_to_list_monthly:
                date_to_list_monthly[year_quarter] = [MonthlyUnemployment(date, unemployment_rate)]
            else:
                date_to_list_monthly[year_quarter].append(MonthlyUnemployment(date, unemployment_rate))

        # Create list of QuarterlyUnemployment objects
        for key in date_to_list_monthly:
            list_monthly = date_to_list_monthly[key]
            quarter = QUARTERS[date_to_list_monthly[key][0].date.month]
            year = date_to_list_monthly[key][0].date.year
            self._quarterly_unemployment.append(QuarterlyUnemployment(list_monthly, quarter, year))
