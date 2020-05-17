from twisted.internet import reactor
import web
import sys
import signal
from httphandler import HttpHandler
from udplistener import UdpListener
import httpthread

app=None

def ctrlchandler(signum,_):
    reactor.stop()
    app.stop()

if __name__ == '__main__':
    signal.signal(signal.SIGTERM,ctrlchandler)
    signal.signal(signal.SIGINT,ctrlchandler)
    urls = ("/tasks", "HttpHandler")
    app = web.application(urls,globals())
    t1=httpthread.HTTPThread(app)
    #t1.setDaemon(True)
    t1.start()
    reactor.listenUDP(4200,UdpListener())
    reactor.run()
