import time

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)
pca.frequency = 50




def init_servos(count):
    servos = list()
    for i in range(count):
        # DS3218 pulse rage is 400 ~ 2400
        s = servo.Servo(pca.channels[i], min_pulse=400, max_pulse=2400)
        servos.append(s)
    return servos

def setAllAngle(svs, angle):
    for s in svs:
        s.angle = angle

def setAllFraction(svs, fraction):
    for s in svs:
        s.fraction = fraction


motors = init_servos(12)


# calibrate
setAllAngle(motors, 45)
time.sleep(1)
setAllAngle(motors, 90)
time.sleep(1)
setAllAngle(motors, 125)
time.sleep(1)
setAllAngle(motors, 180)
time.sleep(1)
setAllAngle(motors, 0)
time.sleep(0.03)

for i in range(180):
    setAllAngle(motors, i)
    time.sleep(0.03)

for i in range(180):
    setAllAngle(motors, 180 - i)
    time.sleep(0.03)

fraction = 0.0
while fraction < 1.0:
    setAllFraction(motors, fraction)
    fraction += 0.01
    time.sleep(0.03)

pca.deinit()
