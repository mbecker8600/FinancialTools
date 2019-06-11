from cmd import Cmd
from src.util.session import Session, SessionManager
from src.instrument import Portfolio
from src.strategy import BasicInvestment


class IPrompt(Cmd):

    def __init__(self):
        self.session = Session()
        self.session_manager = SessionManager()
        super().__init__()

    def do_create_portfolio(self, args):
        """Creates a portfolio"""
        initial_cash = float(input("How much cash is in your portfolio? "))
        n_holdings = int(input("How many holdings do you have? "))
        holdings = []
        for _ in range(n_holdings):
            sym = input("Symbol? ")
            shares = float(input("Number of shares? "))
            holdings.append((sym, shares))
        portfolio = Portfolio(holdings, initial_cash=initial_cash)

        print("Created new portfolio")
        portfolio.report()
        self.session.portfolio = portfolio

    def do_save(self, args):
        """Saves the current session with name given"""

        session_name = args
        print("Saving session '{}'".format(session_name))
        self.session.name = session_name
        self.session_manager.save(self.session)

    def do_load(self, args):
        """Loads the specified session name"""
        session_name = args
        print("Loading session '{}'".format(session_name))
        self.session = self.session_manager.load(session_name)

    def do_invest(self, args):
        """Invests based on a given strategy"""

        target_alloc = {
            'VTI': .5,
            'BND': .2,
            'VXUS': .2,
            'BNDX': .1
        }
        self.session.portfolio.invest(BasicInvestment(target_alloc, target_cash=10000))

    def do_report(self, args):
        """report portfolio"""
        self.session.portfolio.report()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = IPrompt()
    prompt.prompt = 'Portfolio tools> '
    prompt.cmdloop('Starting prompt...')
