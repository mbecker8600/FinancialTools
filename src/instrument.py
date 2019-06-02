from src.rebalance import BasicRebalancer
from src.util.data import get_initial_holdings


class Portfolio:

    def __init__(self, initial_holdings, initial_cash):
        # self.holdings = pd.DataFrame.from_dict(initial_holdings, orient='index', columns=['value'])
        self.holdings = initial_holdings
        self.cash = initial_cash
        self.allocations = self.holdings / self.holdings.sum()
        self.value = self.holdings.sum().value + self.cash

    def rebalance(self, rebalance_strategy):
        rebalance_strategy.rebalance(self)

    def statisitics(self):
        pass

    def execute_trade(self):
        pass

    def __compute_stats__(self):
        self.allocations = self.holdings / self.holdings.sum()
        self.value = self.holdings.sum().value + self.cash


if __name__ == '__main__':
    initial_holdings = get_initial_holdings()
    portfolio = Portfolio(initial_holdings, initial_cash=11012.38)

    target_alloc = {
        'VTI': .4,
        'BND': .3,
        'VXUS': .2,
        'BNDX': .1
    }
    portfolio.rebalance(BasicRebalancer(target_alloc, target_cash=10000))


