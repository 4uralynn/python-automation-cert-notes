#!/usr/bin/python3
import shutil
import psutil
import statistics as stats
from network import *

##This is my first python script since CS162. It will check the
##usage of your hard drive, and average your cpu usage over 10 
##seconds, with display per second. It will leave an error message
##if usage is too high, or will print that everything is OK.

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    percent_free=du.free/du.total*100
    return percent_free > 20

def check_cpu_usage():
    usage=[0]*10
    for num in usage: 
        usage[num]=psutil.cpu_percent(1)
        print("CPU Usage:" + str(usage[num]))
    return (stats.mean(usage)) < 75

if not check_disk_usage("/"):
    print("ERROR! Low disk capacity!")
if not check_cpu_usage():
    print("ERROR! CPU usage high! Over 75 percent!")
else:
    print("Your disk and cpu usage is OK.")

if check_localhost():
    print("You are connected to the network.")
else:
    print("Network check failed!")

if check_connectivity():
    print("You are connected to the internet.")
else:
    print("Internet connectivity check failed!")


