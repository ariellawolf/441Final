import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

PIRPin= 5 #change this as needed- this connects to alarm pin (low if something is detected)
LEDPin= 13 #change this as needed
GPIO.setup(PIRPin, GPIO.IN,pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(LEDPin, GPIO.OUT)

state = 0

def doorOpen(self):
  print('led will turn on')
  PIRreading = GPIO.input(PIRPin)
  
  
  try:
    while(PIRreading>0): #**** changed this to only do one rotation timing wise 
      global state
      if(state == 0):
        GPIO.output(LEDPin, state)
        
        state = 1
      elif (state == 1):
        GPIO.output(LEDPin, state)
        state = 0
      PIRreading = GPIO.input(PIRPin)
      time.sleep(.5)
    
  except KeyboardInterrupt:
    print("bye")
    
    
  

GPIO.add_event_detect(PIRPin, GPIO.FALLING, callback= doorOpen, bouncetime=100)

while(True):
  PIRreading = GPIO.input(PIRPin)
  print('waiting for edge detection, PIR Reading is: ', PIRreading)
  time.sleep(.1)
