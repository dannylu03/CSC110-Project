from datetime import datetime
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases


class ProcessCovidCases:
    def __init__(self) -> None:
        self._monthly_covid_cases = []

    def process_monthly_cases(self, raw_covid_data: list[(str, str, int, int, int, int)]) -> None:
        cumulative_cases = 0

        # Maps year-month to list of daily cases
        date_to_cases = {}

        for data in raw_covid_data:
            date_reported = data[0]
            country_code = data[1]
            new_cases = data[2]
            cumulative_cases = data[3]
            new_deaths = data[4]
            cumulative_deaths = data[5]

            date = datetime.strptime(date_reported, 'Y-%m')
            day = datetime.strptime(date_reported, '%d')

            # 
            if date not in date_to_cases:
                date_to_cases[date] = [DailyCases(country_code, cumulative_cases, new_cases, day)]
            
            else:
                date_to_cases[date].append(DailyCases(country_code, cumulative_cases, new_cases, day))

        
        for month in date_to_cases:
            month_list_cases = date_to_cases[month]
            cumulative_cases = date_to_cases[month][-1]
            monthly_covid_case = MonthlyCovidCases(month_list_cases, cumulative_cases, month.month)
            self._monthly_covid_cases.append(monthly_covid_case)
