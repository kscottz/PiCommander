#!/usr/bin/env python
import pika
import pygame as pg

pg.mixer.pre_init()
pg.init()

#sound = pg.mixer.Sound('./evil.wav')
bear = pg.mixer.Sound('./bear.wav')
burp = pg.mixer.Sound('./burp.mp3')
goat = pg.mixer.Sound('./goat2.wav')
lroar = pg.mixer.Sound('./lion_roar.wav')
lgrowl = pg.mixer.Sound('./lion_growl.wav')
panther = pg.mixer.Sound('./panther.wav')
horse = pg.mixer.Sound('./horse')

soundMap = {
    'bear':bear,
    'burp':burp,
    'goat':goat,
    'lroar':lroar,
    'lgrowl':lgrowl,
    'panther':panther,
    'horse':horse
    }



connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    s = soundMap[body]
    s.play()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
