from entities.QuarterlyGdp import QuarterlyGdp

class ProcessGdp:

    quarterly_gdp: [QuarterlyGdp]

    def __init__(self):
        self.quarterly_gdp = []

    def process_gdp(self, raw_gdp_data: list[(str, float)]) -> list[QuarterlyGdp]:
        """
            Processes quarterly gdp data
        """
        # discard any previous data
        self.quarterly_gdp = []
        for data in raw_gdp_data:
            # processes quarter and year as it is stored as a string (example: Q1 '11)
            split_data = data[0].split(' ')
            quarter = int(split_data[0][1])
            # dataset stores last 2 digits of years, since dataset only has data from 2000s and to be consistent
            # with other datasets 2000 is added
            year = 2000 + int(split_data[1].split('\'')[1])
            self.quarterly_gdp.append(QuarterlyGdp(quarter, year, data[1]))