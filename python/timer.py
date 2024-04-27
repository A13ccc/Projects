import time
import os
h = input("How many hours: ")
m = input("How many minutes: ")
s = input("How many seconds: ")
elapsed = int(h) * 3600 + int(m) * 60 + int(s)
print("Timer started")
print(h, ":", m, ":", s)
while int(h) > 0 or int(m) > 0 or int(s) > 0:
    time.sleep(1)
    elapsed = elapsed - 1
    s = int(s) - 1
    if int(s) == 0:
        if int(elapsed) == 0 & int(h) == 0 & int(m) == 0 & int(s) == 0:
            h = 0
            m = 0
            s = 0
            print("Timer ended")
            break
    if int(s) < 0:
        m = int(m) - 1
        s = 59
        if int(m) < 0:
            m = 0
        if int(m) == 0:
            h = int(h) - 1
            if int(h) == 0:
                m = 0
            if int(h) < 0:
                h = 0
    print(h, ":", m, ":", s)
print("Timer ended")