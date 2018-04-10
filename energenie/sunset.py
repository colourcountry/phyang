#!/usr/bin/python

import energenie
import sys,datetime
import time, random

time.sleep(random.randrange(1200))
sys.stdout.write("Running sunset at %s\n" % datetime.datetime.now().isoformat())
sys.stdout.flush()

energenie.switch_on(2)
time.sleep(random.randrange(1200))
energenie.switch_on(1)

