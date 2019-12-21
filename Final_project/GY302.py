#!/usr/bin/python
import smbus
import time
import sys
import os
import RPi.GPIO as GPIO
import DAN

GPIO.setmode(GPIO.BOARD)

# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21

num = 0
LED = 11
#GPIO.setup(LED,GPIO.OUT)

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

#Set IoTtalk
ServerURL = 'https://5.iottalk.tw/'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = 'GY30251536564778545355144543' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='GY302'
DAN.profile['df_list']=['light_level']
#DAN.profile['d_name']= 'Assign a Device Name' 
DAN.device_registration_with_retry(ServerURL, Reg_addr)


def convertToNumber(data):
  # change binary number to normal number 
  return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_2)
  return convertToNumber(data)

def main():

  while True:
    num = readLight()
    print ("Light Level : " + str(num) + " lx")
    DAN.push('light_level', str(num))
    time.sleep(0.2)
"""
    if num < 300:
       GPIO.output(LED,GPIO.HIGH)
    else:
       GPIO.output(LED,GPIO.LOW)
"""
    

if __name__=="__main__":
   main()
