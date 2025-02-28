from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)
servo.duty_u16(1803)
inc = 100
try:
    while True:
        for duty in range(1803, 7865, inc):
            servo.duty_u16(duty)
            sleep(0.01)
        for duty in range(7864, 1803, -inc):
            servo.duty_u16(duty)
            sleep(0.01)
except KeyboardInterrupt:
    servo.deinit()
    print('Keyboard Interrupt')