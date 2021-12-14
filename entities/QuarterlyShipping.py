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

    _monthly_ship_trades: List[MonthlyShipping]
    quarterly_value: int
    quarter: int
    year: int

    def __init__(self, quarter: int, year: int, ship_trades: list[MonthlyShipping]) -> None:
        self._monthly_ship_trades = ship_trades
        self.quarter = quarter
        self.year = year
        self.calculate_quarterly_value()

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
