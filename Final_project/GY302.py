#!/usr/bin/python
import smbus
import time
import sys
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address

ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21

num = 0
LED = 11
#GPIO.setup(LED,GPIO.OUT)

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

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
    time.sleep(0.2)
"""
    if num < 300:
       GPIO.output(LED,GPIO.HIGH)
    else:
       GPIO.output(LED,GPIO.LOW)
"""
    

if __name__=="__main__":
   main()
