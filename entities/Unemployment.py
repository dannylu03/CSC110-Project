from dataclasses import dataclass
import datetime as dt


@dataclass
class Unemployment:
    date: dt.datetime
    rate: float
