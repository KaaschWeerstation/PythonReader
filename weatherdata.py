import csv
import math
from mmap import *
from datetime import *

from os import listdir
from os.path import isfile, join


def bytesToInt(bytes):
    return int.from_bytes(bytes, byteorder="big", signed=True)


def humidty(temperature, dewPoint):
    actualVapourPressure = math.exp((17.625 * dewPoint) / (243.04 + dewPoint))
    standardVapourPressure = math.exp((17.625 * temperature) / (243.04 + temperature))
    return round(actualVapourPressure / standardVapourPressure * 100, 1)


def getData(stationID, filename, country):
    with open("venv/" + str(stationID) + "/" + str(filename), "rb", 0) as f, mmap(f.fileno(), 0, access=ACCESS_READ) as s:
        mDate = datetime(1970, 1, 1, 0, 0) + timedelta(bytesToInt(s[12:20]))
        index = 20
        stationData = {}
        i = 1

        while index + 23 <= s.size():
            temperature = bytesToInt(s[index + 4:index + 6]) / 100
            dewPoint = round((bytesToInt(s[index + 4:index + 6]) / 100 + bytesToInt(s[index + 6:index + 7]) / 10),
                             1)
            fullDate = mDate + timedelta(seconds=(bytesToInt(s[index:index + 4])))
            timeData = fullDate.strftime("%d-%m-%Y %H:%M:%S")
            stationData[i] = {'country': country, 'time': timeData, 'temperature': temperature, 'humidity': humidty(temperature, dewPoint)}
            # print(stationData)
            i += i
            index += 23
    f.close()
    return stationData


def getWeatherData():
    with open("csv/weatherdata.csv", 'w', newline='') as wd:
        writer = csv.writer(wd)
        writer.writerow(["Country", "Time", "Temperature", "Humidity"])
        with open('csv/stationid.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].isdigit():
                    files = [f for f in listdir("venv/"+str(row[0])) if isfile(join("venv/"+str(row[0]), f))]
                    for file in files:
                        dataDict = getData(row[0], file, row[1])
                        for data in dataDict:
                            writer.writerow([dataDict[data]['country'], dataDict[data]['time'], dataDict[data]['temperature'], dataDict[data]['humidity']])
        f.close()
    wd.close

getWeatherData()