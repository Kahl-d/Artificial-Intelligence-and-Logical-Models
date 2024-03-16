############################################################
# Problem 4: Odd and even integers
from typing import Tuple, List
from logic import *


# Return the following 6 laws. Be sure your formulas are exactly in the order specified.
# 0. Each number $x$ has exactly one successor, which is not equal to $x$.
# 1. Each number is either even or odd, but not both.
# 2. The successor number of an even number is odd.
# 3. The successor number of an odd number is even.
# 4. For every number $x$, the successor of $x$ is larger than $x$.
# 5. Larger is a transitive property: if $x$ is larger than $y$ and $y$ is
#    larger than $z$, then $x$ is larger than $z$.
# Query: For each number, there exists an even number larger than it.
def ints() -> Tuple[List[Formula], Formula]:
    def Even(x): return Atom('Even', x)  # whether x is even

    def Odd(x): return Atom('Odd', x)  # whether x is odd

    def Successor(x, y): return Atom('Successor', x, y)  # whether x's successor is y

    def Larger(x, y): return Atom('Larger', x, y)  # whether x is larger than y

    # Note: all objects are numbers, so we don't need to define Number as an
    # explicit predicate.
    #
    # Note: pay attention to the order of arguments of Successor and Larger.
    # Populate `formulas` with the 6 laws above.
    #
    # Hint: You might want to use the Equals predicate, defined in logic.py.  This
    # predicate is used to assert that two objects are the same.
    formulas = []

    # BEGIN_YOUR_CODE (our solution is 16 lines of code, but don't worry if you deviate from this)

    # Law 0: Each number $x$ has exactly one successor, which is not equal to $x$.
    # We can devie this in two parts:
        # 1. For each number $x$, there exists a number $y$ such that $y$ is the successor of $x$ and $x$ is not equal to $y.
        # 2. For all x and y, if y is the successor of x, and z is also the successor of x, then y is equal to z.
    formulas.append(Forall('$x', Exists('$y', And(Successor('$x', '$y'), Not(Equals('$x', '$y'))))))
    formulas.append(Forall('$x', Forall('$y', Forall('$z', Implies(And(Successor('$x', '$y'), Successor('$x', '$z')), Equals('$y', '$z'))))))

    # Law 1: Each number is either even or odd, but not both.
    # We can devide this in two parts:
        # 1. For each number $x$, $x$ is either even and  not odd.
        # 2. For each number $x$, $x$ is either odd and not even.
    formulas.append(Forall('$x', Or(And(Even('$x'), Not(Odd('$x'))), And(Odd('$x'), Not(Even('$x'))))))

    # Law 2: The successor number of an even number is odd.
    formulas.append(Forall('$x', Implies(Even('$x'), Exists('$y', And(Successor('$x', '$y'), Odd('$y'))))))

    # Law 3: The successor number of an odd number is even.
    # For all x and y, if y is the successor of x, and x is odd, then y should be even.
    formulas.append(Forall('$x', Forall('$y', Implies(And(Odd('$x'), Successor('$x', '$y')), Even('$y')))))

    # Law 4: For every number $x$, the successor of $x$ is larger than $x$.
    # If x is a successor of y, then y should larger than x
    formulas.append(Forall('$x', Forall('$y', Implies(Successor('$x', '$y'), Larger('$y', '$x')))))

    # Law 5: if $x$ is larger than $y$ and $y$ is larger than $z$, then $x$ is larger than $z$.
    # Can be done is part
    # for all x where x is larger than y
    # We check for all y where y is larger than z
    # That will imply that all these x will be larger than z
    formulas.append(Forall('$x', Forall('$y', Implies(Larger('$x', '$y'), Forall('$z', Implies(Larger('$y', '$z'), Larger('$x', '$z')))))))

    # END_YOUR_CODE
    query = Forall('$x', Exists('$y', And(Even('$y'), Larger('$y', '$x'))))
    return formulas, query
