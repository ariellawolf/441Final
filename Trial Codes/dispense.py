import RPi.GPIO as GPIO
import threading
from classes import Stepper
from classes import ADC
import time

GPIO.setmode(GPIO.BCM)

photoResistor= 0 #change as needed
ambientVal= 80 #change depending on room lighting
address= 0x48 #find device address



stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

GPIO.setup(photoResistor, GPIO.IN)

stepperTry= Stepper(180,0)
myADC= ADC(address)

def stepper():
  try:
    condition= True
    while(True):
      if(photoResVal< ambientVal):
        print('in while loop')
        stepperTry.contRotate()
      elif(condition== True):
        print("this second cond is true")
        for j in range(4):
          for i in range(1000):
            stepperTry.contRotate()
            print(i)
        condition= False
      else:
        print('in while loop, not rotating')
        time.sleep(5)

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
    #cond=False #remove this for repetative turning

  



