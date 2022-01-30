
#character classes

import re

print(re.search(r"[Pp]ython", "Python"))
#allows for either uppercase or lowercase 'P'

#a dash ('-') signals a range (see below)
print(re.search(r"[a-z]way", "End of the highway"))
print(re.search(r"[a-z]way", "Walk this way"))
#(no match when there is a space when searching a-z)
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
#we can combine ranges inside the brackets^
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

#to match a character that is not in a range use '^'
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
#(add a space(' '))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

#Use a pipe ('|') to search either/or
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats."))
#if the sentence has both...
print(re.search(r"cat|dog", "I like cats and dogs."))
#the 'search' method will only find the first match...

#to find every occurance (like grep), use the 'findall' method 
print(re.findall(r"cat|dog", "I like cats and dogs."))


