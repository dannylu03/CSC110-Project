from QuarterlyGdp import QuarterlyGdp

class ProcessGdp:

    def __init__(self):
        self._quarterly_gdp = []

    def process_gdp(self, raw_gdp_data: list[(str, float)]) -> None:
        """
            Processes quarterly gdp data
        """
        # discard any previous data
        self._quarterly_gdp = []
        for data in raw_gdp-data
            split_data = data[0].split(' ')
            quarter = int(split_data[0][1])
            year = 2000 + int(data[1].split('i')[1])
            self._quarterly_gdp.append(QuarterlyGdp(quarter, year, data[1]))