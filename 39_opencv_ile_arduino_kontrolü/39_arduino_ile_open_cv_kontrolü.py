import serial
import time

arduino=serial.Serial('COM5',9600)
time.sleep(2)

print("ENTER1 TO TURN ON LED AND 0 TO TURN OFF LED")

while 1:
    datafromUser=input()

    if datafromUser=='1':
        arduino.write(b'1')
        print("LED TURNED ON")
    elif datafromUser=='0':
        arduino.write(b'0')
        print("LED TURNED OFF")