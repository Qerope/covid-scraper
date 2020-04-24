import argparse

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fetch import counties


def daily(df):
    new = df.sort_values('date').set_index('date')['cases'].diff().fillna(0)
    return new.clip(lower=0)


def smooth(s):
    return s.rolling(7, min_periods=1).mean()


def population(state, county):
    pop = pd.read_csv('data/population.csv')
    row = pop[(pop.state == state) & (pop.county == county)]
    return int(row.population.iloc[0])


def select(df, state, county):
    # the NYT file reports the five boroughs as "New York City"
    if state == 'New York' and county in ('Kings', 'Queens', 'Bronx', 'Richmond', 'New York'):
        county = 'New York City'
    return df[(df.state == state) & (df.county == county)], county


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', required=True)
    ap.add_argument('--counties', nargs='+', required=True)
    ap.add_argument('--per-100k', action='store_true')
    args = ap.parse_args()

    df = counties()
    for name in args.counties:
        c, name = select(df, args.state, name)
        new = daily(c)
        new = smooth(new)
        if args.per_100k:
            new = new / population(args.state, name) * 100000
        plt.plot(new.index, new, label=name)
    plt.legend()
    plt.title(args.state)
    plt.ylabel('new cases (7 day mean)')
    plt.gcf().autofmt_xdate()
    plt.savefig('out/%s.png' % args.state.replace(' ', '_'))


if __name__ == '__main__':
    main()
