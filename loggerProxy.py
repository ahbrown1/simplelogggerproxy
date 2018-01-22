#!/usr/bin/env python

'''
Provide one unique logger class with run-time
adjustable format. Supports multiple handlers.

'''

import logging
from logging import INFO

import sys
import uuid
import collections

class LoggerProxy(object) :
    def __init__( self, logger=None, name=None, format_str="%(message)s", level=logging.INFO) :

        if name is None:
            name =  str(uuid.uuid4())  #create a unique logger name
        self.__name =  name

        if logger is None :
            logger = logging.getLogger(self.__name)

        logger.setLevel(level)

        self.__logger = logger
        self.__handlers = []

        self.__format = format_str

    def getLogger(self) :
        return self

    def addHandler(self, hdlr) :
        '''
        save new handler in internal list as well as passing it to the actual logger
        '''
        formatter = logging.Formatter(self.__format)
        hdlr.setFormatter(formatter)
        self.__logger.addHandler(hdlr)
        self.__handlers.append(hdlr)

    def removeHandler(hdlr) :
        if hdlr in self.__handlers:
            self.__handlers.remove(hdlr)
            self.__logger.removeHandler(hdlr)

    def reformat( self, new_format) :
        '''
        Redo the format string for all handlers
        '''

        self.__format = new_format
        formatter = logging.Formatter(self.__format)
        for handler in self.__handlers :
            handler.setFormatter(formatter) # replace existing formatter

    def __getattr__(self, name):
        #catch-all : everything else invoked on the real logger object
        def method(*args):
            getattr(self.__logger, name )(args)
        return method

    @property
    def name(self) :
        return self._name

    @property
    def formatStr(self) :
        return self.__format

    @formatStr.setter
    def formatStr( self, newStr ) :
        #import pdb; pdb.set_trace()
        self.reformat( newStr)

def main() :
    logger = LoggerProxy()
    logger.addHandler(logging.StreamHandler(sys.stderr),)
    logger.info('HI')
    #import pdb; pdb.set_trace()
    pval = 12345
    logger.formatStr = "%(asctime)s %(levelname)s: {custom}: -- %(message)s".format(custom=pval)

    logger.info('HI')



if __name__ == '__main__' :
    sys.exit(main())
