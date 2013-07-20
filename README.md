# rpi-mpd-controller

Controller for Raspberry Pi + MPD. Based on mpc, Raspberry Pi GPIO.

## Features
* Play / Pause Music
* Previous Music / Next Msuic
* Playing Status LED (Blink when playing)

## Installation
1. Install mpd and configure
2. Install mpc
3. Test ```mpc play```, ```mpc pause```, ```mpc next```, ```mpc prev```
4. Make Circuit
![Circuit](https://raw.github.com/if1live/rpi-mpd-controller/master/documentation/circuit.jpg)
![GPIO](http://leaqua.mulple.com/wp-content/uploads/2012/08/Raspberry-Pi-GPIO-Layout.png)
4. ```sudo python main.py```
5. If want add startup script, add ```<rpi-mpd-controller-path>/main.py &``` inside ```/etc/rc.local```.

## Preview
[Video](http://www.youtube.com/watch?v=TRn8TviiMe0)

![Image](https://raw.github.com/if1live/rpi-mpd-controller/master/documentation/image.jpg)

## Reference
* http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html
* https://code.google.com/p/raspberry-gpio-python/
