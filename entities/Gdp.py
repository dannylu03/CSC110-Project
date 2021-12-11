import datetime
from dataclasses import dataclass

@dataclass
class Gdp:
    gdp: float
    month: datetime.datetime
