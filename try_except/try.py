#/usr/bin/env python3

def character_ frequency(filename):
    """Counts the frequency of ech character in the given file."""
    #First try to open the file
    try:
        file = open(filename)
    except OSError:
        return None     #The code in the 'except' block is only raised
                        #if the code in the 'try' block produces an error

    #Now process the file
    characters = {}
    for line in filename:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    file.close()
    return characters
