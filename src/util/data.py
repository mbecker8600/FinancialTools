import pandas as pd
from definitions import ROOT_DIR
import os


def get_datafile(name):
    return os.path.join(ROOT_DIR, 'src', 'data', name)


def get_current_pricing():
    current_pricing = pd.read_csv(get_datafile('pricing.csv'), index_col=0)
    return current_pricing


def get_initial_holdings():
    holdings = pd.read_csv(get_datafile('initial_holdings.csv'), index_col=0)
    return holdings


if __name__ == '__main__':
    get_initial_holdings()

