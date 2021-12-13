"""CSC110 Final Project: Entities Quarterly GDP

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from dataclasses import dataclass


@dataclass
class QuarterlyGdp:
    """GDP growth of US in a quarter"""
    quarter: int
    year: int
    growth: float


