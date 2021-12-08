import RPi.GPIO as GPIO
import time
import threading
import smbus
from classes import ADC

GPIO.setmode(GPIO.BCM)

photoResistor= 0 #change as needed

address= 0x48 #find device address
myADC= ADC(address)
photoResVal=myADC.read(0) #0 channel
print(photoResVal)



