from typing import Any


class DataLoad:

    raw_data: Any
    file_path: str
    
    def __init__(self, raw_data: Any):
        """Initialize DataLoad class"""

    def load_data(self):
        """load raw data from file into raw_data"""
