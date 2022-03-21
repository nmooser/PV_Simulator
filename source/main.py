# !/usr/bin/env python
from pv_simulator import pv_simulator
from meter import meter

meter = meter()
pv_simulator = pv_simulator(meter.getChannel(), meter.getConnection())

print("creating meter values")
values = meter.createDayMeterValues() # Creates random power values for one day & writes it into an array as json expressions
print("writing meter values to message queue")
meter.writeDayMeterValues2Queue(values) # Writes it all into a RabbitMQ queue
print("reading queue & mixing PV values, writing message.csv")
pv_simulator.processDayMeterValuesFromQueue() # Reads from that Queue and generates a simulated PV power value, adds this value to the meter value and output the result.
exit(1)







