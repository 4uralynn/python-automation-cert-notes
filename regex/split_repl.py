import re

#Splitting and Replacing

#This is a new re method that can split a string by regex
re.split(r"[.?!]", "One sentence. And another one! Is this the last one?")
#Results were: ['One sentence', ' And another one', ' Is this the last one', '']

#To include the delimiter characters used to split the valuse, we can use capturing groups '()'
re.split(r"([.?!])", "One sentence. And another one! Is this the last one?")
#Results show the punctition seperately included in the list:
#['One sentence', '.', ' And another one', '!', ' Is this the last one', '?', '']


#The 'sub' method creates new strings by replacing substrings with new substrings
#again using regex:
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "received an email for go_nuts95@my.example.com")
#Result: 'received an email for [REDACTED]'

re.sub(r"^([\w .-]*), ([\w.-]*)$", r"\2 \1", "Lovelace, Ada")
#For regex '\1' and '\2' are general notation for capturing groups
#Here the results rearrange the name, (first name followed by last name)
#Results: 'Ada Lovelace'
