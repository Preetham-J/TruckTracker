from threading import Thread
from threading import Timer
from ServerThread import ServerThread
import json
import random
import os

defaultTimeLimit = 30


def main():
    threads = {}
    while True:
        data = input("Enter JSON file\n")
        if data is not None:
            dataFile = open(data)
            newTruck = json.load(dataFile)
            dataFile.close()
            threads[newTruck["ID"]] = Thread(target=createMission, args=[newTruck])
            threads[newTruck["ID"]].start()


def createMission(jsonData):
    driverCode = random.randint(100000, 999999)
    print(driverCode)
    positionPath = jsonData["positionFile"]
    position = {
        "latitude": None,
        "longitude": None
    }
    codeFile = jsonData["codeFile"]
    requestCodeFile = jsonData["requestCodeFile"]
    mission = ServerThread(defaultTimeLimit, jsonData["ID"], driverCode, jsonData["startLocation"], jsonData["destination"], 0.0, 0.0)
    while True:
        receiveLocation(positionPath, position)
        mission.setLatitude(position["latitude"])
        mission.setLongitude(position["longitude"])
        print("hi1")
        check = mission.verifyLocation()
        print("hi2")
        if not check:
            inputCode = requestCode(mission.getTimeLimit(), mission, codeFile, requestCodeFile)
            mission.verifyCode(inputCode)


def receiveLocation(positionPath, previousPosition):
    while True:
        while True:
            try:
                positionFile = open(positionPath, "r")
                positionJson = json.load(positionFile)
                positionFile.close()
            except json.JSONDecodeError:
                print("Error reading file")
            else:
                break
        positionLatitude = positionJson["latitude"]
        positionLongitude = positionJson["longitude"]
        if (previousPosition["latitude"] != positionLatitude) or (previousPosition["longitude"] != positionLongitude):
            previousPosition["latitude"] = positionLatitude
            previousPosition["longitude"] = positionLongitude
            return


def requestCode(missionTimeLimit, mission, codeFile, requestCodeFile):
    timer = Timer(missionTimeLimit, mission.sendAlert)
    while not mission.alert:
        inputCode = receiveCode(codeFile, requestCodeFile)
        if len(inputCode) >= 1:
            timer.cancel()
            return inputCode[0]


def receiveCode(codeFile, requestCodeFile):
    startCodeFileTime = os.stat(codeFile).st_mtime
    with open(requestCodeFile, "w") as f:
        f.write("1")
    while True:
        currentCodeFileTime = os.stat(codeFile).st_mtime
        if startCodeFileTime != currentCodeFileTime:
            print("hello")
            f = open(codeFile, "r")
            lines = f.readlines()
            with open(requestCodeFile, "w") as f:
                f.write("0")
            return lines


if __name__ == "__main__":
    main()
