from datetime import datetime
from MonthlyShipping import MonthlyShipping
import ShipTrade


class QuarterlyShipping:

    _monthly_ship_trades: [MonthlyShipping]
    quarterly_value: int
    quarter: int
    year: int

    def __init__(self, quarter: int, year: int, ship_trades: list[MonthlyShipping]):
        self._ship_trades = ship_trades
        self.quarter = quarter
        self.year = year

    def calculate_quarterly_value(self) -> None:
        """Calculates total value of quarterly trade"""
        self.quarterly_value = sum([trade.monthly_value for trade in self._monthly_ship_trades])