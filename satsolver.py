# single formula SAT solver for LOGIA
# to avoid the halting problem on unsatisfiable propositions

# define propositional operators

def neg(x):
  return not x

def con(x, y):
  return x and y

def dis(x, y):
  return x or y

def imp(x, y):
  return not x or y

def iff(x, y):
  return (x and y) or (not x and not y)

# this stores a string as a formula and returns a truth value
def sat_main():
  wff = input()   # wff = raw_input() on Python 2.x, stores the formula
  return eval(wff)

sat_main()

# Create a 'var' list that stores the variables used in wff
# Iterate the variables through {False, True} to get at least one instance when wff is 'True'
