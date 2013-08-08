#!/usr/bin/python
import wx
import random
import pika
APP_SIZE_X = 200
APP_SIZE_Y = 620
class MyButtons(wx.Dialog):
	def __init__(self, parent, id, title):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.142'))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue='hello')
		self.ButtonNames = ["burp","belch","horn","goat","bear","backUp","exterminate","horse","growl","roar","meow","panther","rex","rex2","rex3","roar2","screech","warning"]
		wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X, APP_SIZE_Y))
		cnt = len(self.ButtonNames)
		for name,idx in zip(self.ButtonNames,range(0,cnt)):
			wx.Button(self,idx,name,(50,idx*30+10))
			self.Bind(wx.EVT_BUTTON,self.CBMethod,id=idx)

		self.Centre()
		self.ShowModal()
		self.Destroy()

	def OnClose(self, event):
		self.connection.close()
		self.Close(True)

	def CBMethod(self, data):
		msg = data.GetEventObject().GetLabel()#self.ButtonNames[data.GetSelection()]
		self.channel.basic_publish(exchange='',routing_key='hello',body=msg)
		print " [x] Sent {0}".format(msg)
		
app = wx.App(0)
MyButtons(None, -1, 'DragonBot Sounds')
app.MainLoop()
