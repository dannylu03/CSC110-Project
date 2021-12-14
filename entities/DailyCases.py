"""CSC110 Final Project: Entities Daily Cases

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from dataclasses import dataclass


@dataclass
class DailyCases:
    """Daily covid cases stats

    Instance Attributes:
        - country: the country corresponding to the COVID cases
        - cumulative_cases: the total cumulated cases within the country
        - new_cases: the number of new cases
        - year: the year corresponding to the cases
        - month: the month corresponding to the cases

    Representation Invariants:
        - self.country != ''
        - 0 < self.month < 13
    """
    country: str
    cumulative_cases: int
    new_cases: int
    year: int
    month: int
