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
            # filter irrelevant data based on year
            if data[2] > 2010:
                date = datetime(data[2], data[1], 1)
                # adds trades to corresponding months
                if date in trades_and_dates:
                    trades_and_dates[date].append(ShipTrade(date, data[0]))
                else:
                    trades_and_dates[date] = [ShipTrade(date, data[0])]
        # Restructures dictionary of months and trades into a list instances of MonthlyShipping class
        for date in trades_and_dates:
            monthly_shipping = MonthlyShipping(date, trades_and_dates[date])
            monthly_shipping.calculate_monthly_value()
            self._monthly_ship_trades.append(monthly_shipping)

    def process_quarterly_trades(self) -> list[QuarterlyShipping]:
        """
            Process Maritime data into Quarters
        """
        years_and_quarters = {}
        # iterates through self._monthly_ship_trades
        for monthly_trade in self._monthly_ship_trades:
            # finds in which quarter the monthly_trade occurred
            quarter = QUARTERS[monthly_trade.date.month]
            # finds in which year the monthly_trade occurred
            year = monthly_trade.date.year
            # Code for quarter and year so it can be used as a dictionary key
            code = str(quarter) + str(year)
            # monthly_trade inserted into dictionary that maps year and quarter to monthly trade
            # example: 12021 is code for first quarter in the year 2021
            if code in years_and_quarters:
                years_and_quarters[code].append(monthly_trade)
            else:
                years_and_quarters[code] = [monthly_trade]
        # Restructures dictionary of quarters and years into a list of instances of QuarterlyShipping class
        for code in years_and_quarters:
            quarter = QUARTERS[years_and_quarters[code][0].date.month]
            year = years_and_quarters[code][0].date.year
            quarterly_shipping = QuarterlyShipping(quarter, year, years_and_quarters[code])
            self._quarterly_ship_trades.append(quarterly_shipping)

        self.quarterly_shipping_sort()
        return self._quarterly_ship_trades

    def quarterly_shipping_sort(self) -> None:
        """
            Helper function that sorts self._quarterly_ship_trades earliest year and quarter using Selection Sort
            Preconditions:
                - len(self._quarterly_ship_trades) != 0
        """
        # outer for loop that loops through all elements
        for i in range(len(self._quarterly_ship_trades)):
            earliest = i
            # inner loop iterates through unsorted elements
            for j in range(i + 1, len(self._quarterly_ship_trades)):
                # compares the earliest element with rest of elements to find earliest element in unsorted list
                if self._quarterly_ship_trades[earliest].year > self._quarterly_ship_trades[j].year:
                    earliest = j
                elif self._quarterly_ship_trades[earliest].year == self._quarterly_ship_trades[j].year\
                        and self._quarterly_ship_trades[earliest].quarter > self._quarterly_ship_trades[j].quarter:
                    earliest = j
            # Swap earliest element if ith element in the list
            self._quarterly_ship_trades[i], self._quarterly_ship_trades[earliest] =\
                self._quarterly_ship_trades[earliest], self._quarterly_ship_trades[i]
