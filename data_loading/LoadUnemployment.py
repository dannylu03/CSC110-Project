"""CSC110 Final Project: Data Loading: Load Unemployment

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from data_loading.DataLoad import DataLoad
import csv


class LoadUnemployment(DataLoad):
    """Load unemployment data"""

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.raw_data = []

    def load_data(self) -> list[(str, float)]:
        """ Loads data from provided file path


         """
        with open(self.file_path, 'r') as raw_unemployment_data:
            raw_file_data = csv.reader(raw_unemployment_data)
            # skips header row
            next(raw_file_data)
            for row in raw_file_data:
                self.raw_data.append((row[0], float(row[1])))
        return self.raw_data
