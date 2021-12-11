import ShipTrade


class Shipping:

    _ship_trades: list[ShipTrade]
    monthly_value: int
    month: int

    def __init__(self, ship_trades: list[ShipTrade]):
        self._ship_trades = ship_trades
        self.monthly_value = 0

    def calculate_monthly_value(self) -> None:
        self.monthly_value = sum([trade.value for trade in self._ship_trades])
