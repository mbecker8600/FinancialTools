from src.rebalance import BasicRebalancer
from src.util.data import get_current_pricing
import pandas as pd


class Portfolio:

    def __init__(self, initial_holdings, initial_cash):
        # self.holdings = pd.DataFrame.from_dict(initial_holdings, orient='index', columns=['value'])
        self.holdings = pd.DataFrame(initial_holdings, columns=['sym', 'shares']).set_index('sym')
        self.__compute_stats__()
        self.cash = initial_cash
        self.value = self.holdings['value'].sum() + self.cash

    def rebalance(self, rebalance_strategy):
        trades = rebalance_strategy.rebalance(self)
        for trade in trades:
            print(trade)

    def report(self):
        print("-- Portfolio Report --")
        print("Value\n{}\n".format(self.value))
        print("Current portfolio\n{}\n".format(self.holdings))
        print("----------------------")
        pass

    def execute_trade(self):
        pass

    def __compute_stats__(self):
        current_prices = get_current_pricing()
        self.holdings['value'] = current_prices['value'] * self.holdings['shares']
        self.holdings['allocation'] = self.holdings['value'] / self.holdings['value'].sum()


if __name__ == '__main__':
    # initial_holdings = get_initial_holdings()

    initial_holdings = [
        ('VTI', 106.323),
        ('BND', 108.796),
        ('VXUS', 128.178),
        ('BNDX', 71.368)
    ]
    portfolio = Portfolio(initial_holdings, initial_cash=11012.38)

    target_alloc = {
        'VTI': .4,
        'BND': .3,
        'VXUS': .2,
        'BNDX': .1
    }
    portfolio.rebalance(BasicRebalancer(target_alloc, target_cash=10000))

    portfolio.report()


