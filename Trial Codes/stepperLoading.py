import RPi.GPIO as GPIO
from classes import Stepper

GPIO.setmode(GPIO.BCM)

stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

stepperTry= Stepper(180,0)

try:
    while(True):
      print('in while loop')
      stepperTry.contRotateCW()
except Exception as e:
  print(e)