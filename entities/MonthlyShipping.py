"""CSC110 Final Project: Entities Monthly Shipping

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from datetime import datetime

from entities.ShipTrade import ShipTrade


class MonthlyShipping:
    """Shipments in a month"""

    _ship_trades: list[ShipTrade]
    monthly_value: int
    date: datetime

    def __init__(self, date: datetime, ship_trades: list[ShipTrade]):
        self._ship_trades = ship_trades
        self.date = date
        self.calculate_monthly_value()

    def calculate_monthly_value(self) -> None:
        """Calculates total value of monthly trade

        >>> st = [ShipTrade(datetime(2020, 4, 2), 200), ShipTrade(datetime(2020, 4, 5), 100)]
        >>> ms = MonthlyShipping(datetime(2020, 4, 1), st)
        >>> ms.monthly_value == 300
        True
        """
        self.monthly_value = sum([trade.value for trade in self._ship_trades])
