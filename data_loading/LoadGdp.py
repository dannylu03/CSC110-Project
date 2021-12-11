from data_loading.DataLoad import DataLoad
import csv


class LoadGdp(DataLoad):

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.raw_data = []

    def load_data(self) -> list[(str, float)]:
        """ Loads data from provided file path


         """
        with open(self.file_path, 'r') as raw_gdp_data:
            raw_file_data = csv.reader(raw_gdp_data)
            # Skips header row
            next(raw_file_data)
            for row in raw_file_data:
                self.raw_data.append((row[0], float(row[1])))
        return self.raw_data
