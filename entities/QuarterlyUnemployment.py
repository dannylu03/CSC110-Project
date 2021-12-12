from MonthlyUnemployment import MonthlyUnemployment


class QuarterlyUnemployment:
    """Unemployment rate every quarter
    """
    _quarter: int
    _unemployment_rate: int
    _quarter_unemployment: list[MonthlyUnemployment]

    def __init__(self, quarter_unemployment: list[MonthlyUnemployment], quarter, unemployment_rate):
        self._quarter_unemployment = quarter_unemployment
        self._quarter = quarter
        self._unemployment_rate = unemployment_rate


def calculate_average_quarterly_unemployment(self) -> None:
    """Returns the average unemployment rate for this quarter"""
    total = sum([monthly_unemployment.unemployment_rate for monthly_unemployment in self._quarter_unemployment])
    num_months = 3
    return total / num_months
