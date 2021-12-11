import datetime
from dataclasses import dataclass

@dataclass
class Daily_cases:
    day: datetime.datetime
    num_cases: int
