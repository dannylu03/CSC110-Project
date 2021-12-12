from datetime import datetime

from entities.Unemployment import Unemployment


class ProcessUnemployment:
    """Process the raw data from LoadUnemployment"""
    _monthly_ship_trades: []

    def __init__(self):
        self._monthly_unemployment = []

    def process_monthly_unemployment(self, raw_unemployment_data: list[(str, int)]) -> None:
        """
            Processes raw data into months
        """
        for data in raw_unemployment_data:
            date_reported = data[0]
            unemployment_rate = data[1]
            month = datetime.strptime(date_reported, '%m')
            self._monthly_unemployment.append(Unemployment(month, unemployment_rate))
