import RPi.GPIO as GPIO
import time

# Pin Definitions
IN3 = 17
IN4 = 27
ENA = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup
GPIO.setup([IN3, ENA, IN4], GPIO.OUT)


# Forward

pwm = GPIO.PWM(ENA, 100)
pwm.start(25)

GPIO.output(IN4, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
print("pin set to high")
time.sleep(20)

# Stop
GPIO.output(IN3, GPIO.LOW)

pwm.stop()
GPIO.cleanup()
