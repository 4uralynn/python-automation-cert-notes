#!/usr/bin/env python3
import re

#Capturing Groups in Regex

#Captured groups are patterns of the pattern that are enclosed in parentheses
#result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
#print(result)
#print(result.groups())
# ('Lovelace', 'Ada')
#The groups method returns a tuple, as seen in the example above 
#print(result[0])
#print(result[1])
#print(result[2])
#You can access from the groups method using indexing
#the first index will be the entire match, and then the next and next
#are each subsequent match.

#Now we can format
#"Hi, I am {} {}, what's you're name?".format(result[2], result[1])

#New function:
def rearrange_name(name):
#the expression is slightly changed to include middle initials:
     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
     if result is None:
             return "" 
            #return name
     return "{} {}".format(result[2], result[1])


#rearrange_name("Lovelace, Ada")
#rearrange_name("Ritchie, Dennis")
#rearrange_name("Hopper, Grace M.")
#These all should rearrage to First and Middle Initial, then Last name
#Example: 'Grace M. Hopper'
