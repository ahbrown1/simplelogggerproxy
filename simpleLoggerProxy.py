#!/usr/bin/env python
'''
Provide one unique logger class with run-time
adjustable format. Supports multiple handlers.

'''

import logging
import sys
import uuid
import collections

class SimpleLoggerProxy(object) :

    def __init__( self, name=None, handlers=None, format_str="%(message)s", level=logging.INFO) :

        if handlers is None:
            handlers = [logging.StreamHandler(sys.stderr)]
        elif not isinstance(handlers, collections.Iterable):
            handlers = [ handlers ]

        self.logger = None
        self.handlers = handlers
        self.__format_str = format_str
        self.level = level

        if name is None:
            name =  str(uuid.uuid4())  #create a unique logger name
        self._name =  name

    def getLogger(self):
        '''
        create the internal (logging class) logger
        '''
        if self.logger is None:
            self.logger = logging.getLogger(self.name) # create a unique logger
            self.logger.setLevel(self.level)
            formatter = logging.Formatter(self.__format_str)
            for handler in self.handlers :
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
        return self.logger

    def reformat( self, new_format) :
        '''
        Redo the format string for all handlers
        '''

        self.__format_str = new_format
        formatter = logging.Formatter(self.__format_str)
        for handler in self.handlers :
            handler.setFormatter(formatter) # replace existing formatter

    def __getattr__(self, name):
        #raise Exception('?')
        def method(*args):
            getattr(self.getLogger(), name )(args)
        return method

    @property
    def name(self) :
        return self._name

    @property
    def formatStr(self) :
        return self.__format_str

    @formatStr.setter
    def formatStr( self, newStr ) :
        self.reformat( newStr)

def main() :

    # so nice, say it twice
    handlers = [ logging.StreamHandler(sys.stderr), logging.StreamHandler(sys.stderr) ]

    logger = SimpleLoggerProxy(handlers=handlers)
    print logger.name
    print logger.formatStr

    logger.error('HEY!')

    # change the log output format
    logger.formatStr = "HERE: %(message)s"
    logger.error('HEY!')



if __name__ == '__main__' :
    sys.exit(main())
