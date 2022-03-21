PV_Simulator
----
Python package implementing PV Simulator Challenge as provided

Installation
------------
Checkout from Github: https://github.com/nmooser/PV_Simulator.git

Python 3.8.10 / RabbitMQ 3.9.13 / Erlang 24.3.2

Quick start
-----------
main.py
~~~~~~~~~~~~~~

.. code-block::

    values = meter.createDayMeterValues() # Creates random power values for one day & writes it into an array as json expressions
    meter.writeDayMeterValues2Queue(values) # Writes it all into a RabbitMQ queue
    pv_simulator.processDayMeterValuesFromQueue() # Reads from that Queue and generates a simulated PV power value, adds this value to the meter value and output the result.


meter.py
~~~~~~~~~~~~~~

creates RabbitMQ queue and writes random power values to that in json format.
Covers a full day at intervals of 10 seconds

pv_simulator.py
~~~~~~~~~~~~~~

Reads the power values & timestamps from the queue and generates the
additional PV power from the characteristic given, these are:

+----------------------------------------------------------+
| default: 0.0                                             |
+----------------------------------------------------------+
| line with slope 0.35 from 6 to 8 o'clock                 |
+----------------------------------------------------------+
| fitted sin curve from 8 to 14 o'clock                    |
+----------------------------------------------------------+
| fitted sin curve from 14 to 20 o'clock                   |
+----------------------------------------------------------+
| line with slope -0.15 from 20 to 21 o'clock              |
+----------------------------------------------------------+

this is an approximate mathematical modelling of the curve.

Then creates a messages.csv file with Header

"timestamp", "pwr_meter/W", "pwr_pv/W", "pwr_meter+pv/W"
all power values are in W as integer.







