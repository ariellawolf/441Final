import RPi.GPIO as GPIO
import time
from classes import Stepper

GPIO.setmode(GPIO.BCM)

stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

stepperTry= Stepper(180,0)
rotationNumber=0
try:
    while(True):
      print('in while loop')
      stepperTry.contRotate()
      rotationNumber=rotationNumber+1
      print(rotationNumber)
except Exception as e:
  print(e)