import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

photoResistor= 0 #change as needed
ambientVal= 100 #change depending on room lighting
address= 0x48 #find device address



GPIO.setup(photoResistor, GPIO.IN)
stepperPins = [23,24,16,20] # controller inputs: in1, in2, in3, in4
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
      time.sleep(1)
except Exception as e:
  print(e)