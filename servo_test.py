# We imports the GPIO module
import RPi.GPIO as GPIO
# We import the command sleep from time
import time

# Stops all warnings from appearing
GPIO.setwarnings(False)
servo_pin = 16

# We name all the pins on BOARD mode
GPIO.setmode(GPIO.BCM)
# Set an output for the PWM Signal
GPIO.setup(16, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)

pwm.start(0)
def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)


def move_head():
    count = 0
    try:
        while count < 6:
            angle = 65
            if 0 <= angle <= 180:
                set_angle(20)
                set_angle(180)
                count += 1
                print(count)
            else:
                print("Angle must be between 0 and 180")
    except KeyboardInterrupt:
        pass

pwm.stop()
GPIO.cleanup()
