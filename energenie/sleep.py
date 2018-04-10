#!/usr/bin/python

import energenie
import sys,datetime
import time, random

time.sleep(random.randrange(1200))
sys.stdout.write("Running sleep at %s\n" % datetime.datetime.now().isoformat())
sys.stdout.flush()

energenie.switch_off(1)
energenie.switch_off(3)
time.sleep(random.randrange(1200))
energenie.switch_off(4)
time.sleep(random.randrange(1200))
energenie.switch_off(2)

