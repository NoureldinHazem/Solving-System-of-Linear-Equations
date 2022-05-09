from sympy import sympify, Poly
import numpy as np
import re
from sympy.abc import *


# for UI textbox reading
def readeqn_from_ui(equations_as_string):
    eqns = []
    eqn_num = len(equations_as_string)
    for eqn in equations_as_string:
        eqns.append(extract_coeffs(eqn, eqn_num))
    return eqns


# for console reading from file
def readfile(filename):
    eqns = []
    with open(filename, "r") as file:
        eqn_num = int(file.readline())
        method = file.readline()
        for i in range(eqn_num):
            eqns.append(extract_coeffs(file.readline(), eqn_num))
        file.close()
    return eqns


# for both console and UI file printing
def writefile(results, filename):
    filename = filename + ".txt" if filename != "" else "out.txt"
    elapsed_time = round(results[1], 6)
    results.pop()
    results = results[0]
    results.reverse()  # easier for printing using ascii
    char = 0
    with open(filename, "w") as file:
        file.write(f"Elapsed Time = {elapsed_time} secs.\n")
        file.write("----------------------------------------\n")
        for res in results:
            file.write(f"\n{chr(char + 97)} = {res}")
            char += 1
        file.close()


def extract_coeffs(expr, eqn_num):
    coeffs = []
    check = re.split(' \+ | - ', expr)[-1]
    if (int(check) == 0):
        expr = sympify(expr)  # converting the string equation to sympy object

        for i in range(eqn_num):
            coeff = expr.coeff(chr(i + 97))
            coeffs.append(coeff)
        coeffs.append(0)
        return coeffs   # retuning a list of all coeffs

    expr = sympify(expr)                    # converting the string equation to sympy object

    symbs = ()
    for i in range(eqn_num):
        symbs += (sympify(chr(i + 97)),)
        coeff = expr.coeff(chr(i + 97))
        coeffs.append(coeff)
    polynomial = Poly(expr, symbs)  # converting the sympy object to polynomial to get the constant
    all_coeffs = polynomial.coeffs()  # getting all coefficients to get the last coeff which is the const
    coeffs.append(all_coeffs[-1])
    return coeffs                        # retuning a list of all coeffs


def list_to_matrix(eqns):
    matrix = np.array(eqns)                 # converting the 2D list to a numpy matrix
    return matrix