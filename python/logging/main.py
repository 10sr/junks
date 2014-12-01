#!/usr/bin/env python3
import sys

# NOTE: SysLogHandler cannot send messages to journalctl

import logging
from logging.handlers import SysLogHandler

def main(argv):
    log = logging.getLogger('__main__')

    hdlr = SysLogHandler()
    log.addHandler(hdlr)

    fmttr = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    hdlr.setFormatter(fmttr)

    log.warn('Log from j/python/logging')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
