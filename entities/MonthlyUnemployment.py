"""Insert module shit here"""
from dataclasses import dataclass


@dataclass
class MonthlyUnemployment:
    """Monthly unemployment rate in the US"""
    month: int
    year: int
    unemployment_rate: float
