from datetime import datetime

import ShipTrade


class MonthlyShipping:

    _ship_trades: list[ShipTrade]
    monthly_value: int
    month: datetime

    def __init__(self, month: datetime, ship_trades: list[ShipTrade]):
        self._ship_trades = ship_trades
        self.month = month
        self.monthly_value = 0

    def calculate_monthly_value(self) -> None:
        """Calculates total value of monthly trade"""
        self.monthly_value = sum([trade.value for trade in self._ship_trades])
