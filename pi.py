import RPi.GPIO as GPIO
import serial
import time

GPIO.setmode(GPIO.BCM)

buttons = {
    17: b'0',   # 0 degrees
    27: b'1',   # 90 degrees
    22: b'2'    # 180 degrees
}

for pin in buttons:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

try:
    while True:
        for pin, cmd in buttons.items():
            if GPIO.input(pin) == GPIO.LOW: 
                ser.write(cmd)
                time.sleep(0.25) 

finally:
    GPIO.cleanup()
    ser.close()
