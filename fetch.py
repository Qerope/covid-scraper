import io
import os
import time

import pandas as pd
import requests

URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
CACHE = 'cache/us-counties.csv'


def counties():
    if os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 3600:
        return pd.read_csv(CACHE, parse_dates=['date'])
    os.makedirs('cache', exist_ok=True)
    for attempt in range(3):
        try:
            r = requests.get(URL, timeout=30)
            r.raise_for_status()
            break
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
    with open(CACHE, 'wb') as f:
        f.write(r.content)
    return pd.read_csv(io.StringIO(r.text), parse_dates=['date'])
