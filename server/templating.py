# -*- coding: utf-8 -*-
#Author:LTW

'''
This is a simple templating engine.It is based on str.format.

This is rudimentary and is not suitable for too complex use.
The HTML escape support is now removed because it's useless.
'''
class Templating:
    def __init__(self,filename):
        file=open(filename,'r',encoding="utf8")
        self.__template=file.read()
        file.close()

    def render(self,argDict):
        return self.__template.format(**argDict)
    
    def renderList(self,dictList):
        return "\n".join(map(lambda x:self.__template.format(**x),dictList))