import threading

class HTTPThread(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app=app

    def run(self):
        self.app.run()
