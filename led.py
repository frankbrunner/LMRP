import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)

print("Start Engine")
gpio.output(23, gpio.PUD_UP)
time.sleep(5)
gpio.output(23,gpio.PUD_DOWN)


gpio.cleanup() 

#kommentar
 
