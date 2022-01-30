import re

#Escaping Caharcters

#Typing a '.' into the search doesn't actually stand for a '.'
print(re.search(r".com", "welcome"))
#We can get get around this and take the '.' literally with a '\' 
#typed in front of the '.' -- Like '\.'
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

#We can use '\' to escape any special character.
#We can also use it in combination with other characters:
#For example, '\w' matches any alphanumeric character (a-z,0-9, and _)
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another."))

#In addition, '\d'matches digits, '\s' matches whitespace, and '\b' for word boundries
#Check out regex101.com

