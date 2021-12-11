import pandas as pd
from DataLoad import DataLoad

class LoadGDP(DataLoad):
    def __init__(self, file: str) -> None:
        DataLoad.__init__(file)
    
    def load_file(self) -> Dataframe:
        gdp_df = pd.read_csv(file)
        return gdp_df