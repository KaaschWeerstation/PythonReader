from mmap import *
from datetime import *
# https://docs.python.org/3/library/mmap.html
# https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte/20014805#20014805

def bytesToInt(bytes):
    return int.from_bytes(bytes, byteorder="big",signed=True)

if __name__ == '__main__':
    with open("venv/10490/18282.wd", "rb", 0) as f, mmap(f.fileno(), 0, access=ACCESS_READ) as s:
        print("SerialVersion: " + str(bytesToInt(s[0:8])))
        print("StationId: " + str(bytesToInt(s[8:12])))
        mDate = datetime(1970, 1, 1, 0, 0) + timedelta(bytesToInt(s[12:20]) - 1)
        print("Date: " + mDate.strftime("%d-%m-%Y"))
        index = 20
        size = s.size()
        while index+52 <= s.size():

            fullDate = mDate + timedelta(seconds=(bytesToInt(s[index:index+8])))
            print("\nTime: " + fullDate.strftime("%d-%m-%Y %H:%M:%S"))

            print("Temperature: " + str(bytesToInt(s[index+8:index+12])/100))
            print("Dew: " + str(bytesToInt(s[index+12:index+16])/100))
            print("PressureSeaLevel: " + str(bytesToInt(s[index+16:index+20])/100))
            print("Visibility: " + str(bytesToInt(s[index+20:index+24])/100))
            print("PressureStation: " + str(bytesToInt(s[index+24:index+28])/100))
            print("Wind: " + str(bytesToInt(s[index+28:index+32])/100))
            print("Precipictation: " + str(bytesToInt(s[index+32:index+36])/100))
            print("Snow: " + str(bytesToInt(s[index+36:index+40])/100))
            print("Events: " + str(bytesToInt(s[index+40:index+44])))
            print("Cloudcoverage: " + str(bytesToInt(s[index+44:index+48])/100))
            print("WindDirection: " + str(bytesToInt(s[index+48:index+52])/100))
            index += 52



