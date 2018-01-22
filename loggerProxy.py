import logging
import sys
import uuid

class LoggerProxy(object) :
    def __init__( self, name=None, logger=None, format_str="%(message)s", level=logging.INFO) :

        if name is None:
            name =  str(uuid.uuid4())  #create a unique logger name
        self._name =  name

        if logger is None:
            print type(self.name)
            logger = logging.getLogger(self.name)

        logger.setLevel(level)

        self.logger = logger
        self.handlers = []

        self.__format = format_str

    def getLogger(self) :
        return self

    def addHandler(self, hdlr) :
        formatter = logging.Formatter(self.__format_str)
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.handlers.append(hdlr)

    def removeHandler(hdlr) :
        if hdlr in self.handlers:
            self.handlers.remove(hdlr)
            logger.removeHandler(hdlr)

    def reformat( self, new_format) :
        '''
        Redo the format string for all handlers
        '''
        #import pdb; pdb.set_trace()

        self.__format_str = new_format
        formatter = logging.Formatter(self.__format_str)
        for handler in self.handlers :
            handler.setFormatter(formatter) # replace exist:20ing formatter

    def __getattr__(self, name):
        #print name
        def method(*args):
            getattr(self.logger, name )(args)
        return method

    @property
    def name(self) :
        return self._name

    @property
    def formatStr(self) :
        return self.__format_str

    @formatStr.setter
    def formatStr( self, newStr ) :
        #import pdb; pdb.set_trace()
        self.reformat( newStr)

def main() :
    logger = LoggerProxy(logger=logging.getLogger())
    logger.addHandler(logging.StreamHandler(sys.stderr))
    logger.info('HI')
    #import pdb; pdb.set_trace()
    logger.formatStr = "HERE: %(message)s"

    logger.info('HI')


if __name__ == '__main__' :
    sys.exit(main())
