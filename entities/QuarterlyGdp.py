"""CSC110 Final Project: Entities Quarterly GDP

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from dataclasses import dataclass


@dataclass
class QuarterlyGdp:
    """GDP growth of US in a quarter

    Instance Attributes:
        - quarter: the quarter of the specific year
        - year: year that corresponds so the GDP growth
        - growth: the growth of in GDP

    Representation Invariants:
        - 1 < self.quarter < 5
    """
    quarter: int
    year: int
    growth: float


