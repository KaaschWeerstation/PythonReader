from mmap import *
# https://docs.python.org/3/library/mmap.html
# https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte/20014805#20014805

def bytesToInt(bytes):
    return int.from_bytes(bytes, byteorder="big")

if __name__ == '__main__':
    with open("81400/18281.wd", "rb", 0) as f, mmap(f.fileno(), 0, access=ACCESS_READ) as s:
        print("SerialVersion: " + str(bytesToInt(s[0:8])))
        print("StationId: " + str(bytesToInt(s[8:12])))
        print("Date: " + str(bytesToInt(s[12:20])))
        index = 20
        size = s.size()
        while index+49 <= s.size():
            print("\n")
            print("Time: " + str(bytesToInt(s[index:index+8])))
            print("Temperature: " + str(bytesToInt(s[index+8:index+12])/100))
            print("Dew: " + str(bytesToInt(s[index+12:index+16])))
            print("PressureSeaLevel: " + str(bytesToInt(s[index+16:index+20])))
            print("Visibility: " + str(bytesToInt(s[index+20:index+24])))
            print("PressureStation: " + str(bytesToInt(s[index+24:index+28])))
            print("Wind: " + str(bytesToInt(s[index+28:index+32])))
            print("Precipictation: " + str(bytesToInt(s[index+32:index+36])))
            print("Snow: " + str(bytesToInt(s[index+36:index+40])))
            print("Events: " + str(bytesToInt(s[index+40:index+41])))
            print("Cloudcoverage: " + str(bytesToInt(s[index+41:index+45])))
            print("WindDirection: " + str(bytesToInt(s[index+45:index+49])))
            index += 49



