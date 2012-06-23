#!/usr/bin/python
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hello World")

        #self.button = Gtk.Button(label = "Click Here")
        #self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)
        rootBox = Gtk.Box()
        albumImg = Gtk.Label(label="Album Art")
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        ctrlBox = Gtk.Box()
        prevBtn = Gtk.Button(label="Prev")
        ppBtn = Gtk.Button(label="PP")
        stopBtn = Gtk.Button(label="Stop")
        nextBtn = Gtk.Button(label="Next")
        progBar = Gtk.ProgressBar()
        volBtn = Gtk.Button(label="Vol")
        infoLabel = Gtk.Label(label="Currently Playing")
        label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
        
        ctrlBox.pack_start(prevBtn, False, False, 0)
        ctrlBox.pack_start(ppBtn, False, False, 0)
        ctrlBox.pack_start(stopBtn, False, False, 0)
        ctrlBox.pack_start(nextBtn, False, False, 0)
        ctrlBox.pack_start(progBar, False, False, 0)
        ctrlBox.pack_start(volBtn, False, False, 0)

        mainBox.pack_start(ctrlBox, False, False, 0)
        mainBox.pack_start(infoLabel, False, False, 0)
        
        rootBox.pack_start(albumImg, False, False, 0)
        rootBox.pack_start(mainBox, False, False, 0)

        self.add(rootBox)

    def on_button_clicked(self, widget):
        print("Hello World!")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
