import RPi.GPIO as GPIO
import threading
from classes import Stepper
from classes import ADC

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
    while(photoResVal< ambientVal):
      print('in while loop')
      stepperTry.contRotate()
  except Exception as e:
    print(e)
    


stepperThread = threading.Thread(target= stepper)
stepperThread.daemon= True # force to end when main code terminates
photoResVal=myADC.read(0) #0 channel
stepperThread.start() #continuously looping through stepper code
cond= True
while(cond==True):
  if (photoResVal< ambientVal):
    photoResVal=myADC.read(0) #0 channel
    print('the first cond is true: ', photoResVal)
  elif (photoResVal>= ambientVal):
    print('end motor')
    cond==False

  



