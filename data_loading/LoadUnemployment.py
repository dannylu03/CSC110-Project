import pandas as pd
from DataLoad import DataLoad

class LoadUnemployment(DataLoad):
    def __init__(self, file: str) -> None:
        DataLoad.__init__(file)
    
    def load_file(self) -> Dataframe:
        unemployment_df = pd.read_csv(file)
        return unemployment_df