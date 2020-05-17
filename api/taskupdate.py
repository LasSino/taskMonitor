
import socket
import json
import time
import random

def updateTask(taskName,taskProgress,taskInfo,taskid,taskServer=('127.0.0.1',4200)):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock:
        datadict={"name":taskName,"progress":taskProgress,"info":taskInfo,"taskid":taskid}
        jsonStr=json.dumps(datadict)
        data=bytes(jsonStr,"utf8")
        sock.sendto(data,taskServer)
       
def generateTaskID():
    return hex(int(time.time()))[2:]+hex(random.randint(0,0xffffff))[2:]

__taskID=generateTaskID()

def getTaskID():
    return __taskID