"""Insert Module shit here
"""
from datetime import datetime
from DailyCases import DailyCases


class MonthlyCovidCases:
    """Contains methods to calculate stats for covid cases in a month
    """

    def __init__(self, monthly_cases: list[DailyCases], cumulative_cases: int, month: int, year: int) -> None:
        """Initialize a new ????
        """
        self._monthly_cases = monthly_cases
        self._cumulative_cases = cumulative_cases
        self._month = month
        self._year = year
    
    def calculate_average_daily_increase(self) -> float:
        """Return a float value of the average daily increase of this month instance. 
        """

        # Initialize accumulator which will be returned later
        average_daily_increase = 0.0

        # Initialize num_days as the length of this month object's list of daily covid cases
        num_days = len(self._monthly_cases)

        total_new_cases = sum([d.new_cases for d in self._monthly_cases])
        
        average_daily_increase = total_new_cases / num_days
        return average_daily_increase

    def calculate_total_monthly_increase(self) -> float:
        """Return the total increase in cumulative cases this month"""
        last_day = len(self._monthly_cases) - 1
        last_day_cases = self._monthly_cases[last_day].cumulative_cases
        first_day_cases = self._monthly_cases[0].cumulative_cases

        return last_day_cases - first_day_cases
