#!/usr/bin/env python
import pika
import pygame as pg

pg.mixer.pre_init(frequency=22050, size=-16, channels=1)
pg.init()


bear = pg.mixer.Sound('./bear.wav')

lroar = pg.mixer.Sound('./lion_roar.wav')
lgrowl = pg.mixer.Sound('./lion_growl.wav')
panther = pg.mixer.Sound('./panther.wav')
horse = pg.mixer.Sound('./horse.wav')
warning = pg.mixer.Sound('./warning.wav')
meow = pg.mixer.Sound('./meow.wav')
rex = pg.mixer.Sound('./rex.wav')
rex2 = pg.mixer.Sound('./rex2.wav')
rex3 = pg.mixer.Sound('./rex3.wav')
roar = pg.mixer.Sound('./roar.wav')
roar2 = pg.mixer.Sound('./roar2.wav')
backup = pg.mixer.Sound('./backUp.wav')
exterminate = pg.mixer.Sound('./exterminate.wav')
screech = pg.mixer.Sound('./screech.wav')
goat = pg.mixer.Sound('./goat.wav')
burp = pg.mixer.Sound('./burp.wav')
belch = pg.mixer.Sound('./belch.wav')
horn = pg.mixer.Sound('./horn.wav')


soundMap = {
    'burp':burp,
    'horn':horn,
    'belch':belch,
    'bear':bear,
    'goat':goat,
    'roar':lroar,
    'growl':lgrowl,
    'panther':panther,
    'horse':horse,
    'meow':meow,
    'rex':rex,
    'rex2':rex2,
    'rex3':rex3,
    'roar2':roar2,
    'backUp':backup,
    'warning':warning,
    'exterminate':exterminate,
    'screech':screech
    }

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    if( soundMap.has_key(body) ):
        s = soundMap[body]
        s.play()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
