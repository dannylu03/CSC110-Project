from dataclasses import dataclass


@dataclass
class QuarterlyGdp:

    quarter: int
    year: int
    growth: float


