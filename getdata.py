import csv
import math
from mmap import *
from datetime import *


def bytesToInt(bytes):
    return int.from_bytes(bytes, byteorder="big", signed=True)


def humidty(temperature, dewPoint):
    actualVapourPressure = math.exp((17.625 * dewPoint) / (243.04 + dewPoint))
    standardVapourPressure = math.exp((17.625 * temperature) / (243.04 + temperature))
    return round(actualVapourPressure / standardVapourPressure * 100, 1)


def getData(stationID, filename):
    with open("venv/" + str(stationID) + "/" + str(filename) + ".csv", 'w', newline='') as wd:
        writer = csv.writer(wd)
        writer.writerow(["Time", "Temperature", "Humidity"])
        with open("venv/" + str(stationID) + "/" + str(filename) + ".wd", "rb", 0) as f, mmap(f.fileno(), 0,
                                                                                              access=ACCESS_READ) as s:
            mDate = datetime(1970, 1, 1, 0, 0) + timedelta(bytesToInt(s[12:20]))
            index = 20

            while index + 23 <= s.size():
                temperature = bytesToInt(s[index + 4:index + 6]) / 100
                dewPoint = round((bytesToInt(s[index + 4:index + 6]) / 100 + bytesToInt(s[index + 6:index + 7]) / 10),
                                 1)
                fullDate = mDate + timedelta(seconds=(bytesToInt(s[index:index + 4])))
                timeData = fullDate.strftime("%d-%m-%Y %H:%M:%S")
                writer.writerow([timeData, temperature, humidty(temperature, dewPoint)])

                index += 23

        f.close()
    wd.close()