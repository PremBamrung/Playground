# Python program to find the sum of natural numbers up to n where n is provided by user
import time
# change this value for a different result
num = 160
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " ms")
        return result
    return wrapper
# uncomment to take input from the user
#num = int(input("Enter a number: "))

@time_it
def sum_iter(num):
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
   # use while loop to iterate un till zero
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is",sum," by iterations")
    #return (sum)


@time_it
def sum_formule(num):
    sum=num*(num+1)/2
    print("The sum is ", sum, " by formula")
    #return sum

sum_iter(num)
sum_formule(num)