# covid-scraper

Per-county case charts from the New York Times data
(github.com/nytimes/covid-19-data).

    pip install -r requirements.txt
    python plot.py --state Massachusetts --counties Suffolk Middlesex --per-100k

Daily new cases are computed from the cumulative counts, smoothed with a 7 day
mean. The NYT data counts NYC as one geography, so the five boroughs are not
separate. Population comes from `data/population.csv` (Census 2019 estimates,
county level).

`run_all.sh` writes one chart per county for a state into `out/`; I run it
from cron.
