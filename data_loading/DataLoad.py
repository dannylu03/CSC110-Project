from typing import Any


class DataLoad:

    raw_data: Any
    file_path: str

    def __init__(self, file_path: str):
        """Initialize DataLoad class"""
        self.file_path = file_path

    def load_data(self):
        """load raw data from file into raw_data"""
