#Repitition Qualifiers
import re

#Repeated matched are shown by the '.*' which will match any and all characters

#the star will take as many characters as possibe
print(re.search(r"Py.*n", "Pymalion"))
print(re.search(r"Py.*n", "Python Programming"))
#the '*' does not end at the first character. it takes as many as possible
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

#the '+' matches one or more occurances of the character before it
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
#above, because there was another character between the 'o' and 'l', it did
#not match 'o+l+'

#the '?' means either zero or one occurance of the character before it
print(re.search(r"p?each", "To each their own."))
print(re.search(r"p?each", "I like peaches."))
print(re.search(r"p?each", "Cold pppeaches."))
print(re.search(r"p?each", "Star-bellied sneaches."))

