#!/usr/bin/env python3

import sys
import login
import time

if __name__ == '__main__':

    while True:

        isSuccess, reply_string = login.login()
        now_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now_string, reply_string)
        print(now_string, reply_string, file=sys.stderr)

        time.sleep(10 * 60) # every 10 minutes

