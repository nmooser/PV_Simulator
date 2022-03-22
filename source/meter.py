import json
import random
from datetime import datetime, timedelta
import pika

class meter():
    step = None
    connection = None
    channel = None

    def getChannel(self): return self.channel
    def getConnection(self): return self.connection

    def __init__(self):
        self.step = 10 # secs
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_delete(queue='hello')
        self.channel.queue_declare(queue='hello')

    def createDayMeterValues(self):
        out = []
        dateinfo = datetime.now()
        today = dateinfo.replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow = today + timedelta(days=1)
        timeval = today

        msg = {}
        while timeval < tomorrow:
            msg['ts'] = timeval.strftime("%Y-%m-%d %H:%M:%S")
            msg['pwr'] = str(random.randint(0, 9000))
            out.append(json.dumps(msg, indent=None, separators=(",", ":")))
            timeval += timedelta(seconds=self.step)
        return out

    def writeDayMeterValues2Queue(self, values):
        for x in values:
            self.channel.basic_publish(exchange='', routing_key='hello', body=x)
        self.channel.basic_publish(exchange='', routing_key='hello', body="stop")
        # self. connection.close()




