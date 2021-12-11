from datetime import datetime

from entities.ShipTrade import ShipTrade
from entities.MonthlyShipping import MonthlyShipping


class ProcessShippingData:

    _monthly_ship_trades: []

    def __init__(self):
        self._monthly_ship_trades = []

    def process_monthly_trades(self, raw_ship_data: list[(int, int, int)]) -> None:
        """
            Processes maritime trade data so
        """
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
