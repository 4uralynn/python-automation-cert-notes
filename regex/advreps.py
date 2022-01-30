import re

#ADVANCED (numeric) Repitition

#You can repeat character matches numerically using curly brackets '{}'
print(re.search(r"\b[a-zA-Z]{5}\b", "A grinning ghost has come out to socialize."))
#in the above expression, 'ghost' matched because it was 5 letters making up a word
#('\b' is a word boundry)

print(re.findall(r"\b[a-zA-Z]{5}\b", "A great grinning ghost has come out to socialize."))
#Using the findall method, we can find all words of that length

#We could also use a range in side the curly brackets
print(re.findall(r"\b[a-zA-Z]{5,10}\b", "A great grinning ghost has come out to socialize."))
print(re.findall(r"\b[a-zA-Z]{5,}\b", "A great grinning ghost has come out to socialize."))

print(re.search(r"s\w{,20}", "I really like strawberries."))
#<re.Match object; span=(14, 26), match='strawberries'>
#Using the search method again, this one matches a pattern of starting with an 's' 
#which followed by up to 20 alphanumeric characters
