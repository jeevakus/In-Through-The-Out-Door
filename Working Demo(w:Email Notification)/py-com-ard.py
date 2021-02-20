"""
Created on Fri Feb 19 2021

@author: In Through The Out Door
"""

"""Module importation"""
import serial
import time
import datetime
import serial
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""Initialization of capacity and cap_warning based on raw input data"""
capacity = int(input("What is your store capacity: "))
cap_warning = int(input("How close to your capacity do you want to be notified? (ex. 5 away from capacity): "))


previous_decoded_numPeople = []

"""Set up the serial line"""
ser = serial.Serial('COM3',9600)
time.sleep(2)
ser.flushInput()

"""Email Setup"""

email = 'makeuoft2021test@gmail.com'
password = 'insideout'
send_to_email = 'makeuoft2021test@gmail.com'

"""Define Send Email Function for Over Capacity"""
def send_email():
        subject = 'Over Capacity!'

        msg = MIMEMultipart()
        msg['FROM'] = email
        msg['TO'] = send_to_email
        msg['SUBJECT'] = subject

        message = 'The store is over capacity! \n' + (datetime.datetime.now()).strftime(
            "%d-%b-%Y (%H:%M:%S.%f)")

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("makeuoft2021test@gmail.com", "insideout")

"""Define Send Email Function for At Capacity"""
def send_email_cap():
        subject = 'At Capacity!'

        msg = MIMEMultipart()
        msg['FROM'] = email
        msg['TO'] = send_to_email
        msg['SUBJECT'] = subject

        message = 'You are at capacity! You do not want to go over your limit of ' + str(capacity) + "\n" + (datetime.datetime.now()).strftime(
            "%d-%b-%Y (%H:%M:%S.%f)")

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("makeuoft2021test@gmail.com", "insideout")

"""Define Send Email Function for Close To Capacity"""
def send_email_close():
        subject = str(cap_warning)+' away from capacity!'

        msg = MIMEMultipart()
        msg['FROM'] = email
        msg['TO'] = send_to_email
        msg['SUBJECT'] = subject

        message = 'You are approaching your limit for customers in the store. Keep a look out to not go over! You have ' +str(cap_warning)+ ' spots remaining \n ' + (datetime.datetime.now()).strftime(
            "%d-%b-%Y (%H:%M:%S.%f)")

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("makeuoft2021test@gmail.com", "insideout")

"""Read Streaming Data from Arduino using Serial Port Communication"""            
while True:
    try:
        ser_bytes = ser.readline()
        current_decoded_numPeople = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        previous_decoded_numPeople.append(current_decoded_numPeople) 
        if current_decoded_numPeople != previous_decoded_numPeople[-2]:
            print(current_decoded_numPeople)
    """Function Send Email call to corresponding case"""
    except:
        continue
    if (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (current_decoded_numPeople == capacity):
        print("At Capacity")
        send_email_cap()
    elif  (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (capacity > current_decoded_numPeople >= (capacity - cap_warning)):
        print("Reaching capacity", (capacity - current_decoded_numPeople), "spots remain")
        if(current_decoded_numPeople==capacity-cap_warning):
                send_email_close()
    elif (current_decoded_numPeople != previous_decoded_numPeople[-2]) and (current_decoded_numPeople > capacity):
        print("Over Capacity")
        send_email()

