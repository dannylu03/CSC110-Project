from datetime import datetime

from entities.ShipTrade import ShipTrade
from entities.MonthlyShipping import MonthlyShipping
from entities.QuarterlyShipping import QuarterlyShipping
from Utilities.Utils import QUARTERS


class ProcessShippingData:

    _monthly_ship_trades: [MonthlyShipping]

    def __init__(self):
        self._monthly_ship_trades = []
        self._quarterly_ship_trades = []

    def process_monthly_trades(self, raw_ship_data: list[(int, int, int)]) -> None:
        """
            Processes maritime trade data so
        """
        # discard any previous data
        self._monthly_ship_trades = []
        trades_and_dates = {}
        # Maps months to trades
        for data in raw_ship_data:
            date = datetime(data[1], data[2], 1)
            if date in trades_and_dates:
                trades_and_dates[date].append(ShipTrade(date, data[0]))
            else:
                trades_and_dates[date] = [ShipTrade(date, data[0])]
        # Restructures dictionary oof months and trades into concrete MonthlyShipping class
        for date in trades_and_dates:
            monthly_shipping = MonthlyShipping(date, trades_and_dates[date])
            monthly_shipping.calculate_monthly_value()
            self._monthly_ship_trades.append(monthly_shipping)

    def process_quarterly_trades(self) -> None:
        """
            Process Maritime data into Quarters
        """
        years_and_quarters = {}
        for monthly_trade in self._monthly_ship_trades:
            quarter = QUARTERS[monthly_trade.date.month]
            year = monthly_trade.date.year
            # Code for quarter and year so it can be used as a dictionary key
            code = str(quarter) + str(year)
            if code in years_and_quarters:
                years_and_quarters[code].append(monthly_trade)
            else:
                years_and_quarters[code] = [monthly_trade]

        for quarter in years_and_quarters:
            quarter = QUARTERS[years_and_quarters[quarter][0].date.month]
            year = years_and_quarters[quarter][0].date.month
            quarterly_shipping = QuarterlyShipping(quarter, year, years_and_quarters[quarter])
            self._quarterly_ship_trades.append(quarterly_shipping)



