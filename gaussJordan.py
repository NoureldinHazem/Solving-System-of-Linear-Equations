from time import time
import numpy as np

flag = 0
def jordan(A,n):
    global flag
    start_time = time()
    for i in range(n):
        A[i][n]*=-1
    k = 0
    for i in range(n):
        if A[i][i] == 0:
            c = 1
            while (i + c)< n and A[i+c][i] == 0:
                c+=1
            if (i+c) == n:
                flag = 1
                break
            j = i
            for k in range(n+1):
                A[j][k],A[j+c][k] = A[j+c][k],A[j][k]
        for j in range(n):
            if i != j:
                p = A[j][i]/A[i][i]
                for k in range(n+1):
                    A[j][k] = A[j][k] - A[i][k]*p
    results = []
    for i in range(n):
        A[i][n]=A[i][n]/A[i][i]
        results.append(A[i][n])
    end_time = time()
    elapsed_time = end_time - start_time
    
    return [results[::-1],elapsed_time]   

# if flag = 1 :
def CheckConsistency(A,n):
    flag = 3 # No solution
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i][j]
        if sum == A[i][j]:
            flag = 2    #infinite solution
    return flag
    


if __name__ == '__main__':
    # A = [[0.0,2,1,4],[1,1,2,6],[2,1,1,7]]
    A=[]
    n = len(A)
    Res = jordan(np.array(A),n)
    print(Res)
    
