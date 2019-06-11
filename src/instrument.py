from src.strategy import BasicInvestment
from src.util.data import PricingRetriever
import pandas as pd


class Portfolio:

    def __init__(self, initial_holdings, initial_cash):
        self.holdings = pd.DataFrame(initial_holdings, columns=['sym', 'shares']).set_index('sym')
        self.retriever = PricingRetriever.instance()
        self.retriever.initialize(self.holdings.index.tolist())
        self.__compute_stats__()
        self.cash = initial_cash
        self.value = self.holdings['value'].sum() + self.cash

    def invest(self, investment_strategy):
        trades = investment_strategy.execute(self)
        for trade in trades:
            print(trade)

    def report(self):
        self.__compute_stats__()
        print("-- Portfolio Report --")
        print("Value\n{}\n".format(self.value))
        print("Current portfolio\n{}\n".format(self.holdings))
        print("----------------------")

    def execute_trade(self):
        pass

    def __compute_stats__(self):
        current_prices = self.retriever.current_prices()
        self.holdings['value'] = current_prices['adjClose'] * self.holdings['shares']
        self.holdings['allocation'] = self.holdings['value'] / self.holdings['value'].sum()


if __name__ == '__main__':
    initial_holdings = [
        ('VTI', 119.323),
        ('BND', 109.052),
        ('VXUS', 138.178),
        ('BNDX', 71.437)
    ]
    portfolio = Portfolio(initial_holdings, initial_cash=10097.26)

    target_alloc = {
        'VTI': .5,
        'BND': .2,
        'VXUS': .2,
        'BNDX': .1
    }
    portfolio.invest(BasicInvestment(target_alloc, target_cash=10000))

    portfolio.report()


