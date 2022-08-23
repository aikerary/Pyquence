from numbers import Real
import sympy as sp
import re

# Create a function using sympy for extract the roots of an equation
def roots(equation):
    # Create a variable for the equation
    eq = sp.sympify(equation)
    # Create a variable for the roots
    roots = sp.solve(eq)
    # Return the roots
    return roots

# Create a function to factorize a polynomial equation
def factorize(equation):
    # Create a variable for the equation
    eq = sp.sympify(equation)
    # Create a variable for the roots
    roots = sp.factor(eq)
    # Return the roots
    return roots

# Create a method to extract the grade of the equation
def grade(equation):
    # Create a variable for the equation
    eq = sp.sympify(equation)
    # Create a variable for the roots
    grade = eq.as_poly().degree()
    # Return the roots
    return grade

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

# Create a def main and prove the roots works
def main():
    x = sp.Symbol('x')
    print(roots("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x"))
    print(factorize("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x"))
    print(grade("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x"))
    print(grade(factorize("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x")))
         

# If the file is run directly, run the main function.
if __name__ == "__main__":
    main()

# End of file.
