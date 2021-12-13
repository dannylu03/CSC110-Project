"""CSC110 Final Project: Entities Monthly Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from dataclasses import dataclass


@dataclass
class MonthlyUnemployment:
    """Monthly unemployment rate in the US

    Instance Attributes:
        - month: the month in the year corresponded to the the unemployment rate
        - year: the year corresponded to the unemployment
        - unemployment_rate: unemployment rate measured in percentage

    Representation Invariants:
        - 0 < self.month < 13
    """
    month: int
    year: int
    unemployment_rate: float
