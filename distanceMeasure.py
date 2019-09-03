#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:22:30 2019

@author: pi
"""
import RPi.GPIO as GPIO
import time
count = 0
GPIO.setwarnings(False)
 
class distanceMeasure:
    def __init__(self,Channel,Durchmesser,Teilung):
        self.channel = Channel
        self.durchmesser = Durchmesser
        self.teilung = Teilung
        self.distance = 0.0
         
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel,GPIO.IN,GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.channel, GPIO.RISING)
    
    def distMeasure(self):
        if GPIO.event_detected(self.channel):
                global count
                count = count + 1
                print (count)
                self.distance = self.distance + (self.durchmesser * 3.14333) / self.teilung
        return self.distance

        


        
