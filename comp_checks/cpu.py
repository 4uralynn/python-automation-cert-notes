#!/usr/bin/python3

import psutil

##This is my first python script since CS162. It will check the
##usage of your hard drive, and average your cpu usage over 10 
##seconds, with display per second. It will leave an error message
##if usage is too high, or will print that everything is OK.

usage=0

while True: 
    usage=psutil.cpu_percent(1)
    print("CPU Usage:" + str(usage))

