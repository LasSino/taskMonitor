from templating import Templating

entryTemplate=Templating("templates/taskDataEntry.html")
fileTemplate=Templating("templates/taskdata.html")

tasklist=[
    {"name":"Hello","progress":15,"info":"Test 1"},
    {"name":"Hello","progress":99,"info":"Test 2"}
]

print (fileTemplate.render({"taskdataEntry":entryTemplate.renderList(tasklist)}))