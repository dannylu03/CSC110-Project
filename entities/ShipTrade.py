import datetime
from dataclasses import dataclass


@dataclass
class ShipTrade:
    date: datetime
    value: int
