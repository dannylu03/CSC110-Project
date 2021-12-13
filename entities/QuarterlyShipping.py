from datetime import datetime
from entities.MonthlyShipping import MonthlyShipping
from entities.ShipTrade import ShipTrade


class QuarterlyShipping:
    """A shipping model that contains the different entities (monthly_ship_trades), quarterly_value,
     quarter and year.

    Representation Invariants:
        - 0 < self.quarter < 5

    Private Instance Attributes:
        - _monthly_ship_trades: a list of Monthly Shipping Data. This represents all of the shipping
            data by month.

    Instance Attributes:
        - quarterly_value: the average of a certain quarter within a certain year.
        - quarter: quarter of the year
        - year: the year that corresponding to the value
    """

    _monthly_ship_trades: [MonthlyShipping]
    quarterly_value: int
    quarter: int
    year: int

    def __init__(self, quarter: int, year: int, ship_trades: list[MonthlyShipping]):
        self._monthly_ship_trades = ship_trades
        self.quarter = quarter
        self.year = year
        self.calculate_quarterly_value()

    def calculate_quarterly_value(self) -> None:
        """Calculates total value of quarterly trade

        >>> st1 = [ShipTrade(datetime(2020, 4, 2), 200), ShipTrade(datetime(2020, 4, 5), 100)]
        >>> st2 = [ShipTrade(datetime(2020, 5, 2), 100), ShipTrade(datetime(2020, 5, 5), 400)]
        >>> ms = [MonthlyShipping(datetime(2020, 4, 1), st1), MonthlyShipping(datetime(2020, 4, 1), st2)]
        >>> qs = QuarterlyShipping(2, 2020, ms)
        >>> qs.quarterly_value
        800
        """

        self.quarterly_value = sum([trade.monthly_value for trade in self._monthly_ship_trades])
