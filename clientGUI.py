#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
import pika


class HelloWorld:

    def CBMethod(self, widget, data=None):
        self.channel.basic_publish(exchange='',
                                   routing_key='hello',
                                   body=data)
        print " [x] Sent {0}".format(data)


    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        self.connection.close()
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.143'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.entry  = gtk.Entry()
        self.vbox = gtk.VBox()

        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)
    
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(30)
    
        # Creates a new button with the label "Hello World".
        self.ButtonNames = ["burp","belch","horn","goat","bear","backUp","exterminate","horse","growl","roar","meow","panther","rex","rex2","rex3","roar","roar4","screech","warning"]
        self.Buttons = [gtk.Button(name) for name in self.ButtonNames]
    
        [self.vbox.pack_start(button) for button in self.Buttons]
        
        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        [button.connect("clicked", self.CBMethod, name) for button, name in zip(self.Buttons,self.ButtonNames)]
        
    
        # This packs the button into the window (a GTK container).
        self.window.add(self.vbox)
        self.window.show_all()
 

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
