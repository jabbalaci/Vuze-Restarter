#!/usr/bin/env python3
# encoding: utf-8

"""
keep a specified program alive, i.e. restart it if it dies
"""

import os
from time import sleep

import psutil

import mylogging as log

PROCESS_NAME = 'vuze'
WAIT = 5


def is_process_running(name):
    """
    Tell if a process is running.

    The proc object is cached so it doesn't need to be looked up every time.
    """
    if not hasattr(is_process_running, "proc"):
        is_process_running.proc = None    # it doesn't exist yet, so init it

    if is_process_running.proc:
        if is_process_running.proc.is_running():
            return True
        else:
            is_process_running.proc = None
            return False
    else:
        for p in psutil.process_iter():
            if p.name() == name:
                is_process_running.proc = p
                return True
        #
        return False
        

def kill_process(name):
    """
    Kill the process with the specified name.
    """
    for p in psutil.process_iter():
        cmd = " ".join(p.cmdline())
        if ('java' in cmd) and (name in cmd):
            log.info(cmd)
            log.info(p.pid)
            p.kill()
            break


def main():
    while True:
        try:
            if is_process_running(PROCESS_NAME):
                sleep(WAIT)
            else:
                log.info("vuze is not running, restarting")
                sleep(10)
                os.system("./start_vuze.sh")
                sleep(10)
        except KeyboardInterrupt:
            kill_process(PROCESS_NAME)
            log.info("interrupted by the user")
            break
    #
    print()

##############################################################################

if __name__ == '__main__':
    main()
