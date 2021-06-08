import random
import string

rd = random.random()
def get_letter():
    list = string.ascii_letters
    fin = ''
    while (True):
        num = int(100 * round(random.random(), 2))
        if num <= 26:
            yield list[num]



# for i in get_letter():
#     print(i, end=" ")

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

def check(func,num):
    if num > 0 and isinstance(num, int):
        results = func(num)
        return results
    else:
        return -1

print(check(factorial,3))