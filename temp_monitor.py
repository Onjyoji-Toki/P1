#!/usr/bin/env python3

import psutil
from psutil import NoSuchProcess
from time import sleep
from process_mail import process_mail


def main():
    process = None

    for proc in psutil.process_iter():
        try:
            if proc.name() == 'python.exe':
                if 'hoge.py' in proc.cmdline()[1]:
                    process = proc
                    break
        except Exception:
            continue

    if process is not None:
        print(process)
    else:
        print('Process not found.')
        return

    try:
        while True:
            print('.', end='', flush=True)
            process.status()
            sleep(1)
    except NoSuchProcess:
        process_mail()
    except KeyboardInterrupt:
        print('bye')

if __name__ == '__main__':
    main()
