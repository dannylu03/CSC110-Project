"""Insert module shit here"""
import datetime
from dataclasses import dataclass


@dataclass
class DailyCases:
    """Stats for covid cases in particular country on particular day"""
    country: str
    cumulative_cases: int
    new_cases: int
    date: datetime.datetime
