import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

PIRPin= 5 #change this as needed- this connects to alarm pin (low if something is detected)
servoPin= 13 #change this as needed
GPIO.setup(PIRPin, GPIO.IN,pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(servoPin, GPIO.OUT)
dcMin = 2 #this may need to be changed
dcMax = 12 #this may need to be changed
servo= GPIO.PWM(servoPin, 50) #50 Hz

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
  

GPIO.add_event_detect(PIRPin, GPIO.RISING, callback= doorOpen, bouncetime=100)

while(True):
  PIRreading = GPIO.input(PIRPin)
  print('waiting for edge detection, PIR Reading is: ', PIRreading)
  time.sleep(.1)
