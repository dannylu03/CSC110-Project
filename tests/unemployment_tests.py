from data_loading.LoadUnemployment import LoadUnemployment
from entities.QuarterlyUnemployment import QuarterlyUnemployment
from entities.MonthlyUnemployment import MonthlyUnemployment
from data_processing.ProcessUnemployment import ProcessUnemployment


def test_load_unemployment() -> None:
    file_path = '../data/LNS14000024.csv'
    load_unemployment = LoadUnemployment(file_path)
    loaded_data = load_unemployment.load_data()
    assert loaded_data[0] == ('1948-01-01', 3.0)
    assert loaded_data[-1] == ('2021-11-01', 4.0)


def quarterly_unemployment_sample() -> [QuarterlyUnemployment]:
    """Quarterly Unemployment Sample for testing."""
    monthly_unemploymentq1 = [MonthlyUnemployment(1, 1948, 3.0), MonthlyUnemployment(2, 1948, 3.3),
                              MonthlyUnemployment(3, 1948, 3.5)]
    monthly_unemploymentq2 = [MonthlyUnemployment(4, 1948, 3.5), MonthlyUnemployment(5, 1948, 3.3)]

    return [QuarterlyUnemployment(monthly_unemploymentq1, 1948, 1),
            QuarterlyUnemployment(monthly_unemploymentq2, 1948, 2)]


def test_processing_unemployment() -> None:
    raw_unemployment_data = [('1948-01-01', 3.0), ('1948-02-01', 3.3), ('1948-03-01', 3.5), ('1948-04-01', 3.5),
                             ('1948-05-01', 3.3)]

    process_unemployment_data = ProcessUnemployment()
    process_unemployment_data.process_quarterly_unemployment(raw_unemployment_data)
    actual = process_unemployment_data._quarterly_unemployment
    expected = quarterly_unemployment_sample()

    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i]._year == expected[i]._year
        assert actual[i]._quarter == expected[i]._quarter
        assert actual[i]._list_monthly == expected[i]._list_monthly
