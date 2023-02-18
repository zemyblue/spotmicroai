# MPU6050와 Raspberry Pi4와 연결

MPU6050은 6축 가속도 + 자이로의 기울기 센서로 자세 제어용으로 사용될 예정이다. 
자세한 정보는 [ElectronicWings의 MPU6050](https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi) 에 자세히 나온다. 

## 회로도
![circuit](./MPU6050_interface_with_RaspberryPi.png)
<image source:ElectronicWings의 MPU6050>

## python
adafruit-circuitpython-mpu6050 라이브러리를 설치해 준다.
```
pip3 install adafruit-circuitpython-mpu6050
```

* python library source: https://github.com/adafruit/Adafruit_CircuitPython_MPU6050
* example: https://github.com/adafruit/Adafruit_CircuitPython_MPU6050/blob/main/examples/mpu6050_inclinometer.py
  * 이 소스가 ZX, ZY의 각도를 변환해서 출력해준다. 