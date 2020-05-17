# -*- coding: utf-8 -*-
'''
@author LTW
@desc This is the api for use in your program to update task information to a taskMonitor Server.

function: updateTask(),generateTaskID(),getTaskID()
data:__taskID
'''
import socket
import json
import time
import random

def updateTask(taskName,taskProgress,taskInfo,taskid,taskServer=('127.0.0.1',4200)):
    '''Update your task to the server.

    Sends an UDP message to the server with task informations.

    @param taskName: A str, the name for your program task.
    @param taskProgress: A number(int or float), the progress of your task.
    @param taskInfo: A str, the detailed information about your task's current progress.
    @param taskid: An object of any serializable type in JSON, this marks your task. And therefore you
        should **use a consistent one** during the program. To avoid collide, you can use the generate
        method below.
    @param taskServer: A tuple of (str,int), the server ip information in python socket format.
    '''
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock:
        datadict={"name":taskName,"progress":taskProgress,"info":taskInfo,"taskid":taskid}
        jsonStr=json.dumps(datadict)
        data=bytes(jsonStr,"utf8")
        sock.sendto(data,taskServer)
       
def generateTaskID():
    '''Generate a task id that will hardly collide.

    @return A taskID str.
    '''
    return hex(int(time.time()))[2:]+hex(random.randint(0,0xffffff))[2:]
