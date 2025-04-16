import RPi.GPIO as GPIO
import time

# Pin Definitions
ENB = 2
IN3 = 3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup
motor_pins = [ENA, IN1, IN2, ENB, IN3, IN4]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)

# Optional: Enable PWM for speed control
pwm_b = GPIO.PWM(ENB, 100)
pwm_a.start(100)  # Full speed
pwm_b.start(100)

# Forward
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

time.sleep(2)

# Stop
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

pwm_a.stop()
pwm_b.stop()
GPIO.cleanup()
