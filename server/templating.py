
class Templating:
    def __init__(self,filename):
        file=open(filename,'r',encoding="utf8")
        self.__template=file.read()
        file.close()

    def render(self,argDict):
        return self.__template.format(**argDict)
    
    def renderList(self,dictList):
        return "\n".join(map(lambda x:self.__template.format(**x),dictList))