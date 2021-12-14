"""CSC110 Final Project: Entities Monthly Shipping

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from datetime import datetime

from entities.ShipTrade import ShipTrade


class MonthlyShipping:
    """A dataclass for the monthly shipping data.

    Private Instance Attributes:
        - _ship_trades: a list of ShipTrade data, represents all the shipments in the month

    Instance Attributes:
        - monthly_value: the monthly value from the sum of the trade_value
        - date: the date of which the trade happened

    """
    _ship_trades: list[ShipTrade]
    _monthly_value: int
    _date: datetime

    def __init__(self, date: datetime, ship_trades: list[ShipTrade]) -> None:
        self._ship_trades = ship_trades
        self.date = date
        self.calculate_monthly_value()

    def get_ship_trades(self) -> list[ShipTrade]:
        """Return the object's ship trades."""
        return self._ship_trades

    def get_monthly_value(self) -> int:
        """Return the object's monthly value."""
        return self._monthly_value

    def get_date(self) -> datetime:
        """Return the object's date."""
        return self._date

    def calculate_monthly_value(self) -> None:
        """Calculates total value of monthly trade

        >>> st = [ShipTrade(datetime(2020, 4, 2), 200), ShipTrade(datetime(2020, 4, 5), 100)]
        >>> ms = MonthlyShipping(datetime(2020, 4, 1), st)
        >>> ms.monthly_value == 300
        True
        """
        self.monthly_value = sum([trade.value for trade in self._ship_trades])
