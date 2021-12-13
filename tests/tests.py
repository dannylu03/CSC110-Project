from datetime import datetime
from data_loading import LoadShipping
from data_processing import ProcessShippingData
from entities.MonthlyShipping import MonthlyShipping
from entities.QuarterlyShipping import QuarterlyShipping
from entities.ShipTrade import ShipTrade
from data_loading.LoadGdp import LoadGdp
from data_processing.ProcessGdp import ProcessGdp
from entities.QuarterlyGdp import QuarterlyGdp
from Utilities import Utils


def quarterly_shipping_sample() -> [QuarterlyShipping]:
    monthly_trades_q1 = [MonthlyShipping(datetime(2013, 2, 1), [ShipTrade(datetime(2013, 2, 1), 500)])]
    monthly_trades_q2 = [MonthlyShipping(datetime(2013, 12, 1), [ShipTrade(datetime(2013, 12, 1), 100)]),
                         MonthlyShipping(datetime(2013, 11, 1), [ShipTrade(datetime(2013, 11, 1), 200)])]
    monthly_trades_q3 = [MonthlyShipping(datetime(2021, 1, 1), [ShipTrade(datetime(2021, 1, 1), 400)]),
                         MonthlyShipping(datetime(2021, 2, 1), [ShipTrade(datetime(2021, 2, 1), 600)])]
    quarterly_shipping = [QuarterlyShipping(1, 2013, monthly_trades_q1), QuarterlyShipping(4, 2013, monthly_trades_q2),
                          QuarterlyShipping(1, 2021, monthly_trades_q3)]
    return quarterly_shipping


def test_load_shipping() -> None:
    file_path = '../data/ship_data.csv'
    load_shipping = LoadShipping.LoadShipping(file_path)
    loaded_data = load_shipping.load_data()
    assert loaded_data[0] == (29818, 1, 2011)
    assert loaded_data[-1] == (646528, 1, 2018)


def test_processing_shipping_data() -> None:
    raw_ship_data = [(100, 12, 2013), (200, 11, 2013), (500, 2, 2013), (400, 1, 2021), (600, 2, 2021)]
    expected = quarterly_shipping_sample()
    process_shipping_data = ProcessShippingData.ProcessShippingData()
    process_shipping_data.process_monthly_trades(raw_ship_data)
    actual = process_shipping_data.process_quarterly_trades()
    Utils.quarterly_shipping_sort(actual)
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i].year == expected[i].year
        assert actual[i].quarter == expected[i].quarter
        assert actual[i].quarterly_value == expected[i].quarterly_value


def test_load_gdp() -> None:
    file_path = '../data/statistic_id188185_real-gdp-growth-by-quarter-in-the-us-2011-2021.xlsx'
    load_gdp = LoadGdp(file_path)
    loaded_gdp = load_gdp.load_data()
    assert loaded_gdp[0] == ('Q1 \'11', -1.0)
    assert loaded_gdp[-1] == ('Q3 \'21', 2.1)


def test_process_gdp() -> None:
    raw_gdp_data = [('Q1 \'11', -1.0), ('Q2 \'13', 1.2), ('Q2 \'18', 5.1), ('Q3 \'21', 2.1)]
    expected = [QuarterlyGdp(1, 2011, -1.0), QuarterlyGdp(2, 2013, 1.2), QuarterlyGdp(2, 2018, 5.1), QuarterlyGdp(3, 2021, 2.1)]
    processing_gdp = ProcessGdp()
    processing_gdp.process_gdp(raw_gdp_data)
    actual = processing_gdp.quarterly_gdp
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i].quarter == expected[i].quarter
        assert actual[i].year == expected[i].year
        assert actual[i].growth == expected[i].growth
