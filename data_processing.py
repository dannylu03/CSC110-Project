import pandas as pd
import plotly.express as px
import datetime as dt

covid_df = pd.read_csv('./data/WHO-COVID-19-global-data.csv')

# Extract the columns we need
covid_df = covid_df[['Date_reported', 'Country_code', 'New_cases', 'Cumulative_cases']]

start = dt.datetime(2020, 1, 3)
end = dt.datetime.now()






if __name__ == "__main__":
  # import python_ta

  #   python_ta.check_all(config={
  #     'extra-imports': [],  # the names (strs) of imported modules
  #     'allowed-io': [],     # the names (strs) of functions that call print/open/input
  #     'max-line-length': 100,
  #     'disable': ['R1705', 'C0200']
  #   })

  #   import python_ta.contracts
  #   python_ta.contracts.check_all_contracts()

  #   import doctest
  #   doctest.testmod()