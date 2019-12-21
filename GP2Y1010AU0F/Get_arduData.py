import serial
import DAN

ServerURL = 'https://5.iottalk.tw/'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = 'getarduinof5153656463585145144543' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='0858812_final'
DAN.profile['df_list']=['dust']
#DAN.profile['d_name']= 'Assign a Device Name' 
DAN.device_registration_with_retry(ServerURL, Reg_addr)


ser = serial.Serial('/dev/ttyACM0', 9600)

while 1: 
    if(ser.in_waiting >0):
        
        line = ser.readline()
        DAN.push('dust',line)
        print(line)

