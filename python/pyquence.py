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

# Create a def main and prove the functions works
def main():
    equation = "(2+x)**3 *(x+1)**2* (x+0.5)"
    x = sp.Symbol('x')
    print(roots(equation))
    print(factorize(equation))
    print(grade(equation))
    print(grade(factorize(equation)))
    print(splitEquation(factorize(equation)))
    print(splitE(equation))
    print(gradesOf(equation))
    #  Capture a string named equation

# If the file is run directly, run the main function.
if __name__ == "__main__":
    main()

# End of file.
