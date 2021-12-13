"""CSC110 Final Project: Data Loading: Load Shipping

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from data_loading.DataLoad import DataLoad
import csv


class LoadShipping(DataLoad):
    """Load Shipping data"""

    def __init__(self, file_path: str):
        """Initializes LoadShipping data class"""
        super().__init__(file_path)
        print(file_path)
        self.raw_data = []

    def load_data(self) -> list[(int, int, int)]:
        """ Loads data from provided file path


        """
        with open(self.file_path) as raw_shipping_file:

            raw_file_data = csv.reader(raw_shipping_file)
            # skips header row
            next(raw_file_data)
            for row in raw_file_data:
                # Appends raw_data with relevant entries from the data set
                if int(row[-1]) > 2010:
                    self.raw_data.append((int(row[5]), int(row[-2]), int(row[-1])))
        return self.raw_data

