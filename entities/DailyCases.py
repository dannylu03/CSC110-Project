"""CSC110 Final Project: Entities Daily Cases

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee."""
from dataclasses import dataclass


@dataclass
class DailyCases:
    """Daily covid cases stats"""
    country: str
    cumulative_cases: int
    new_cases: int
    year: int
    month: int
