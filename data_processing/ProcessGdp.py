"""CSC110 Final Project: Data Processing Process Gdp

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from entities.QuarterlyGdp import QuarterlyGdp


class ProcessGdp:
    """Processes the raw gdp data from LoadGdp"""

    quarterly_gdp: List[QuarterlyGdp]

    def __init__(self) -> None:
        self.quarterly_gdp = []

    def process_gdp(self, raw_gdp_data: list[(str, float)]) -> None:
        """Processes quarterly gdp data"""
        # discard any previous data
        self.quarterly_gdp = []
        for data in raw_gdp_data:
            split_data = data[0].split(' ')  # data[0] is string representation of date
            quarter = int(split_data[0][1])
            year = 2000 + int(split_data[1].split('\'')[1])
            self.quarterly_gdp.append(QuarterlyGdp(quarter, year, data[1]))
