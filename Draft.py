from math import exp
import numpy as np


def func(x1,x2,c):
    return (x1+x2+c)

def func2(x1,x2,c):
    return (10*x1+10*x2+c)

def sigmoid(x):
    return 1/(1+exp(-x))

def softmax(x):
    exp_list=np.exp(x)
    return np.divide(exp_list,exp_list.sum()) 

def softmax2(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))    

"""
list_x=[1,2,5,-4]
list_y=[1,4,-5,5]

#result_np=np.empty([len(list_x),1])
result_np=[]

print(result_np)

for i in range(len(list_x)):
    func_result=func(list_x[i],list_y[i])
    print("Function for x=",list_x[i]," and y=",list_y[i],"is",func_result," and the sigmoid is",sigmoid(func_result))
    result_np=np.append(result_np,func_result)
    


print(result_np)
print("Softmax of result :")
print(softmax(result_np))
print("Softmax2 of result :")
print(softmax2(result_np))

softmax(result_np)==softmax2(result_np)



    
Y=[1,1,0]
P=[0.8,0.7,0.9]

print("The cross entropy of Y P is ")
cross_entropy(Y,P)
"""

