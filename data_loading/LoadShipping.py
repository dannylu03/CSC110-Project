import pandas as pd
from DataLoad import DataLoad

class LoadShipping(DataLoad):
    def __init__(self, file: str) -> None:
        DataLoad.__init__(file)
    
    def load_file(self) -> Dataframe:
        shipping_df = pd.read_csv(file)
        return shipping_df