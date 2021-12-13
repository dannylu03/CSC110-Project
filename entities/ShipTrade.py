"""CSC110 Final Project: Entities ShipTrade

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
import datetime
from dataclasses import dataclass


@dataclass
class ShipTrade:
    """A shipment metric that is taken from the shipping data set.

    Instance Attributes:
        - date: the date of which the ship trade occured
        - value: the monetary value of the ship trade of that day

    Representation Invariants:
        - self.value > 0
    """
    date: datetime
    value: int
