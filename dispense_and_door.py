import RPi.GPIO as GPIO
import threading
from classes import Stepper
from classes import ADC
import time

GPIO.setmode(GPIO.BCM)

PIRPin= 5 #change this as needed- this connects to alarm pin (low if something is detected)
servoPin= 13 #change this as needed
GPIO.setup(PIRPin, GPIO.IN,pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(servoPin, GPIO.OUT)
dcMin = 2 #this may need to be changed
dcMax = 12 #this may need to be changed
servo= GPIO.PWM(servoPin, 50) #50 Hz


ambientVal= 100 #change depending on room lighting
address= 0x48 #find device address



stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)



stepperTry= Stepper(180,0)
myADC= ADC(address)


def doorOpen(self):
  
  print('servo started')
  
  try:
    servo.start(dcMin)
    print('in try statement')  
    servo.ChangeDutyCycle(dcMax)
    time.sleep(3)
    servo.ChangeDutyCycle(dcMin)
    time.sleep(.5)
    
  except KeyboardInterrupt:
    print("bye")
    servo.stop()
  
def stepper():
  try:
    while(True):
      if(photoResVal< ambientVal):
        print('in while loop')
        stepperTry.contRotate()
      else:
        print('in while loop, not rotating')
        time.sleep(5)

  except Exception as e:
    print(e)
    
    
GPIO.add_event_detect(PIRPin, GPIO.RISING, callback= doorOpen, bouncetime=100)


stepperThread = threading.Thread(target= stepper)
stepperThread.daemon= True # force to end when main code terminates
photoResVal=myADC.read(0) #0 channel
stepperThread.start() #continuously looping through stepper code
cond= True

while(cond==True):
  photoResVal=myADC.read(0) #0 channel
  PIRreading = GPIO.input(PIRPin)
  print('pir value is: ', PIRreading)
  time.sleep(.1)
  if (photoResVal< ambientVal):
    print('the first cond is true: ', photoResVal)
    time.sleep(1)
  elif (photoResVal>= ambientVal):
    print('end motor')
    time.sleep(1)
    cond=False #remove this for repetative turning