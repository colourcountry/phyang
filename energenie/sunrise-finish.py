#!/usr/bin/python

import energenie
import sys,datetime

sys.stdout.write("Running sunrise-finish at %s\n" % datetime.datetime.now().isoformat())
sys.stdout.flush()

energenie.switch_off(1,2,3)

