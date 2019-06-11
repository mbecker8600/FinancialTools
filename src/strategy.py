import pandas as pd
import numpy as np
from src.transaction import Trade
from src.util.data import PricingRetriever


class BasicInvestment:

    def __init__(self, target_allocations, target_cash=0):
        '''
        :param target_allocations: JSON object of target allocations
        :type target_allocations: json
        :param target_cash: cash amount you'd like left over from the rebalancing
        :type target_cash: float
        '''
        self.target_allocations = pd.DataFrame.from_dict(target_allocations, orient='index', columns=['value'])
        self.target_cash = target_cash

    def execute(self, portfolio):
        '''
        Basic rebalancer strategy. It wont sell any funds in order to avoid any capital gains costs. It will only take
        the difference of the money in your cash reserves and your target cash allocations and invest your money to bring you
        closer to your target allocations.

        :param portfolio: The portfolio object that will be rebalanced
        :return: a list of trades to execute based on the rebalancing algorithm
        :rtype: Trade[]
        '''

        investment_capital = portfolio.cash - self.target_cash
        target_holdings = self.target_allocations * (portfolio.holdings['value'].sum() + investment_capital)
        holdings_difference = target_holdings['value'] - portfolio.holdings['value']

        retriever = PricingRetriever.instance()
        current_prices = retriever.current_prices()

        buy_symbols = holdings_difference[holdings_difference > 0]
        safe_buy_symbols = (buy_symbols / buy_symbols.sum()) * investment_capital
        buy_trades = safe_buy_symbols / current_prices['adjClose']
        buy_trades.dropna(inplace=True)
        buy_trades = buy_trades.apply(np.floor)

        trades = []
        for sym, quantity in zip(buy_trades.index.tolist(), buy_trades.values.tolist()):
            trade = Trade(sym, 'BUY', quantity)
            trades.append(trade)

        return trades


class BasicRebalance:

    def __init__(self):
        pass

    def execute(self):
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
