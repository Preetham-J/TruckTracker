from threading import Thread
from threading import Timer
from ServerThread import ServerThread
import json
import random

defaultTimeLimit = 30


def main():
    threads = {}
    while True:
        data = input("Enter JSON file\n")
        if data is not None:
            newTruck = json.load(open(data))
            threads[newTruck["ID"]] = Thread(target=createMission, args=[newTruck])
            threads[newTruck["ID"]].start()


def createMission(jsonData):
    driverCode = random.randint(1, 100000)
    mission = ServerThread(defaultTimeLimit, jsonData["ID"], driverCode, jsonData["startLocation"], jsonData["destination"], 0.0, 0.0)
    while True:
        position = receiveLocation()
        mission.setLatitude(position["latitude"])
        mission.setLongitude(position["longitude"])
        check = mission.verifyLocation()
        if not check:
            inputCode = requestCode(mission.getTimeLimit(), mission)
            mission.verifyCode(inputCode)


def receiveLocation():
    position = {
        "latitude": None,
        "longitude": None
    }
    
    return position


def requestCode(missionTimeLimit, mission):
    timer = Timer(missionTimeLimit, mission.sendAlert)
    while not mission.alert:
        inputCode = receiveCode()
        if inputCode is not None:
            timer.cancel()
            return inputCode


# TODO: Ping driver
def receiveCode():
    return input("\nPlease enter your code: ")


if __name__ == "__main__":
    main()


# def main():
#     threads = {}
#     while True:
#         data = input("Enter JSON file\n")
#         if data is not None:
#             newTruck = json.load(open(data))
#             threads[newTruck["ID"]] = Thread(target=runTest, args=[newTruck["ID"]])
#             threads[newTruck["ID"]].start()
#
#
# class Test:
#     def __init__(self, testString):
#         self.testString = testString
#
#     def printTestString(self):
#         print("\nTruck ID is: %d", self.testString)
#
#
# def runTest(testString):
#     time.sleep(10)
#     test = Test(testString)
#     test.printTestString()
