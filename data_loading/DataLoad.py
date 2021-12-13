"""CSC110 Final Project: Data Processing Process Covid Cases

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Clark Zhang, Danny Lu, Alex Balaria, Yue Fung Lee.
"""
from typing import Any


class DataLoad:
    """Loads data"""

    raw_data: Any
    file_path: str

    def __init__(self, file_path: str):
        """Initialize DataLoad class"""
        self.file_path = file_path

    def load_data(self):
        """load raw data from file into raw_data"""
        raise NotImplementedError
