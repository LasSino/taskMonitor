import httpthread
from twisted.internet import reactor
from udplistener import UdpListener
import web
from httphandler import HttpHandler


if __name__ == '__main__':
	urls = ("/tasks", "HttpHandler")
	app = web.application(urls,globals())
	t1=httpthread.HTTPThread(app)
	t1.start()
	reactor.listenUDP(4200,UdpListener())
	reactor.run()

