import RPi.GPIO as GPIO
import time
import threading
import smbus
from classes import ADC

GPIO.setmode(GPIO.BCM)

photoResistor= 0 #change as needed
ambientVal= 100 #change depending on room lighting
address= 0x48 #find device address


myADC= ADC(address)
GPIO.setup(photoResistor, GPIO.IN)
stepperPins = [12,16,20,21] # controller inputs: in1, in2, in3, in4
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]


def stepper():
  try:
    while(True):
      print('in while loop')
      for state in range(8):
        for pin in range(4):
          GPIO.output(stepperPins[pin], sequence[state][pin])
      time.delay(1)
  except Exception as e:
    print(e)
    


stepperThread = threading.Thread(target= stepper)
photoResVal=myADC.read(0) #0 channel
stepperThread.start() #continuously looping through stepper code
if (photoResVal> ambientVal):
  photoResVal=myADC.read(0) #0 channel
  print('the first cond is true: ', photoResVal)
elif (photoResVal< ambientVal):
  stepperThread.end()

  



