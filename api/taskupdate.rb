#-*- coding: UTF-8 -*-
#Author:LTW
#This is the api for use in your program to update task information to a taskMonitor Server.
require 'socket'
require 'json'
require 'date'

=begin
Update your task to the server.

Sends an UDP message to the server with task informations.

@param taskName: A str, the name for your program task.
@param taskProgress: A number(int or float), the progress of your task.
@param taskInfo: A str, the detailed information about your task's current progress.
@param taskid: An object of any serializable type in JSON, this marks your task. And therefore you
    should **use a consistent one** during the program. To avoid collide, you can use the generate
    method below.
@param taskServer: A list of [ip address,port].
=end
def updateTask (taskName,taskProgress,taskInfo,taskid,taskServer=['127.0.0.1',4200])
    taskDict={
        "name"=>taskName,
        "progress"=>taskProgress,
        "info"=>taskInfo,
        "taskid"=>taskid
    }
    sock=UDPSocket.new
    sock.send(JSON.generate(taskDict),0,taskServer[0],taskServer[1])
end

=begin
Generate a task id that will hardly collide.

@return A taskID str.
=end
def generateTaskID
    return ((Time.now.to_datetime.strftime '%Q').to_i()/1000).to_s(16)+rand(0xffffff).to_s(16)
end