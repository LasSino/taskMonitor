import web
from templating import Templating
from tasklist import tasks

entryTemplate=Templating("templates/taskdataentry.html")
fileTemplate=Templating("templates/taskdata.html")

class HttpHandler:
    def GET(self):
        return fileTemplate.render({"taskdataEntry":entryTemplate.renderList(tasks.values())})