# main file to run
import RPi.GPIO as GPIO
import time
import requests
import sqlite3

# Database path for detections
db_file = "/home/birder/BirdNET-Pi/scripts/birds.db"

# servo
servo_pin = 16

# motors
IN3 = 17
IN4 = 27
ENA = 22

# We name all the pins on BOARD mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup GPIO
GPIO.setup([IN3, ENA, IN4, servo_pin], GPIO.OUT)

# servo pwm for setting angle
servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)

# motor pwm for setting speed
motor_pwm = GPIO.PWM(ENA, 100)
motor_pwm.start(25)

# ---------------------------------
# ------- SERVO FUNCTIONS ---------
# ---------------------------------

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    servo_pwm.ChangeDutyCycle(0)


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

# ---------------------------------
# ------- MOTOR FUNCTIONS ---------
# ---------------------------------

def flap_wings():
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    print("pin set to high")
    time.sleep(10)

    GPIO.output(IN3, GPIO.LOW)

# ---------------------------------
# ----- DATABASE FUNCTIONS --------
# ---------------------------------

def get_tables(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        return [table[0] for table in tables]
    except sqlite3.Error as e:
        print(f"Error occured: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


def count_detections(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM detections;")
        tables = cursor.fetchall()

        print("Detections found: " + tables[0][0])

        return [table[0] for table in tables]
    except sqlite3.Error as e:
        print(f"Error occured: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


# ---------------------------------
# -------- MAIN FUNCTION ----------
# ---------------------------------

def main():
    num_detections = count_detections(db_file)[0]
    while (True):
    time.sleep(1)
    if(count_detections(db_file)[0] > num_detections):
        print("Bird Found!")
        move_head()
        num_detections = count_detections(db_file)[0]


# stop pwms
servo_pwm.stop()
motor_pwm.stop()

# was having weird error so set PWM's to None so no delete destructor is called
servo_pwm = None
motor_pwm = None
GPIO.cleanup()
