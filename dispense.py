import RPi.GPIO as GPIO
import threading
from classes import Stepper
from classes import ADC
import time

GPIO.setmode(GPIO.BCM)

photoResistor= 0 #change as needed
ambientVal= 100 #change depending on room lighting
address= 0x48 #find device address


GPIO.setmode(GPIO.BCM)

stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

GPIO.setup(photoResistor, GPIO.IN)

stepperTry= Stepper(180,0)
myADC= ADC(address)

def stepper():
  try:
    while(True):
      if(photoResVal< ambientVal):
        print('in while loop')
        stepperTry.contRotate()
      else:
        print('in while loop, not rotating')
        time.sleep(1)

  except Exception as e:
    print(e)
    


stepperThread = threading.Thread(target= stepper)
stepperThread.daemon= True # force to end when main code terminates
photoResVal=myADC.read(0) #0 channel
stepperThread.start() #continuously looping through stepper code
cond= True
while(cond==True):
  photoResVal=myADC.read(0) #0 channel
  if (photoResVal< ambientVal):
    print('the first cond is true: ', photoResVal)
    time.sleep(1)
  elif (photoResVal>= ambientVal):
    print('end motor')
    time.sleep(1)
    

  



