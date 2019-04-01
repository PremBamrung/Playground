import numpy as np
import time 
#import threading
from multiprocessing import Pool
#import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import matplotlib.pyplot as plt
from numba import jit


timesleep=0
arr = np.arange(1,50000)
lst=range(1,50)
#time.sleep(timesleep)

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " ms")
        return result
    return wrapper
   


def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        a=n*n
    return 


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        print(n*n*n)

"""
if __name__ == "__main__":

    #Multithread 
    print("Using Multithreading")
    start_multihread = time.time()

    t1= threading.Thread(target=calc_square, args=(arr,))
    t2= threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_multithread=time.time()
    time_multithread=(end_multithread-start_multihread)*1000
    



    #Serial
    print("Using Serial")
    start_serial = time.time()
    calc_cube(arr)
    calc_square(arr)
    end_serial = time.time()
    time_serial=(end_serial-start_serial)*1000




    #Multiprocessing
    print("Using Multiprocessing")
    start_multiprocessing = time.time()
    
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    #pool
    pool = Pool(processes=8)
    result_squares = pool.map_async(calc_square, arr)
    result_cubes = pool.map_async(calc_cube, arr)
    #print(result_cubes)
    #print(result_squares)
    #endpool
    end_multiprocessing = time.time()
    time_multiprocessing=(end_multiprocessing-start_multiprocessing)*1000

    print("Multithreading done in : ",time_multithread," ms")
    print(" ")
    print("Serial processing done in : ",time_serial," ms")
    print(" ")
    print("Multiprocessing done in : ",end_multiprocessing," ms")
"""
def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)

def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)

def cpu_heavy(x):
    print('I am', x)
    start = time.time()
    count = 0
    for i in range(10**8):
        count += i
    stop = time.time()
    return start, stop

def visualize_runtimes(results, title):
    start, stop = np.array(results).T
    plt.barh(range(len(start)), stop - start)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.xlim(0, 22.5)
    ytks = range(len(results))
    plt.yticks(ytks, ['job {}'.format(exp) for exp in ytks])
    plt.title(title)
    return stop[-1] - start[0]


"""
if __name__=="__maine__":


    print("carotte")
    #plt.subplot(1, 2, 1)
    #visualize_runtimes(multithreading(cpu_heavy, range(4), 4), "Multithreading")
    #plt.subplot(1, 2, 2)
    #visualize_runtimes(multiprocessing(cpu_heavy, range(4), 4), "Multiprocessing")
    #plt.show()
    multiprocessing(cpu_heavy, range(4), 4)
    multithreading(cpu_heavy, range(4), 4)
"""



"""
if __name__ == "__main__":
    lst=list(range(1,50000))
    #multiprocessing
    t1=time.time()
    p1=multiprocessing.Process(target=calc_square, args=(lst,))
    p1.start()
    p1.join()
    t2=time.time()
    mp_time=(t2-t1)*1000

    #serial
    t3=time.time()
    calc_square(lst)
    t4=time.time()
    serial_time=(t4-t3)*1000

    print("Multiprocessing took ", mp_time, " ms")
    print("Serial took ", serial_time, " ms")
    
"""


def square_pool(number):
    result = number*number
    return result
"""
if __name__ == "__main__":
    debut_pool=time.time()
    p=Pool()
    p.map(cpu_heavy,lst)
    fin_pool=time.time()

    debut_serial=time.time()
    cpu_heavy(lst)
    fin_serial=time.time()

    print("Pooling took ", (fin_pool-debut_pool)*1000, " ms")
    print("Serial took ", (fin_serial-debut_serial)*1000, " ms")
"""

@time_it
def pure_python(number):
    a=list(range(number))
    b=list(range(number))
    c=[a[i]+b[i] for i in range(len(a))]


@time_it
def pure_numpy(number):
    a_np=np.arange(number)
    b_np=np.arange(number)
    c_np=a_np+b_np


@time_it
@jit(nopython=True, parallel=True)
def numpy_jit(number):
    a_np=np.arange(number)
    b_np=np.arange(number)
    c_np=a_np+b_np

n=1000000000
pure_numpy(n)
#pure_python(n)
numpy_jit(n)