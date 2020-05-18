# -*- coding: utf-8 -*-
from time import time

'''A global var. The task list.
'''
tasks={
}

def refreshTaskList():
    '''This refershes the task list.

    This function removes the finished and outdated tasks from the task list.
    It also removed the seemingly aborted task from the list. 
    This applies to the tasks that are not updated for a week.

    As you can see, this is passively called when new updates are made to the tasks.
    '''
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