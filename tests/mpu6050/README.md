# MPU6050와 Raspberry Pi4와 연결

MPU6050은 6축 가속도 + 자이로의 기울기 센서로 자세 제어용으로 사용될 예정이다. 
자세한 정보는 [ElectronicWings의 MPU6050](https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi) 에 자세히 나온다. 

## 회로도
![circuit](MPU6050_interface_with_RaspberryPi.png)
<image source:ElectronicWings의 MPU6050>

## python
adafruit-circuitpython-mpu6050 라이브러리를 설치해 준다.
```
pip3 install adafruit-circuitpython-mpu6050
```

* python library source: https://github.com/adafruit/Adafruit_CircuitPython_MPU6050
* example: https://github.com/adafruit/Adafruit_CircuitPython_MPU6050/blob/main/examples/mpu6050_inclinometer.py
  * 이 소스가 ZX, ZY의 각도를 변환해서 출력해준다. 


### example
mpu6050_inclinometer.py
```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Display inclination data five times per second

# See this page to learn the math and physics principals behind this example:
# https://learn.adafruit.com/how-tall-is-it/gravity-and-acceleration

import time
from math import atan2, degrees
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_mpu6050.MPU6050(i2c)


# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees


def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)


while True:
    angle_xz, angle_yz = get_inclination(sensor)
    print("XZ angle = {:6.2f}deg   YZ angle = {:6.2f}deg".format(angle_xz, angle_yz))
    time.sleep(0.2)
```