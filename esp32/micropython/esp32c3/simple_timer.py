import network

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    #sta.connect('your wifi ssid', 'your wifi password')
    sta.connect("rockspace_EXT", "917219418D05224247G")
    while not sta.isconnected():
        pass

print('network config:', sta.ifconfig())
