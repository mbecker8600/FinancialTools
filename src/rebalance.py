import pandas as pd
import numpy as np
from src.util.data import get_current_pricing


class BasicRebalancer:

    def __init__(self, target_allocations, target_cash=0):
        '''
        :param target_allocations: JSON object of target allocations
        :type target_allocations: json
        :param target_cash: cash amount you'd like left over from the rebalancing
        :type target_cash: float
        '''
        self.target_allocations = pd.DataFrame.from_dict(target_allocations, orient='index', columns=['value'])
        self.target_cash = target_cash

    def rebalance(self, portfolio):
        '''
        Basic rebalancer strategy. It wont sell any funds in order to avoid any capital gains costs. It will only take
        the difference of the money in your cash reserves and your target cash allocations and invest your money to bring you
        closer to your target allocations.

        :param portfolio: The portfolio object that will be rebalanced
        :return: a list of trades to execute based on the rebalancing algorithm
        :rtype: Trade[]
        '''

        investment_capital = portfolio.cash - self.target_cash
        target_holdings = self.target_allocations * (portfolio.holdings.sum() + investment_capital)
        holdings_difference = target_holdings - portfolio.holdings
        pricing = get_current_pricing()

        buy_symbols = holdings_difference[holdings_difference > 0]
        buy_symbols.dropna(inplace=True)
        safe_buy_symbols = (buy_symbols / buy_symbols.sum()) * investment_capital
        buy_trades = safe_buy_symbols / pricing
        buy_trades.dropna(inplace=True)
        buy_trades = buy_trades.apply(np.floor)
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
