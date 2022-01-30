import re

#Applying Regular Expressions

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
#'Azerbaijan' matches, but it doesn't show the whole string

#we can make our expression stricter like '^A.a$' so that it
#inludes the entire line
print(re.search(r"^A.*a$", "Azerbaijan"))
#Now 'Azerbaijan' does not match, but 'Austrailia' will
print(re.search(r"^A.*a$", "Austrailia"))
print(re.search(r"^A.*a$", "Australia"))


#Now construct expression to detect valid variables in Python
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "1variable"))
#the above does not match since the string begins with a number

#Another application (try running this module in an IDE):
def check_sentence(text):
	result = re.search(r"^[A-Z][a-zA-Z0-9\,\;\- ]*[\.\?\!]$", text)
	return result != None
print(check_sentence("Is this is a sentence?"))
print(check_sentence("is this is a sentence?"))
print(check_sentence("Hello"))
print(check_sentence("1-2-3-GO!"))
print(check_sentence("A star is born."))

#keep practicing, and remember, all of these regex characters apply in grep
