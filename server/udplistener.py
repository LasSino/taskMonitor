from twisted.internet.protocol import DatagramProtocol
from tasklist import tasks,refreshTaskList
import json
from time import time

class UdpListener(DatagramProtocol):
    def datagramReceived(self, datagram, addr):
        jsonStr=str(datagram,encoding="utf8")
        task=json.loads(jsonStr)
        task["time"]=int(time())
        tasks[task["taskid"]]=task
        print(tasks)
        refreshTaskList()
        return