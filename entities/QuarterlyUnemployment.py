"""CSC110 Final Project: Entities Quarterly Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from entities.MonthlyUnemployment import MonthlyUnemployment


class QuarterlyUnemployment:
    """Quarterly unemployment rate in the US
    Instance Attributes:
        - _list_monthly: list of 
        - quarter: the quarter corresponding to the unemployment rate
        - year: the year corresponding to the unemployment rate

    Representation Invariants:
        - 0 < self.month < 13
    """

    def __init__(self, list_monthly: list[MonthlyUnemployment], quarter: int, year: int):
        """Initialize a new quarterly unemployment model"""
        self._list_monthly = list_monthly
        self._quarter = quarter
        self._year = year

    def get_year(self) -> int:
        """Return the object's year."""
        return self._year
    
    def get_quarter(self) -> int:
        """Return the object's quarter."""
        return self._quarter
    
    def calculate_average_quarterly_unemployment(self) -> float:
        """Returns the average unemployment rate for this quarter"""
        total = sum([monthly_unemployment.unemployment_rate for monthly_unemployment in self._list_monthly])
        num_months = 3
        return total / num_months
