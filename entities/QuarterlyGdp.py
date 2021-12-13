from dataclasses import dataclass


@dataclass
class QuarterlyGdp:
    """A dataclass for average GDP measured quarterly.

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


