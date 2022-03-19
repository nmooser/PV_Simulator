from datetime import datetime

print ('Hello Git')
#!/usr/bin/env python
import pika
import json
import time
import random

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

msg={}


while True:
    now = datetime.now()
    msg['ts']=now.strftime("%H%M%S")
    msg['pwr']= str(random.randint(0,9000))
    time.sleep(1)
    print(json.dumps(msg, indent = None, separators=(",",":")))









connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')



i=0



