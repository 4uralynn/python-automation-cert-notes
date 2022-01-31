#!/usr/bin/env python3

import csv
import operator
import os
import sys
import re


def parsefile(errors, user_entries):
    with open("syslog.log") as file:
        for line in file.readlines():
            results = re.search(r"^\w[a-z\d\s:\.]+([A-Z]+)\s([\w'\s]*)\s[\[[#\d]*\]?]?\s?\((.*)\)" , line)                    
            summary, error, user = results.group(1), results.group(2), results.group(3)
            if error not in errors.keys():
                errors[error] = 1
            else:
                errors[error] += 1
            if user not in user_entries:
                user_entries[user] = {}
                user_entries[user]["INFO"] = 0
                user_entries[user]["ERROR"] = 0
            if summary == "INFO":
                if user not in user_entries.keys():
                    user_entries[user] = {}
                    user_entries[user]["INFO"] = 0
                else:
                    user_entries[user]["INFO"] +=1
            elif summary == "ERROR":
                if user not in user_entries.keys():
                    user_entries[user] = {}
                    user_entries[user]["ERROR"] = 0
                else:
                    user_entries[user]["ERROR"] += 1
    file.close()

def generate_reports(errors, user_entries):
    sorted_errors = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
    sorted_entries = sorted(user_entries.items(), key = operator.itemgetter(0))
    with open("error_message.csv", "w", newline="") as file:
        file.write("Error,Count\n")
        for key, value in sorted_errors:
            file.write(str(key) + "," + str(value) + "\n")
    file.close()
    with open("user_statistics.csv", "w", newline="") as file:
        file.write("Username,INFO,ERROR\n")
        for key, value in sorted_entries:
            file.write(str(key) + "," + str(value["INFO"]) + "," + str(value["ERROR"]) + "\n")
    file.close()
    return True

def main():
    errors = {}
    user_entries = {}
    parsefile(errors, user_entries)
    generated = generate_reports(errors, user_entries)
    sys.exit(1)
    return generated

main()
