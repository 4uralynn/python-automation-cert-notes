
#Example to used with the Raising Errors module

from raisingerrors import validate_user

validate_user("", -1)
#Error received: ValueError:minlen must be at least 1


validate_user([3], 1)
#Received error: AssertionError: username must be a string
