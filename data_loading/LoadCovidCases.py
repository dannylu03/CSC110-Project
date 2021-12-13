"""CSC110 Final Project: Data Loading: Load Covid Cases

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from data_loading.DataLoad import DataLoad
import csv


class LoadCovidCases(DataLoad):
    """Load covid data"""
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        self.raw_data = []

    def load_data(self) -> list[(str, str, int, int)]:
        """ Loads data from provided file path


         """
        with open(self.file_path, 'r') as raw_covid_data:
            raw_file_data = csv.reader(raw_covid_data)
            # skips header row
            next(raw_file_data)
            for row in raw_file_data:
                self.raw_data.append((row[0], row[1], int(row[-4]), int(row[-3])))
        return self.raw_data
