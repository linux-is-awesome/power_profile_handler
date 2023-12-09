#!/usr/bin/python3

import os
from gi.repository import Gio, GLib

def trigger_handler(_, __, ___): os.system('/usr/bin/pphandler')

proxy = None
loop = None

# run handler on the service startup as the udev rule is unable to read power profile on boot
trigger_handler(None, None, None)

loop = GLib.MainLoop()
bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
proxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
                               'net.hadess.PowerProfiles',
                               '/net/hadess/PowerProfiles',
                               'net.hadess.PowerProfiles', None)
proxy.connect('g-properties-changed', trigger_handler)
loop.run()
