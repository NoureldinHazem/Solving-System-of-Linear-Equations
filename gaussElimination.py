from time import time
from eqnconvert import *
import numpy as np


def calculate_gauss(matrix, eqn_num):
    start_time = time()
    # converting the matrix to an upper triangular matrix
    for i in range(eqn_num - 1):
        for j in range(i, eqn_num - 1):
            m = -(matrix[j+1][i] / matrix[i][i])
            matrix[j+1] = matrix[j+1] + matrix[i]*m

    # backward substitution
    results = []
    for i in range(eqn_num - 1, -1, -1):

        for j in range(eqn_num - 1 - i):
            matrix[i][-1] = matrix[i][-1] + matrix[i][-2-j]     # subtracting the auxiliary part of matrix from the
                                                                # already calculated values to get ready for pure division
        res = - (matrix[i][-1] / matrix[i][i])          # getting the desired result of the row

        for k in range(i):
            matrix[k][i] = matrix[k][i] * res           # multiply the result by each coeff of its column

        results.append(res)

    end_time = time()
    elapsed_time = end_time - start_time
    return [results, elapsed_time]

if __name__ == "__main__":
    input_filename = input("Input File Name : ")
    eqns = readfile(input_filename)
    matrix = list_to_matrix(eqns)
    output_filename = input("Output File Name : ")
    results = calculate_gauss(matrix, len(eqns))
    writefile(results, output_filename)