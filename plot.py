import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fetch import counties


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', required=True)
    ap.add_argument('--county', required=True)
    args = ap.parse_args()

    df = counties()
    c = df[(df.state == args.state) & (df.county == args.county)]
    plt.plot(c.date, c.cases)
    plt.title(args.state)
    plt.ylabel('new cases (7 day mean)')
    plt.gcf().autofmt_xdate()
    plt.savefig('out/%s.png' % args.state.replace(' ', '_'))


if __name__ == '__main__':
    main()
