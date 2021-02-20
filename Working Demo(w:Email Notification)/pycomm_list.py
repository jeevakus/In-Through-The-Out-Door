"""
Created on Fri Feb 19 2021

@author: TeamName
"""

"""Module importation"""
import serial
import time

"""Initialization of capacity"""
capacity = 20
previous_decoded_numPeople = []

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
        print("At Capacity")
    elif  (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (capacity > current_decoded_numPeople >= (capacity - 5)):
        print("Reaching capacity", (capacity - current_decoded_numPeople), "spots remain")
    elif (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (current_decoded_numPeople > capacity):
        print("Over Capacity")

