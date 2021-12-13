"""CSC110 Final Project: Entities Quarterly Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from entities.MonthlyUnemployment import MonthlyUnemployment


class QuarterlyUnemployment:
    """Quarterly unemployment rate in the US"""

    def __init__(self, list_monthly: list[MonthlyUnemployment], quarter, year):
        self._list_monthly = list_monthly
        self._quarter = quarter
        self._year = year

    def calculate_average_quarterly_unemployment(self) -> float:
        """Returns the average unemployment rate for this quarter"""
        total = sum([monthly_unemployment.unemployment_rate for monthly_unemployment in self._list_monthly])
        num_months = 3
        return total / num_months
