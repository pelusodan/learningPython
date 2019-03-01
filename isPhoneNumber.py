#first project to show phone number search (oh baby)
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print(isPhoneNumber('432-232-2333'))
print(isPhoneNumber('moshi moshi'))
# you can use this to search for pattern expressions in large sets of texts
# short circuits many of the options
