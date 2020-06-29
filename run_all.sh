#!/bin/sh
# usage: run_all.sh "Massachusetts"
mkdir -p out
python plot.py --state "$1" --counties Suffolk Middlesex Norfolk Essex --per-100k
