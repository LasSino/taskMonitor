from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from tasklist import tasks
import json
from time import time

def refreshTaskList():
    remove=[]
    for task in tasks.values():
        if int(time())-task["time"]>=604800:
            remove.append(task["taskid"])
        if task["progress"]>=100:
            if "time" in task:
                if int(time())-task["time"]>=3600:
                    remove.append(task["taskid"])
            else:
                remove.append(task["taskid"])
    for toRemove in remove:
        del tasks[toRemove]

class UdpListener(DatagramProtocol):
    def datagramReceived(self, datagram, addr):
        jsonStr=str(datagram,encoding="utf8")
        task=json.loads(jsonStr)
        task["time"]=int(time())
        tasks[task["taskid"]]=task
        print(tasks)
        refreshTaskList()
        return