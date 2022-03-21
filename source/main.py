# !/usr/bin/env python
import json
from datetime import datetime, timedelta
import time
import random
from pv_simulator import pv_simulator
from meter import meter

meter = meter()
pv_simulator = pv_simulator(meter.getChannel())

values = meter.createDayMeterValues() # Creates random power values for one day & writes it into an array as json expressions
meter.writeDayMeterValues2Queue(values) # Writes it all into a RabbitMQ queue
pv_simulator.processDayMeterValuesFromQueue() # Reads from that Queue and generates a simulated PV power value, adds this value to the meter value and output the result.




exit(1)







# dateinfo = pv_simulator.phase3min
# while True:
#     print(json.dumps(msg, indent = None, separators=(",",":")))
#     pwr = pv_simulator.getPowerValue(dateinfo)
#     print ("%s pwr: %03f" % (msg['ts'], pwr))
#     dateinfo += timedelta(seconds=60 * 15)
#     if (dateinfo > pv_simulator.phase4max): break
#     time.sleep(1)



