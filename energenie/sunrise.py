#!/usr/bin/python

import energenie
import sys, time, datetime

CONFIG = { 'no_weekend': True }

NOT_YET = 0
NOW = 1
NEVER = 2

sys.stdout.write("Running sunrise.py at %s\n" % datetime.datetime.now().isoformat())
sys.stdout.flush()

def is_time_to_wake( t ):
    if CONFIG['no_weekend'] and t.isoweekday() == 6:
        print "Saturday, exiting."
        return NEVER		# Saturday
    elif CONFIG['no_weekend'] and t.isoweekday() == 7:
        print "Sunday, exiting."
        return NEVER		# Sunday
    elif (t.hour,t.minute) > (6,30):
        print "Ready to wake up at "+datetime.datetime.now().isoformat()
        return NOW

def really_switch_on(tries=5, *sockets):
    print "Switching on %s at %s" % (",".join([str(s) for s in sockets]),datetime.datetime.now().isoformat())
    for x in range(tries):
        energenie.switch_on(*sockets)
        time.sleep(1)

while True:
    time.sleep(1)
    result = is_time_to_wake( datetime.datetime.now() )
    if result == NEVER:
        raise SystemExit
    elif result == NOW:
        break

# 6.45 fade
really_switch_on(5,1)

time.sleep(10 * 60)

# 6.55 light & radio
really_switch_on(5,2)

time.sleep(30 * 60)

# 7.25 sunlight downstairs
really_switch_on(5,3)

