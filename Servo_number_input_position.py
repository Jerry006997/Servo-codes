from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)
servo.duty_16(1803)
try:
    while True:
        pos = input('Enter a number between 1803 and 7864')
        pos = int(pos)
        servo.duty_u16(pos)
        sleep(0.01)
except KeyboardInterrupt:
    servo.deinit()
    print('Keyboard Interrupt')