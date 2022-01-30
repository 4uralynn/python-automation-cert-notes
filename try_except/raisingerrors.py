#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    #The 'assert' keyword tries to verify if an expression is True. 
    #If false, an assertion error is raised
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
        #The keyword to raise an error in python is 'raise'
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

