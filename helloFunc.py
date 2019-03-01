# finally seeing how to write functions (rad)
def hello():
    print(' Howdy!')
hello()
hello()
def hello2(name):
    print('Hello ' + name)
hello2('Greg')
hello2('Jajss')


# you can add return statements to have the function bring back something
def ex(x):
    if x == 1:
        return 'Lad'
    else:
        return 'Gad'
for i in range(0,6):
    print(ex(i))

# functions that are void evaluate to "None" which is a keyword

