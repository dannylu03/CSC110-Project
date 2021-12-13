from MonthlyUnemployment import MonthlyUnemployment


class QuarterlyUnemployment:
    """Unemployment rate every quarter
    """

    def __init__(self, list_monthly: list[MonthlyUnemployment], quarter, year):
        self._list_monthly = list_monthly
        self._year = year
        self._quarter = quarter


def calculate_average_quarterly_unemployment(self) -> None:
    """Returns the average unemployment rate for this quarter"""
    total = sum([monthly_unemployment.unemployment_rate for monthly_unemployment in self._quarter_unemployment])
    num_months = 3
    return total / num_months
