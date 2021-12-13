from data_loading import LoadCovidCases
from entities.QuarterlyCovidCases import QuarterlyCovidCases
from entities.MonthlyCases import MonthlyCovidCases
from entities.DailyCases import DailyCases
from data_processing.ProcessCovidCases import ProcessCovidCases


def test_load_covid() -> None:
    file_path = '../data/WHO-COVID-19-global-data.csv'
    load_covid = LoadCovidCases.LoadCovidCases(file_path)
    loaded_data = load_covid.load_data()

    assert loaded_data[0] == ('2020-01-03', 'AF', 0, 0)
    assert loaded_data[-1] == ('2021-12-09', 'ZW', 4996, 150628)


def test_processing_covid_data() -> None:
    raw_covid_data = [('2021-12-09', 'TZ', 0, 26309), ('2020-01-03', 'US', 0, 0), ('2020-01-04', 'US', 0, 0), \
                      ('2020-01-05', 'US', 0, 0), ('2020-01-06', 'US', 0, 0)]
    process_covid_data = ProcessCovidCases()
    process_covid_data.process_monthly_cases(raw_covid_data)
    process_covid_data.process_quarterly_cases()
    actual = process_covid_data._quarterly_covid_cases
    a = DailyCases('US', 0, 0, 2020, 1)
    b = DailyCases('US', 0, 0, 2020, 1)
    c = DailyCases('US', 0, 0, 2020, 1)
    d = DailyCases('US', 0, 0, 2020, 1)
    list_monthly_cases = [MonthlyCovidCases([a, b, c, d], 0, 2020, 1)]
    list_quarterly_cases = [QuarterlyCovidCases(list_monthly_cases, 0, 1, 2020)]
    expected = list_quarterly_cases

    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i]._year == expected[i]._year
        assert actual[i]._quarter == expected[i]._quarter


