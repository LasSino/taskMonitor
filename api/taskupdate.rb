require 'socket'
require 'json'
require 'date'

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

def generateTaskID
    return ((Time.now.to_datetime.strftime '%Q').to_i()/1000).to_s(16)+rand(0xffffff).to_s(16)
end