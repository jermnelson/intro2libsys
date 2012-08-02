__author__ = "Jeremy Nelson"
import json,sys
from django.contrib.auth.models import User
import intro.settings as settings
import datetime
from docutils.core import publish_string
from bs4 import BeautifulSoup
import os,sys,re


def build_loader(chapter_loader,directory):
    chapter_walker = os.walk(directory)
    next(chapter_walker)
    for row in chapter_walker:
        path,filenames = row[0],row[2]
        month = os.path.split(path)[1]
        for filename in filenames:
            name,ext = os.path.splitext(filename)
            if ext.count('rst') < 0:
                pass
            raw_file = open(os.path.join(path,filename),'rb')
            raw_rst = raw_file.read()
            raw_file.close()
            rst_contents = publish_string(raw_rst,
                                          writer_name="html")
            rst_soup = BeautifulSoup(rst_contents)
            main_contents = rst_soup.find("div",attrs={"class":"document"})
            pretty_html = main_contents.prettify()
            chapter_loader[name] = {'html':pretty_html}                                                                                   
    return chapter_loader
    
class BookLoader(object):
    chapter_mapping = {'one':1,
                       'two':2,
                       'three':3,
                       'four':4,
                       'five':5,
                       'six':6,
                       'seven':7,
                       'eight':8,
                       'nine':9,
                       'ten':10,
                       'eleven':11}

    def __init__(self,doc_path=None):
        self.book_path = doc_path
        if self.book_path is None:
            self.book_path = os.path.join(settings.DJANGO_ROOT,'doc')
        self.chapters = {}
        self.appendices = []
        print(self.book_path)
        self.load()

    def load(self):
        doc_walker = os.walk(self.book_path)
        next(doc_walker)
        for row in doc_walker:
            path,filenames = row[0],row[2]
            name = os.path.split(path)[-1]
            self.chapters[name] = {}
            if re.search(r"chapters",path):
                for filename in filenames:
                    page_key,ext = os.path.splitext(filename)
                    if ext.count('rst') > -1:
                        rst_path = os.path.join(path,filename)
                        self.chapters[name][page_key] = {'html':self.__get_contents__(rst_path)}
            if re.search(r"appendices",path):
                for filename in filenames:
                    file_key,ext = os.path.splitext(filename)
                    if ext.count('rst') > -1:
                        rst_path = os.path.join(path,filename)
                        appendix = self.__get_contents__(rst_path)
                        self.appendices.append(dict(file_key = {'html':appendix}))
                        

    def __get_contents__(self,rst_location):
        raw_file = open(rst_location,'rb')
        raw_rst = raw_file.read()
        raw_file.close()
        rst_contents = publish_string(raw_rst,
                                      writer_name="html")
        rst_soup = BeautifulSoup(rst_contents)
        main_contents = rst_soup.find("div",attrs={"class":"document"})
        return main_contents.prettify()
            

        
        

if __name__ == '__main__':
    pass
