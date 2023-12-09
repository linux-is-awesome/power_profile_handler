#!/usr/bin/python3

import os, sys
from gi.repository import Gio, GLib, GObject

def trigger_handler(_, __, ___): os.system('/usr/bin/pphandler')

proxy = None
loop = None

loop = GLib.MainLoop()
bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
proxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
                               'net.hadess.PowerProfiles',
                               '/net/hadess/PowerProfiles',
                               'net.hadess.PowerProfiles', None)
proxy.connect('g-properties-changed', trigger_handler)
loop.run()
