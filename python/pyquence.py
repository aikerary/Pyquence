from numbers import Real
import sympy as sp
import re
from sympy.polys.monomials import itermonomials
from sympy.polys.orderings import monomial_key

# Create a function using sympy for extract the roots of an equation
def roots(eq):
    # Create a variable for the roots
    roots = sp.solve(eq)
    # Return the roots
    return roots

# Create a function to factorize a polynomial equation
def factorize(eq):
    # Create a variable for the factors
    factors = sp.factor(eq)
    # Return the factors
    return factors

# Create a method to extract the grade of the equation
def grade(eq):
    # Create a variable for the grade
    grade = eq.as_poly().degree()
    # Return the roots
    return grade

# Split the equation into a list of terms
def splitEquation(eq):
    # Create a variable for the terms
    terms = eq.as_ordered_factors()
    # Return the terms
    return terms
    
# Factorize an equation and then split it
def splitE(eq):
    # Create a variable for the equation
    eq= sp.factor(eq)
    # Create a variable for the terms
    terms = eq.as_ordered_factors()
    # Return the terms
    return terms

# Final sum of the equation
def finalSum(nrd, mj, rootlist):
    n= sp.Symbol('n', real=True)
    pyquation=""
    equation = "("
    bstring = "b"
    for j in range(nrd):
        for i in range(mj):
            equation+="+b_"+str(i+mj-1)+"n**"+str(i-1)
        equation+=")"+rootlist[j]+"**n"
        pyquation+=equation
        equation="+("
    pyquationS = sp.sympify(pyquation)
    return pyquationS

def resort(list1, list2):
    auxiliar1=sorted(list1)
    auxiliar2=[]
    # Equals the auxliar2 to the list2
    for i in range(len(list2)):
        auxiliar2.append(list2[i])
    # Sort a list and then resort the other using the indexes of the first one
    for i in range(len(list1)):
        auxiliar2[i]=list2[list1.index(auxiliar1[i])]
        list1[list1.index(auxiliar1[i])]=0
    return[auxiliar1, auxiliar2]

# Using a for loop
def gradesOf(equation):
    listOfEquationsPartial= splitE(equation)
    listOfEquations= test(listOfEquationsPartial)
    listOfGrades = []
    for i in range(len(listOfEquations)):
        listOfGrades.append(listOfEquations[i].as_poly().degree())
    matrix = resort(listOfGrades, listOfEquations)
    return matrix

# Removing number factors
def test(list):
    new_list = []
    for i in list:
        if type(i) != sp.core.numbers.Float:
            new_list.append(i)
    return new_list

# Method for extracting the roots
def defRoots(matrix):
    listOfSolves=[]
    for i in range(len(matrix[1])):
      listOfSolves.append(roots(matrix[1][i])[0])
    return listOfSolves

# Method for repeating the roots
def repeat_list(lst):
    new_list = []
    for i in range(len(lst[0])):
        for j in range(lst[0][i]):
            new_list.append(lst[2][i])
    return new_list

# Convert a vector to poly
def poly(lst):
    lst= lst[::-1]
    x = sp.Symbol('x')
    return sum([lst[i] * x**i for i in range(len(lst))])

# Create a function that takes a integer as a parameter and returns a list of the first n
# letters of the alphabet
def alpha(n):
    # Create a list for the alphabet
    alphabet = []
    # Create a for loop to run through the alphabet
    for i in range(n):
        # Append the letter to the list
        alphabet.append(chr(i+97))
    # Return the list
    return alphabet

# Create a function that receives a list of numbers, then takes the maximum number and
# returns a list of the first n numbers of the alphabet
def alphabet(lst):
    # Create a variable for the maximum number
    maximum = max(lst)
    # Create a variable for the alphabet
    alphabet= alpha(maximum)
    # Return the alphabet
    return alphabet

# Create a function that receives a list of letters and create symbols for each one
def symbols(lst):
    # Create a list for the symbols
    symbols = []
    # Create a for loop to run through the list
    for i in range(len(lst)):
        # Create a variable for the symbol
        symbol = sp.Symbol(lst[i], real=True)
        # Append the symbol to the list
        symbols.append(symbol)
    # Return the list
    return symbols

# Create a def main and prove the functions works
def main():
    x = sp.Symbol('x', real=True)
    # equation = x**6+8.5*x**5+29*x**4+50.5*x**3+47*x**2+22*x+4
    equation= [1, 17/2, 29, 101/2, 47, 22, 4]
    if type(equation) == list:
      eq= poly(equation)
    else:
      eq= equation
    lista=gradesOf(eq)
    lista2=defRoots(lista)
    lista.append(lista2)
    print(repeat_list(lista))
    print(lista)
    print(defRoots(lista))
    print(symbols(alphabet(lista[0])))
    print(symbols(alphabet(lista[0]))[0])
    print(finalSumix(lista, symbols(alphabet(lista[0]))))
    # Factorize the finalSumix
    print(factorize(finalSumix(lista, symbols(alphabet(lista[0])))))


# aryMatrix= List of lists containing grades(index 0),  equations(index 1), and roots(index 2)
# repeatedRoots= List of repeated roots in the same order as the grades
# Symbols= List of the max number of symbols for the roots
def finalSumix(aryMatrix, symbols):
    n= sp.Symbol('n', real=True)
    listOfGrades= aryMatrix[0]
    listOfRoots= aryMatrix[2]
    equation=0*n
    for i in range (len(listOfGrades)):
        for j in range (listOfGrades[i]):
            equation+=(symbols[j]*(n**(j)))*(listOfRoots[i]**n)
    return equation


# If the file is run directly, run the main function.
if __name__ == "__main__":
    main()

# End of file.
