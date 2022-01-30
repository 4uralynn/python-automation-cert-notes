#!usr/bin/python3
import os

def all_dir(bits):
    for name in os.listdir(bits):
        fullname = os.path.join(bits, name)
        if os.path.isdir(fullname):
            print("{:50} <DIR>".format(fullname))
        else:
            print("{}".format(fullname))
