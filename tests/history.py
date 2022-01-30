#!/usr/bin/env python3
import os
import readline

def clear():
    readline.clear_history()

def save():
#saves session history into file
    with open("pylog.txt", "w") as file:
        file.write('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))

save()
