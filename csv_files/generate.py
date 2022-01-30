#!/usr/bin/env python3
import csv
##Software
soft = [["name", "version", "status", "users"], ["MaileTree", "5.34", "production", "324"],
        ["CalDoor", "1.25.1", "beta", "22"], ["Chatty Chicken", "0.34", "alpha", "4"]]

with open('software.csv', "w") as soft_csv:
    writer = csv.writer(soft_csv)
    writer.writerows(soft)


