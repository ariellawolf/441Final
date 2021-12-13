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


servo.start(dcMin)
print('in try statement')  
servo.ChangeDutyCycle(3)
time.sleep(.5)
servo.ChangeDutyCycle(6)
time.sleep(.5)
servo.ChangeDutyCycle(9)
time.sleep(5)
servo.ChangeDutyCycle(6)
time.sleep(.5)
servo.ChangeDutyCycle(3)
time.sleep(.5)