from numbers import Real
from os import system
import string
import sympy as sp
import re
from sympy.polys.monomials import itermonomials
from sympy.polys.orderings import monomial_key
from IPython.display import display, Latex


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
    
# Factorize an equation and then split it
def splitE(eq):
    # Create a variable for the equation
    eq= sp.factor(eq)
    # Create a variable for the terms
    terms = eq.as_ordered_factors()
    # Return the terms
    return terms

# aryMatrix= List of lists containing grades(index 0),  equations(index 1), and roots(index 2)
# repeatedRoots= List of repeated roots in the same order as the grades
# Symbols= List of the max number of symbols for the roots
def finalSumix(aryMatrix, symbols):
    n= sp.Symbol('n', real=True)
    listOfGrades= aryMatrix[0]
    listOfRoots= aryMatrix[2]
    equation=0*n
    h=0
    for i in range (len(listOfGrades)):
        for j in range (listOfGrades[i]):
            equation+=(symbols[h]*(n**(j)))*(listOfRoots[i]**n)
            h+=1
    return equation

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

# Create a function that receives a list of numbers, then takes the sum number and
# returns a list of the first n numbers of the alphabet
def alphabet(lst):
    # Create a variable for the maximum number
    # Maximum equals the sum of all the numbers in the list
    maximum = sum(lst)
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

# Create a function that takes a list of numbers, and a sympy equation and returns a list
# of the different equations evaluated in each number
def evaluate(number, eq, start):
    n= sp.Symbol('n', real=True)
    # Create a list for the evaluated equations
    evaluated = []
    # Create a for loop to run through the list
    for i in range(number):
        # Append the evaluated equation to the list
        evaluated.append(eq.subs(n, i+start))
    # Return the list
    return evaluated

# Construct the system
def systemConstruction(listOfEquations, listOfConditions):
    y=0
    listOfEquationsDef=[]
    for equation in listOfEquations:
        equation = equation - listOfConditions[y]
        listOfEquationsDef.append(equation)
        y+=1
    return listOfEquationsDef

# Solve the system
def SolveSystem(listOfEquations, listOfSymbols):
    return sp.solve(listOfEquations, listOfSymbols)

# Create a def main and prove the functions works
def main():
    n= sp.Symbol('n', real=True)
    # equation = x**6+8.5*x**5+29*x**4+50.5*x**3+47*x**2+22*x+4
    # equation= [1, 17/2, 29, 101/2, 47, 22, 4]
    equation= [1, -9, 26, -24]
    equation= input("Enter the equation: ")
    if equation[0] == "[":
        equationIx= list(map(float,equation.strip("[").strip("]").split(",")))
    # If there is no float then parse to int
        for i in range(len(equationIx)):
            if equationIx[i].is_integer():
                equationIx[i]= int(equationIx[i])
        eq= poly(equationIx)
    else:
        eq= sp.sympify(equation)
    aryMatrix=gradesOf(eq)
    aryMatrix2=defRoots(aryMatrix)
    aryMatrix.append(aryMatrix2)
    print(aryMatrix)
    initialConditions= len(symbols(alphabet(aryMatrix[0])))
    print(finalSumix(aryMatrix, symbols(alphabet(aryMatrix[0]))))
    forEvaluated= finalSumix(aryMatrix, symbols(alphabet(aryMatrix[0])))
    start=int(input("Enter the starting iteration: "))
    conditions=[]
    while len(conditions)<initialConditions:
        conditionIx= input("Enter the "+str(initialConditions) +" conditions: ")
        conditions= list(map(float,conditionIx.strip("[").strip("]").split(",")))
        for i in range(len(conditions)):
            if conditions[i].is_integer():
                conditions[i]= int(conditions[i])
    # conditions= [2, 3, 4]
    print(evaluate(initialConditions,forEvaluated, start))
    systemix= systemConstruction(evaluate(initialConditions,forEvaluated, start),conditions)
    print(systemix)
    solutions=SolveSystem(systemix, symbols(alphabet(aryMatrix[0])))
    print(solutions)
    finalExpresion= factorize(forEvaluated.subs(solutions))
    print(finalExpresion)
    print(sp.latex(finalExpresion))
    display(Latex(sp.latex(finalExpresion)))

# If the file is run directly, run the main function.
if __name__ == "__main__":
    main()


# End of file.
