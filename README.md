PiCommander
===========

Using RaspberryPi for Animatronics 

sudo pip install pika

On the RaspberryPi (Occidentalis)
==========================
see http://www.rabbitmq.com/install-debian.html

Add the following line to your /etc/apt/sources.list:

deb http://www.rabbitmq.com/debian/ testing main

Run apt-get update.

sudo apt-get install rabbitmq-server

copy the config file to /etc/rabbitmq
sudo cp rabbitmq.config /etc/rabbitmq

To start rabbitmq
sudo rabbitmq-server

Use rabbitmq-ctl to monitor/administer
 
To monitor
==============
http://<Pi IP address>:15672/#/.
login/pw: guest/guest
http://www.rabbitmq.com/management.html

logs in /var/log/rabbitmq
tail the logs to see if you hit a memory issue. 

Client
===============
install RabbitMQ
sudo pip install pika==0.9.8
PyGTK as necessary
