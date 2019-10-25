'''
PURPOSE:
Voltage Sensor on Raspberry Pi sending real-time voltage data to firebase

COMMAND:
python3 voltageSensor.py

AUTHORS:
   Mikian Musser      - https://github.com/mm909
   Eric Becerril-Blas - https://github.com/lordbecerril
   Zoyla Orellana     - https://github.com/ZoylaO
   Austin Janushan    - https://github.com/Janushan-Austin
   Giovanny Vazquez   - https://github.com/giovannyVazquez
   Ameera Essaqi      - https://github.com/AmeeraE
   Brandon Herrera    - herrer10@unlv.nevada.edu
   Esdras Morales     - morale2@unlv.nevada.edu

ORGANIZATION:
   Dook Robotics - https://github.com/dook-robotics

'''
mport time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from firebase import firebase

firebase = firebase.FirebaseApplication('https://dook-726e9.firebaseio.com/')
R1 = 10000
R2 = 1000
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
#chan1 = AnalogIn(ads, ADS.P1)
#chan2 = AnalogIn(ads, ADS.P3)
# Create differential input between channel 0 and 3
#chan = AnalogIn(ads, ADS.P0, ADS.P3)
print("{:>5}\t{:>5}".format('raw', 'Vout'))
while True:
#batteryVoltage = chan0.voltage*((R1+R2)/R2)
#motor1Current = (chan1.voltage - 2.55)*10
#motor2Current = (chan2.voltage - 2.55)*10
#print("{:>5}\t{:>5.3f}\t{:>5.3f}".format(chan0.value, chan0.voltage, batteryVoltage))
#print("motor1: {:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
#print("motor2: {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
#print("motor1: {:>5}\t{:>5.3f}".format(chan1.value, motor1Current))
#print("motor2: {:>5}\t{:>5.3f}".format(chan2.value, motor2Current))
print("V: {:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
result = firebase.post('https://dook-726e9.firebaseio.com/',{'voltage':int(chan0.voltage)})
time.sleep(0.1)
