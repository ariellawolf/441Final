import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

stepperPins = [19,26,27,22] # controller inputs: in1, in2, in3, in4
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
for pin in stepperPins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

try:
    while(True):
      print('in while loop')
      for state in range(8):
        for pin in range(4):
          GPIO.output(stepperPins[pin], sequence[state][pin])
        delay_us(1000)
      time.sleep(1)
except Exception as e:
  print(e)