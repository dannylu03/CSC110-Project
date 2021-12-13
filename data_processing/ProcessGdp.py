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
            split_data = data[0].split(' ')
            quarter = int(split_data[0][1])
            year = 2000 + int(split_data[1].split('\'')[1])
            self.quarterly_gdp.append(QuarterlyGdp(quarter, year, data[1]))