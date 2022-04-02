import serial
import time

class Connection:
    def __init__(self):
        self.arduino = self.get_connection()
    
    def get_connection(self):
        try:
            arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=15)
            #time.sleep(1)
            return arduino

        except:
            return None

    def read_data(self):
        try:
            data = self.arduino.readline()
            #time.sleep(1)
            info = ""

            for d in data:
                info += chr(d)
            
            return str(info).split(",")

        except:
            return ""

    def send_data(self):
        try:
            self.arduino.write(b'1')
            return True

        except:
            return False





