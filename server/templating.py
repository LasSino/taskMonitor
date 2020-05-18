# -*- coding: utf-8 -*-
#Author:LTW

'''
This is a simple templating engine.It is based on str.format and html.escape.

This is rudimentary and is not suitable for too complex use.
This templating system now supports html escape using html.escape.
'''
import html
class Templating:
    def __init__(self,filename):
        file=open(filename,'r',encoding="utf8")
        self.__template=file.read()
        file.close()

    def render(self,argDict):
        return html.escape(self.__template.format(**argDict))
    
    def renderList(self,dictList):
        return html.escape("\n".join(map(lambda x:self.__template.format(**x),dictList)))