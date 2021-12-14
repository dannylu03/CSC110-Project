"""CSC110 Final Project: Entities Quarterly Shipping

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from datetime import datetime
from entities.MonthlyShipping import MonthlyShipping
from entities.ShipTrade import ShipTrade


class QuarterlyShipping:
    """Shipments in a quarter

    Representation Invariants:
        - 0 < self.quarter < 5

    Private Instance Attributes:
        - _monthly_ship_trades: a list of Monthly Shipping Data

    Instance Attributes:
        - _monthy_ship_trades: list of MonthlyShipping objects
        - quarterly_value: the total shipment value in the quarter
        - quarter: quarter of the year
        - year: the year that corresponding to the value
    """

    _monthly_ship_trades: list[MonthlyShipping]
    _quarterly_value: int
    _quarter: int
    _year: int

    def __init__(self, quarter: int, year: int, ship_trades: list[MonthlyShipping]) -> None:
        self._monthly_ship_trades = ship_trades
        self._quarter = quarter
        self._year = year
        self.calculate_quarterly_value()

    def get_monthly_ship_trades(self) -> list[MonthlyShipping]:
        """Return the object's monthly ship trades."""
        return self._monthly_ship_trades
    
    def get_quarter(self) -> int:
        """Return the object's quarter."""
        return self._quarter
    
    def get_year(self) -> int:
        """Return the object's year."""
        return self._year

    def calculate_quarterly_value(self) -> None:
        """Calculates total value of quarterly trade

        >>> st1 = [ShipTrade(datetime(2020, 4, 2), 200), ShipTrade(datetime(2020, 4, 5), 100)]
        >>> st2 = [ShipTrade(datetime(2020, 5, 2), 100), ShipTrade(datetime(2020, 5, 5), 400)]
        >>> ms = [MonthlyShipping(datetime(2020, 4, 1), st1), MonthlyShipping(datetime(2020, 4, 1), st2)]
        >>> qs = QuarterlyShipping(2, 2020, ms)
        >>> qs.quarterly_value
        800
        """

        self.quarterly_value = sum([trade.monthly_value for trade in self._monthly_ship_trades])
