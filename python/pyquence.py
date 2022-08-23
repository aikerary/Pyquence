import sympy as sp

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

# Create a def main and prove the roots works
def main():
    print(roots("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x"))
    print(factorize("x**7-10*x**6+28*x**5+30*x**4-297*x**3+540*x**2-324*x"))

# If the file is run directly, run the main function.
if __name__ == "__main__":
    main()





