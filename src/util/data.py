import pandas_datareader as pdr
import os
from src.util.patterns import Singleton


@Singleton
class PricingRetriever:

    def __init__(self):
        self.pricing = None

    def initialize(self, syms):
        self.pricing = pdr.get_data_tiingo(syms, api_key=os.getenv('TIINGO_API_KEY'))

    def current_prices(self):
        return self.pricing.groupby('symbol').last()


if __name__ == '__main__':
    PricingRetriever.instance()


