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

def main() :

    logger = LoggerFactory(handlers=logging.StreamHandler(sys.stderr))
    print logger.formatStr  # shows default format string

    logger.error('HEY!')
    ## prints ('HEY!',)

    logger.formatStr = "HERE: %(message)s"
    logger.error('HEY!')
    ## prints HERE: ('HEY!',)
```
NOTE:  The proxy can be given a 'name', but logging.getLogger(name) only returns the underlying logger objet, not the proxy with the additional functionality to modify the format string.
