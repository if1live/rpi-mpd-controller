#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html
'''

import RPi.GPIO as GPIO
import time
import commands
import re

PIN_STATUS = 3
PIN_PREV_BTN = 8
PIN_PLAY_BTN = 10
PIN_NEXT_BTN = 12

class Player(object):
    def __init__(self):
        self.play_state = self.is_playing()
        
    def is_playing(self):
        re_play = re.compile(r'^\[playing\].+$')
        result = commands.getstatusoutput('mpc')
        line_list = result[1].splitlines()

        playing = False
        for line in line_list:
            if re_play.match(line) is not None:
                playing = True

        self.play_state = playing
        return playing

    def play(self):
        if self.is_playing():
            retval = commands.getoutput('mpc pause')
            self.play_state = False
        else:
            retval = commands.getoutput('mpc play')
            self.play_state = True
        print retval

    def prev(self):
        retval = commands.getoutput('mpc prev')
        print retval

    def next(self):
        retval = commands.getoutput('mpc next')
        print retval

class PlayerStatusLED(object):
    def __init__(self, player):
        self.player = player
        
    def update(self):
        if self.player.play_state:
            GPIO.output(PIN_STATUS, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(PIN_STATUS, GPIO.LOW)
            time.sleep(0.1)
        else:
            GPIO.output(PIN_STATUS, GPIO.LOW)
            time.sleep(0.1)

class Button(object):
    def __init__(self, pin, func):
        self.pin = pin
        self.old_state = 0
        self.func = func
        GPIO.setup(pin, GPIO.IN)

    def update(self):
        curr_state = GPIO.input(self.pin)
        if self.old_state is 0 and curr_state is 1:
            self.func()
        self.old_state = curr_state

def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(PIN_STATUS, GPIO.OUT)

    player = Player()
    player.play()
    status_led = PlayerStatusLED(player)

    prev_btn = Button(PIN_PREV_BTN, lambda: player.prev())
    play_btn = Button(PIN_PLAY_BTN, lambda: player.play())
    next_btn = Button(PIN_NEXT_BTN, lambda: player.next())
    
    while True:
        prev_btn.update()
        play_btn.update()
        next_btn.update()
        status_led.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
    GPIO.cleanup()
