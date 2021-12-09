import pandas as pd
import plotly.express as px
import datetime as dt

covid_df = pd.read_csv('./data/WHO-COVID-19-global-data.csv')

# Extract the columns we need
covid_df = covid_df[['Date_reported', 'Country_code', 'New_cases', 'Cumulative_cases']]

start = dt.datetime(2020, 1, 3)
end = dt.datetime.now()

# Conditional statemnt to filter the covid_df for only data on the US
cond = (covid_df["Country_code"] == "US")

us_covid_df = covid_df.loc[cond]

# Accumulators
days = 0 
month_average = 0
monthly_average = []

dates = us_covid_df["Date_reported"]
new_cases = us_covid_df["New_cases"]

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