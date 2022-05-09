from time import time
from eqnconvert import *
import numpy as np


def calculate_lu(matrix, eqn_num):
    start_time = time()

    # creating 2 arrays to store l & u matrix in them
    l = np.array([[0. for n in range(eqn_num)] for m in range(eqn_num)])
    u = np.array([[0. for n in range(eqn_num)] for m in range(eqn_num)])

    # take the values form the matrix and put them in u to start calculations required
    for x in range(eqn_num):
        for y in range(eqn_num):
            u[y][x] = matrix[y][x]

    # calculating l & u matrix
    for i in range(eqn_num-1):
        for j in range(i, eqn_num-1):
            m = -(u[j+1][i] / u[i][i])
            u[j+1] = u[j+1] + u[i]*m
            l[j+1][i] = -m

    # putting 1 in the diagonal of l matrix
    for i in range(eqn_num):
        for j in range(eqn_num):
            if (i==j):
                l[i][j]=1

    # creating b array to take the answers of the equations
    b = []
    for i in range(eqn_num):
        b.append(-matrix[i][eqn_num])

    # forward substitution to calculate y ( LY=B )
    y = []
    for i in range(eqn_num):
        y.append(b[i])
        for j in range(i):
            y[i]=y[i]-l[i][j]*y[j]

    backward = np.array([[0. for n in range(eqn_num+1)] for m in range(eqn_num)])
    for i in range(eqn_num):
        for j in range (eqn_num):
            backward[j][i]=u[j][i]

    for i in range(eqn_num):
        backward[i][eqn_num]=-y[i]

    # backward substitution to calculate x ( UX=Y )
    x = []
    for i in range(eqn_num - 1, -1, -1):

        for j in range(eqn_num - 1 - i):
            backward[i][-1] = backward[i][-1] + backward[i][-2 - j]  # subtracting the auxiliary part of matrix from the
            # already calculated values to get ready for pure division
        res = - (backward[i][-1] / backward[i][i])  # getting the desired result of the row

        for k in range(i):
            backward[k][i] = backward[k][i] * res  # multiply the result by each coeff of its column

        x.append(res)
        
    end_time = time()
    elapsed_time = end_time - start_time
    return [x, elapsed_time]

if __name__ == "__main__":
    input_filename = input("Input File Name : ")
    eqns = readfile(input_filename)
    matrix = list_to_matrix(eqns)
    output_filename = input("Output File Name : ")
    results = calculate_lu(matrix, len(eqns))
    writefile(results, output_filename)