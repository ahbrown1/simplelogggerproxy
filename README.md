# LoggerProxy

## Specially purposed logger proxy

Python logging is powerful and flexible, sometimes at the price of being more than sufficient. In this instance we simply need a proxy for a  'logger' object (as returned from logging.getlogger()). The special scenario goes as follows:
* As usual, we want to enable logging in the program as soon as possible.
* This includes setting up the log format string to something useful, e.g. "(message)s"
* At some time later in the run, we wish to modify the message format because some previously unknown parameter becomes known later. So we want to change the format to be "some_param_value (message)s"
Rather than deconstructing or recreating a whole new logger object, this object supports a formatStr assignment. The new format string is assigned to all handlers registered with the logger.

## Sample :

```
import logging
import sys
from loggerProxy import LoggerProxy

def main() :
    logger = LoggerProxy()
    logger.addHandler(logging.StreamHandler(sys.stderr),)
    logger.info('HI')

    pval = 12345
    logger.formatStr = "%(asctime)s %(levelname)s: {custom}: -- %(message)s".format(custom=pval)
    logger.info('HI')



if __name__ == '__main__' :
    sys.exit(main())

```
