import pickle
from definitions import ROOT_DATA
import os


class Session:

    def __init__(self):
        self.portfolio = None
        self.name = None


class SessionManager:

    def __init__(self):
        pass

    def load(self, name):
        file = os.path.join(ROOT_DATA, "{}.txt".format(name))
        filehandler = open(os.path.expanduser(file), 'rb')
        return pickle.load(filehandler)

    def save(self, session):
        file = os.path.join(ROOT_DATA, "{}.txt".format(session.name))
        filehandler = open(os.path.expanduser(file), 'wb')
        pickle.dump(session, filehandler)


if __name__ == '__main__':
    from src.instrument import Portfolio

    session = Session()
    initial_holdings = [
        ('VTI', 106.323),
        ('BND', 108.796),
        ('VXUS', 128.178),
        ('BNDX', 71.368)
    ]
    portfolio = Portfolio(initial_holdings, initial_cash=11012.38)

    session.portfolio = portfolio
    session.name = 'becker-session'

    session_manager = SessionManager()
    session_manager.save(session)
