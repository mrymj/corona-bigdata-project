#!/usr/bin/env python3
import sys


current_state = None
current_month = None
current_cases = 0
current_dead = 0
i = 0

for line in sys.stdin:
    # remove loading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    state, month, year, cases, dead = line.split(',', 4)
    try:
        cases = int(cases)
        dead = int(dead)
    except ValueError:
        # current_cases or current_dead were not numbers, so silently
        # ignore/discard this line
        continue
        # this IF-switch only works because Hadoop sorts map output
        # by key before it is passed to the reducer

    if current_month == month and current_state == state:
        current_cases += current_cases
        current_dead += current_dead
        continue
    else:

        if current_state and current_month:
            print('Month: %s, State: %s, the average of cases: %s, the average of deaths: %s' % (current_month, current_state, current_cases, current_dead))
        current_state=state
        current_cases=cases
        current_dead=dead
        current_month=month


# do not forget to output the last word if needed!
if current_month and current_state :
    if current_month in ['1','3','5','7','8','10','12']:
        current_cases=current_cases/31
        current_dead=current_dead/31
    elif current_month in ['2','4','6','9','11']:
        current_cases=current_cases/30
        current_dead=current_dead/30
    print('%s, State: %s, the average of cases: %s, the average of deaths: %s' % (current_month, current_state, current_cases, current_dead))
