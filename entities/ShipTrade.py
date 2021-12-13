"""CSC110 Final Project: Entities ShipTrade

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
import datetime
from dataclasses import dataclass


@dataclass
class ShipTrade:
    """A shipment across a US border"""
    date: datetime
    value: int
