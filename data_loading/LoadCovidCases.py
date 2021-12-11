import pandas as pd
from DataLoad import DataLoad

class LoadCovidCases(DataLoad):
    def __init__(self, file: str) -> None:
        DataLoad.__init__(file)
    
    def load_file(self) -> Dataframe:
        covid_cases_df = pd.read_csv(file)
        return covid_cases_df