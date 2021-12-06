import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

PIRPin= 5 #change this as needed- this connects to alarm pin (low if something is detected)
servoPin= 13 #change this as needed
GPIO.setup(PIRPin, GPIO.IN,pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(servoPin, GPIO.OUT)
dcMin = 3 #this may need to be changed
dcMax = 12 #this may need to be changed
servo= GPIO.PWM(servoPin, 50) #50 Hz

def doorOpen(self):
  servo.start(0)
  print('servo started')
  try:
    while(True): #**** changed this to only do one rotation timing wise 
      for dc in range(dcMin,dcMax):
        servo.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(0.5)
  except KeyboardInterrupt:
    print("bye")
    servo.stop()
  GPIO.cleanup()

GPIO.add_event_detect(PIRPin, GPIO.RISING, callback= doorOpen, bouncetime=100)

while(True):
  PIRreading = GPIO.input(PIRPin)
  print('waiting for edge detection, PIR Reading is: ', PIRreading)
  time.sleep(.5)
