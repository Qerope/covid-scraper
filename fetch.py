import io

import pandas as pd
import requests

URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
def counties():
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), parse_dates=['date'])
