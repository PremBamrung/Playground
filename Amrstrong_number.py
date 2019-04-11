# Program to check Armstrong numbers in certain interval
import time
lower = 100
upper = 2000000
from numba import jit
# To take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " ms")
        return result
    return wrapper

"""
for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
"""

@time_it
def Armstrong_list(lower,upper):
    print("List of Armstrong number from ",lower," to ",upper)
    for num in range(lower, upper + 1):

   # order of number
        order = len(str(num))
    
   # initialize sum
        sum = 0

   # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)


@time_it
@jit(parallel=True)
def Armstrong_list_jit(lower,upper):
    print("List of Armstrong number from ",lower," to ",upper)
    for num in range(lower, upper + 1):

   # order of number
        order = len(str(num))
    
   # initialize sum
        sum = 0

   # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)

Armstrong_list(lower,upper)
Armstrong_list_jit(lower,upper)