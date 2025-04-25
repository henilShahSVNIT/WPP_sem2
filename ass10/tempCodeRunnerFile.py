'''The bisection method is a technique for finding solutions (roots) to 
equations with a single 
unknown variable. Given a polynomial function f, try to find an initial 
interval off by 
random probe. Store all the updates in an Numpy array. Plot the root finding 
process using 
the matplotlib/pyplot library.''' 
 
import numpy as np 
import matplotlib.pyplot as plt 
 
def f(x): 
    return x*2 + 4*x + 7 
 
def find_initial_range(func): 
    max = 10 
    min = -10 
    arr = np.linspace(min,max,500) 
 
    for i in range(len(arr)): 
        x = arr[i] 
        for j in range(i+1,len(arr)): 
            if(func(x)*func(arr[j])<0): 
                return np.array([x,arr[j]]) 
             
def bisection(initial_range,func): 
    a = initial_range(func)[0] 
    b = initial_range(func)[1] 
    c = (a+b)/2 
    tol = 1e-5 
    mid_points = [] 
 
    while(abs(func(c)) > tol): 
        mid_points.append(c) 
 
        if func(a)*func(c) < 0: 
            b=c 
        else: 
            a=c 
         
        c = (a+b)/2 
 
    mid_points.append(c) 
    return mid_points 
 
mid_points = bisection(find_initial_range,f) 
plt.plot(mid_points,color='m',marker='.',linewidth='1',label="Mid Points") 
 
plt.title("Bisection values") 
plt.xlabel("Itertion") 
plt.ylabel("Mid Point Values") 
plt.tight_layout() 
plt.grid(True) 
plt.legend(loc="lower right") 
plt.show()