"""CSC110 Final Project: Entities Monthly Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from dataclasses import dataclass


@dataclass
class MonthlyUnemployment:
    """Monthly unemployment rate in the US"""
    month: int
    year: int
    unemployment_rate: float
