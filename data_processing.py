"""CSC110 Fall 2021 Project

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

You may create some additional helper functions to help break up your code into smaller parts.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Danny Lu, Alex Balaria, Yue Fung Lee, and Clark Zhang.
"""

import pandas as pd
from pandas.core.frame import DataFrame
import plotly.express as px
import datetime as dt
from dataclasses import dataclass

covid_df = pd.read_csv('./data/WHO-COVID-19-global-data.csv')

# Extract the columns we need
covid_df = covid_df[['Date_reported', 'Country_code', 'New_cases', 'Cumulative_cases']]

start = dt.datetime(2020, 1, 3)
end = dt.datetime.now()a

# Conditional statemnt to filter the covid_df for only data on the US
cond = (covid_df["Country_code"] == "US")

us_covid_df = covid_df.loc[cond]

# Accumulators
days = 0 
month_average = 0
monthly_average = []

dates = us_covid_df["Date_reported"]
new_cases = us_covid_df["New_cases"]

# Loading data
@dataclass
class LoadData:
    file: str

    def read_csv(self, file: str) -> DataFrame:
        raise NotImplementedError


class LoadCovidData(LoadData):
    def __init__(self) -> None:
        pass


# Covid Cases


class DailyCovidCases:
    def __init__(self, day: str, new_cases: int) -> None:
        self._day = day
        self._new_cases = new_cases






for i in range(len(dates)):
    if i > 1:
      if dates[i].month != dates[i - 1].month:
          month_average = month_average / days
          monthly_average.append(month_average)
          days, month_average = 0

    try: 
      monthly_average += new_cases.iloc[i]
      days += 1
    
    except:
      raise KeyError



# fig = px.scatter(us_covid_df, x = "Date_reported", y = monthly_average)
# fig.show()



# if __name__ == "__main__":
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