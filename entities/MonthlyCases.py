import datetime as dt
from DailyCases import Daily_cases

class MonthlyCovidCases:
    """
    """

    def __init__(self, daily_covid_cases: list[Daily_cases], cumulative_covid_cases: int, month: dt.datetime) -> None:
        """Initialize a new ????
        """
        self._daily_covid_cases = []
        self._cumulative_covid_cases = cumulative_covid_cases
        self._month = month
    
    def calculate_average_daily_increase(self) -> float:
        """Return a float value of the average daily increase of this month instance. 
        """

        # Initialize accumulator which will be returned later
        average_daily_increase = 0.0

        # Initialize num_days as the length of this month object's list of daily covid cases
        num_days = len(self._daily_covid_cases)
        
        # Iterate from 1 to the number of days in instance month, and calculate the percent increase 
        # from that day and the previous day.
        for i in range(1, num_days):
            average_daily_increase += (self._daily_covid_cases[i].new_cases - self._daily_covid_cases[i-1]) / \
                                      self._daily_covid_cases[i - 1] * 100
        
        average_daily_increase = average_daily_increase / num_days
        return average_daily_increase

    def calculate_total_monthly_increase(self) -> float:
        """Return a float value of the cumulative increase in covid cases of this month instance.
        """
        num_days = len(self._daily_covid_cases)

        return self.calculate_average_daily_increase() * num_days
