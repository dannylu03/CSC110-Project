"""Insert module shit here"""
from dataclasses import dataclass
import datetime


@dataclass
class Unemployment:
    """Monthly unemployment rate in the US"""
    month: datetime.datetime
    unemployment_rate: float
