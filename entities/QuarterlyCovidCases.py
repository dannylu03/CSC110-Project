"""CSC110 Final Project: Entities Quarterly Covid Cases

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee."""
from entities.MonthlyCases import MonthlyCovidCases


class QuarterlyCovidCases:
    """Covid stats in a quarter
    
    Instance Attributes:
        - cumulative_cases: the total cumulated cases within the country
        - new_cases: the number of new cases
        - year: the year corresponding to the cases
        - month: the month corresponding to the cases

    Representation Invariants:
        - 0 < self.month < 13
    """
    def __init__(self, quarter_cases: list[MonthlyCovidCases], cumulative_cases: int, quarter: int, year: int) -> None:
        self._quarterly_cases = quarter_cases
        self._cumulative_cases = cumulative_cases
        self._quarter = quarter
        self._year = year

    #TODO: Delete redundant methods

    def calculate_average_daily_increase(self) -> float:
        """Return a float value of the average daily increase of this quarter instance. 
        """

        # Initialize accumulator which will be returned later
        average_daily_increase = 0.0

        # Initialize num_days as the length of this month object's list of daily covid cases
        num_days = len(self._month_list_cases)

        total_new_cases = 0

        for month in self._quarter_cases:
            for day in month:
                total_new_cases += day.new_cases
        
        average_daily_increase = total_new_cases / num_days
        return average_daily_increase

    def calculate_total_quarterly_increase(self) -> float:
        """Return the total increase in cumulative cases this month"""
        first_day_cases = self._quarterly_cases[0]._monthly_list_cases[0].cumulative_cases

        last_day_cases = self._quarterly_cases[-1]._monthly_list_cases[-1].cumulative_cases


        return last_day_cases - first_day_cases
