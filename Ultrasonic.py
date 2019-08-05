#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
 
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
#GPIO_TRIGGER = 20
#GPIO_ECHO = 21

GPIO.setwarnings(False)
 
#Richtung der GPIO-Pins festlegen (IN / OUT)

 
class ultrasonic:
    def __init__(self,GPIO_TRIGGER,GPIO_ECHO):
        
        self.gpioTrigger = GPIO_TRIGGER
        self.gpioEcho = GPIO_ECHO
        
        GPIO.setup(self.gpioTrigger, GPIO.OUT)
        GPIO.setup(self.gpioEcho, GPIO.IN)
        
        
        
    def distanz(self):
        
        # setze Trigger auf HIGH
        GPIO.output(self.gpioTrigger, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(self.gpioTrigger, False)
     
        StartZeit = time.time()
        StopZeit = time.time()
     
        # speichere Startzeit
        while GPIO.input(self.gpioEcho) == 0:
            StartZeit = time.time()
     
        # speichere Ankunftszeit
        while GPIO.input(self.gpioEcho) == 1:
            StopZeit = time.time()
     
        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz = (TimeElapsed * 34300) / 2
     
        return distanz


 
#if __name__ == '__main__':
#    try:
#        while True:
#            abstand = distanz()
#            print ("Gemessene Entfernung = %.1f cm" % abstand)
#            time.sleep(1)
# 
#        # Beim Abbruch durch STRG+C resetten
#    except KeyboardInterrupt:
#        print("Messung vom User gestoppt")
#        GPIO.cleanup()

