import csv
from typing import Any
from data_loading.DataLoad import DataLoad


class LoadShipping(DataLoad):

    def __init__(self, raw_data: Any):
        super().__init__(raw_data)

    def load_data(self):
        """Loads csv data into raw_data"""