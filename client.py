#!/usr/bin/env python
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.143'))
channel = connection.channel()
channel.queue_declare(queue='hello')
buttonNames = ["burp","belch","horn","goat","bear","backUp","exterminate","horse","growl","roar","meow","panther","rex","rex2","rex3","roar","roar4","screech","warning"]

def CBMethod(data):
    print " [x] Sent {0}".format(data)
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=data)
    

derp =["{0}:{1}".format(v,b) for v,b  in zip(range(0,len(buttonNames)),buttonNames)]
while True:
    for d in derp:
        print d
    print "q to quit"
    var = raw_input("Enter a choice: ")
    if( var == 'q' ):
        break
    if not var.isdigit():
        print "NOT A NUMBER!"
        continue
    val = int(var)%(len(buttonNames))
    CBMethod(buttonNames[val])
    
connection.close()
