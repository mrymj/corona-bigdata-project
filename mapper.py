#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    (date, city, state, cases, dead, ok) = line.split(',', 5)
    (month, day, year) = date.split('/', 2)
    print('%s,%s,%s,%s,%s' % (state, month, year, cases, dead))
