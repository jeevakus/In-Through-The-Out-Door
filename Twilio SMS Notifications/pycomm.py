"""
Created on Fri Feb 19 2021

@author: TeamName
"""

"""Module importation"""
import serial
from send_sms import *

"""Initialization of capacity"""
capacity = 20

"""Message Initialization"""
m1 = "At Capacity"
m2 = "Reaching Capacity: " + str(capacity - current_decoded_numPeople) + " spots remain"
m3 = "Over Capacity: " + str(current_decoded_numPeople - capacity) 

"""Set up the serial line"""
ser = serial.Serial('COM3',9600)
time.sleep(2)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        current_decoded_numPeople = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        previous_decoded_numPeople.append(current_decoded_numPeople) 
        if current_decoded_numPeople != previous_decoded_numPeople[-2]:
            print(current_decoded_numPeople)

    except:
        continue
    if (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (current_decoded_numPeople == capacity):
        call(m1)
    elif  (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (capacity > current_decoded_numPeople >= (capacity - 5)):
        call(m2)
    elif (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (current_decoded_numPeople > capacity):
        call(m3)

