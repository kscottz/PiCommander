#!/usr/bin/env python
import pika
import pygame as pg

pg.mixer.pre_init()
pg.init()

sound = pg.mixer.Sound('./evil.wav')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    sound.play()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
