
from classes import ADC



photoResistor= 0 #change as needed
ambientVal= 80
address= 0x48 #find device address
myADC= ADC(address)

photoResVal=myADC.read(0) #0 channel


while(True):
  if (photoResVal> ambientVal):
    photoResVal=myADC.read(0) #0 channel
    print('the first cond is true')
    print('the photo res is at: ', photoResVal)
  elif (photoResVal<= ambientVal):
    photoResVal=myADC.read(0) #0 channel
    print('the second cond it true: ', photoResVal)
