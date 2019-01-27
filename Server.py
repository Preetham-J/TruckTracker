from threading import Thread
from ServerThread import ServerThread
import json
import random

timeLimit = 30


def main():
    threads = {}
    while True:
        data = input("Enter JSON file\n")
        if data is not None:
            newTruck = json.load(open(data))
            threads[newTruck["ID"]] = Thread(target=createMission, args=[newTruck])
            threads[newTruck["ID"]].start()


def createMission(jsonData):
    code = random.randint(1, 100000)
    mission = ServerThread(timeLimit, jsonData["ID"], code, jsonData["startLocation"], jsonData["destination"], 0.0, 0.0)


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
