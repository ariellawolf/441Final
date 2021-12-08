import RPi.GPIO as GPIO
import time
import threading
import smbus
from classes import ADC

GPIO.setmode(GPIO.BCM)

photoResistor= 6 #change as needed
GPIO.setup(photoResistor, GPIO.IN)
stepperPins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

def stepper():
  try:
    while(True):
      for state in range(8):
        for pin in range(4):
          GPIO.output(stepperPins[pin], sequence[state][pin])
      time.delay(1)
  except Exception as e:
    print(e)
    


stepperThread = threading.Thread(target= stepper)

stepperThread.start() #continuously looping through stepper code
while(True):
  



