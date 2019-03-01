# this program show exceptions
def spam(d):
    try:
        return 24 / d
    except ZeroDivisionError:
        print('Error: Invalid Argument')

print(spam(2))
print(spam(1))
print(spam(0))
print(spam(-1))

def so(d):
    return 42 / d
try:
    print(so(2))
    print(so(12))
    print(so(0))
    print(so(1))
except ZeroDivisionError:
    print('Invalid Argument')
# this does not print so(1) because after the exception clause the code continues
