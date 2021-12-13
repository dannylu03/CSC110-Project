from data_loading.DataLoad import DataLoad
import openpyxl


class LoadGdp(DataLoad):

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.raw_data = []

    def load_data(self) -> list[(str, float)]:
        """
        Loads data from provided file path

        Preconditions:
            - self.file_path != ''
        """
        # opens excel file
        sheets = openpyxl.open(self.file_path)
        # changes to relevant sheet
        sheet_data = sheets['Data']
        # skips first 6 rows as they hold irrelevant or no dataa
        i = 6
        # reads cells while they contain relevant values
        while sheet_data.cell(i, 2).value is not None:
            self.raw_data.append((sheet_data.cell(i, 2).value, float(sheet_data.cell(i, 3).value)))
            i += 1

        return self.raw_data
