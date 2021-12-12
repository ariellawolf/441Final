import RPi.GPIO as GPIO
import threading
from classes import Stepper
from classes import ADC
import time
import json

GPIO.setmode(GPIO.BCM)

PIRPin= 5 #change this as needed- this connects to alarm pin (low if something is detected)
servoPin= 13 #change this as needed
GPIO.setup(PIRPin, GPIO.IN,pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(servoPin, GPIO.OUT)
dcMin = 2 #this may need to be changed
dcMax = 12 #this may need to be changed
servo= GPIO.PWM(servoPin, 50) #50 Hz


ambientVal= 95 #change depending on room lighting
address= 0x48 #find device address



stepperPins = [19,26,17,27] # controller inputs: in1, in2, in3, in4

for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)



stepperTry= Stepper(180,0)
myADC= ADC(address)


def stepper():
  try:
    while(photoResVal< ambientVal):
      stepperTry.contRotate()
    
  except Exception as e:
    print(e)
    
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
photoResVal=myADC.read(0)
print('the Photoresistor Value is: ', photoResVal)
GPIO.add_event_detect(PIRPin, GPIO.RISING, callback= doorOpen, bouncetime=100)

cond=True
cond3=True
cond4=True

while (cond4==True):
  try:
    with open('/usr/lib/cgi-bin/vending.txt','r') as f:
      productRead= json.load(f)
      
    productSelected= productRead["option"]
      
    
    if (productSelected=="reeses"):
      stepperThread = threading.Thread(target= stepper)
      stepperThread.daemon= True # force to end when main code terminates
      photoResVal=myADC.read(0) #0 channel
      stepperThread.start() #continuously looping through stepper code

      #Stepper Motor & Photoresistor Execution Code 
      while(cond==True):
        photoResVal=myADC.read(0) #0 channel
        time.sleep(.01)
        if (photoResVal< ambientVal):
          print('the first cond is true: ', photoResVal)
          time.sleep(.01)
        elif (photoResVal>= ambientVal):
          print('end motor')
          time.sleep(.01)
          cond=False #remove this for repetative turning
          
      #Servo Motor & PIR Sensor Code
      
      while(cond3==True):
        PIRreading = GPIO.input(PIRPin)
        print('pir value is: ', PIRreading)
        time.sleep(.01)
        if (PIRreading==1):
          cond3= False
          cond4= False
      
          
    else:
      print(productRead)
      print('product selected is: ', productSelected)
  except Exception as e:
    print(e)