import datetime
from dataclasses import dataclass


@dataclass
class ShipTrade:
    """A metric that is taken from the shipping data set.

    Instance Attributes:
        - date: the date of which the ship trade occured
        - value: the monetary value of the ship trade of that day

    Representation Invariants:
        - self.value > 0
    """
    date: datetime
    value: int
