import numpy as np
import sys
import tabulate
import math

def main():
    # Reading number of unknowns
    n = int(input('Enter number of data points: '))

    # Making numpy array of n & n x n size and initializing 
    # to zero for storing x and y value along with differences of y
    x = np.zeros((n))
    y = np.zeros((n,n))


    # Reading data points

    print('Enter data for x and y: ')
    for i in range(n):
        x[i] = (float(input( 'x['+str(i)+']=')))
        y[i][0] = float(input( 'y['+str(i)+']='))

    h=round(x[1]-x[0],3)
    for i in range (0,n-1):
        #print(round(x[i+1]-x[i],3))
        if round(x[i+1]-x[i],3) != h:
            print('interval for x is not same')
            main()
        
    # Generating backward difference table
    for i in range(1,n):
        for j in range(n-1,i-2,-1):
            y[j][i] = y[j][i-1] - y[j-1][i-1]

            
    print('\nBACKWARD DIFFERENCE TABLE\n');
    array=list()
    for i in range(0,n):
        #print( x[i], end='')
        row=list()
        row.append(x[i])
        for j in range(0, i+1):
            #print('\t'+ str (y[i][j]), end='')
            row.append(y[i][j])
        #print()
        array.append(row)
    
    length = len(y[-1])
    name= ["x","y"]
    for i in range(length):
        name.append(f"∇^{i}y")
    print(tabulate.tabulate(array,headers=name,tablefmt='psql'))

    
    find_x=float(input('enter the value to find interpolation for x='))
    p=(find_x-x[-1])/ h
    sum = array[-1][1]
    for i in range(0,len( array[-1])-1):
        multi = 1
        for j in range(i):
            multi *= (p + j)
        if i==0:
            continue
        #print(sum,array[-1][i+1],multi,math.factorial(i))
        sum += array[-1][i+1] * multi / math.factorial(i)
        
    print(sum)
main()

