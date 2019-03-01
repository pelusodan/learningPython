# python to show passing by referance to a function
def eggs(par):
    par.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam)
# here the function is directly modifying the parameter, so it stays that way
# in the end
# also remember that tuples are immutable and with parentheses
