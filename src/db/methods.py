import sqlite3
import json
import base64
import cv2
from src.common.constants import read_data, table_name, db_name

def write_coordinates(x, y, pic):
    """Write the coordinates and the picture in database"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    #cursor.execute()
    data_tuple = (x, y, pic)
    cursor.execute("INSERT INTO {0} VALUES (?, ?, ?)".format(table_name), data_tuple)
    connection.commit()


def read_coordinates():
    """Read from db the coordinates and coresponding pictures"""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    rows = cursor.execute(read_data).fetchall()
    return rows

def read_single_record(num):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    row = cursor.execute("SELECT * FROM {0} LIMIT {1} OFFSET {2}".format(table_name, num, int(num)+1)).fetchall()
    pic_data = []
    pic_data.append(row[0][0])
    pic_data.append(row[0][1])
    pic_data.append(str(base64.b64encode(row[0][2])))
    return pic_data
