# practice problem from beginning of the python book

def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number //2
    else:
        print(3*number +1)
        return(3*number +1)
print('Enter number:')
enter = int(input())
while enter != 1:
    enter = int(collatz(enter))
    
