import requests
import sqlite3
import time
from servo_test import move_head

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

        return [table[0] for table in tables]
    except sqlite3.Error as e:
        print(f"Error occured: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()




db_file = "/home/birder/BirdNET-Pi/scripts/birds.db"

num_detections = count_detections(db_file)[0]
while (True):
    time.sleep(1)
    if(count_detections(db_file)[0] > num_detections):
        print("Found new detection!")
        move_head()
        num_detections = count_detections(db_file)[0]


