# LOGIA : an automated theorem prover
# -----------------------------------
# 
# version 0.2, December 13, 2016
# for use with Coq 8.5pl3 (Oct 2016)
# written by wrick
# 
# -----------------------------------
# randomly genned tactics from a static tactics_base
# 2-parent crossover, random mutation
# no natural selection


from numpy.random import randint
from os import system


theorem    = open('/home/wrick/Documents/logia/theorem', 'r').readline()
tactics    = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
T          = len(tactics) - 1    # the last tactic is a null tactic
population = 10            # constant population size for every generation
maxlength  = 5             # maximum proof length


# create the seeds -- adds new proofs to the generation
def seedgen(generation) :

    for i in range(population) :
        length = randint(1, maxlength)
        proof  = []

        for j in range(length) :
            proof.append(randint(T))

        generation.append(proof)

    return(generation)


# define reproduction -- 2-parent crossover, creates a new proof with new length and all
def crossover(proof_tuple) :
    (proof1, proof2) = proof_tuple
    newproof      = []
    prooflength   = randint(1, maxlength)
    combine       = proof1 + proof2
    combinelength = len(combine)

    for i in range(prooflength) :
        newproof.append(randint(0, combinelength))

    return(newproof)


# define mutation -- as random as it can be, no dependencies, doesn't change proof length
def mutagen(proof) :
    mutaprob = 13          # probability of mutation is 1 in 13, 0 means zero probability

    if mutaprob != 0 :
        for i in proof :
            if randint(mutaprob) == 0 :    # probability of getting a zero is 1/mutaprob
                proof[i] = randint(T)

    return(proof)


# the new generation
def generationmap(generation) :
    newgeneration = []
    
    for i in range(population) :
        generation[i] = mutagen(generation[i])

    for i in range(population) :
        proof_tuple = (generation[randint(population)], generation[randint(population)])
        newproof = crossover(proof_tuple)
        newgeneration.append(newproof)

    return(newgeneration)


# convert integer sequences to tactic strings
def proofgen(sequence) :
    proof = 'Proof.'
    for i in sequence :
        proof += ' ' + tactics[i] + '.'
    proof += ' Defined.\n'
    return(proof)


# the main program
def logia_main():
    generation = seedgen([])
    qed = False

    while qed == False :
        
        for i in range(population) :
            if qed == False :
                Proof = open('/home/wrick/Documents/logia/proof.v', 'w')
                Proof.write(theorem + proofgen(generation[i]))
                Proof.close()
                system('coqtop -compile /home/wrick/Documents/logia/proof')
                qed = system('test -e /home/wrick/Documents/logia/proof.vo')
    
        generation = generationmap(generation)

logia_main()


# goedel converter for proofs
# assigns a goedel numbering for tactics in the tactics_base 

def goedel_proofs_main():
    tactics = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
    code = [str(i) for i in range(1,len(tactics, 2))]
    t2c = dict(zip(tactics, code))
    c2t = dict(zip(code, tactics))

    prf = open('/home/wrick/Documents/logia/proof', 'r').readline().strip()

    if prf.isdigit():
        prf = prf.split('0')
        ans = ''
        for code in prf:
            try:
                ans += c2t[code] + '. '
            except KeyError:
                pass
        ans = 'Proof. ' + ans + 'Defined.\n'

    else:
        prf = prf.split('. ')[1:-1]
        ans = ''
        for tactic in prf:
            try:
                ans += t2c[tactic] + '0'
            except KeyError:
                pass
        ans.strip('0')

    return(ans)

goedel_proofs_main()

# goedel converter for types
# converts a formula to its goedel number
# converts a valid goedel number to a formula 


# goedel numbering dictionary
# default symbols are those of sympy's; Coq's are secondary; no sympy analog for Coq's '<->', 'forall' and 'exists' logical symbols
sym_dict = {'forall' : '1', 'exists' : '2', '=' : '3', '~': '4', '>>': '5', '->' : '5', '&': '6', '/\\' : '6', '|' : '7', '\\/' : '7', '<->' : '8', ')' : '9', '(' : '10', 'Prop' : '11,' 'nat' : '12'}

var_num = []
var_list = []


# converts a formula to its goedel number
# format -- Definition name : forall x1 x2 ... xn : nat, exists p q : Prop, expression.
# symbols must be separated by spaces
# propositional variables are 21, 211, 2111, ... natural number variables are 31, 311, 3111, ...
def goedel_encoder(wff):
    prenex = wff.split(',')[:-1].split(':')[1:].strip().split(' ')    # ['forall', 'x1', 'x2', ..., 'xn', 'nat', 'exists', 'p', 'q', 'Prop']
    expr = wff.split(',')[-1].strip('.').strip(' ').split[' ']    # ' expression.' is stripped and split
    num = ''
    
    for var in prenex:           # TO DO: loop in reverse to know types beforehand, add more types
        if var is 'Prop':
            vnum = '2'
        elif var is 'nat':
            vnum = '3'
        elif var not in sym_dict:    # won't work if variables are repeated
            var_list.append(var)
            vnum += '1'
            var_num.append(vnum)

    sym_dict.update(dict(zip(var_list, var_num)))
    wff = prenex + expr

    for sym in wff:
        sym = sym.strip()
        num += sym_dict[sym] + '0'
        
    num = num.strip('0')
    return(num)

# generates variable symbols x0, x1, x3, ...
# TO DO: separate variable names by types
def vargen(varcount):
    var = 'x' + str(varcount)
    return(var)
    

# converts a valid number to a theorem
def goedel_decoder(num):                 # takes in a string number like '12013'
    sym_list = list(sym_dict.items())    # create an array of (symbol, number) pairs
    wff = ''
    num = num.split('0')                 # ['12', '13'] 
    varcount = 0
    
    for symnum in num:
        if int(symnum) > 20:             # checks if symbol is a variable
            var = vargen(varcount)       # generates new variables based on the previous
            wff += var
            varcount += 1
        else:
            for pair in sym_list:
                (sym, num) = pair
                if num == symnum:
                    wff += sym + ' '
        
    wff = wff.strip()
    wff += '.'
    return(wff)


# main function -- calls the encoder/decoder according to the thm_obj type in 'object' file
def goedel_main():
    obj = open('/home/wrick/Documents/logia/object', 'r').readline()
    if obj.isdigit():
        val = goedel_decoder(obj)
    else:
        val = goedel_encoder(obj)
    return(val)


goedel_main()


# TO DO:
# sync with satsolver

# SAT Solver for LOGIA
# takes a proposition and outputs the possible cases of propositional variables for which the proposition evaluates to True
# this is to avoid the halting problem and find possible paths of proving a proposition


from sympy import symbols, satisfiable


def satsolver_main():
    prop = open('.../logia/prop', 'r').readline()    # of the form -- Proposition name : forall p q r :Prop, expression.
    expr = prop.split(',')[-1].strip('.')            # expression without leading space or trailing .
    varnames = split(':')[1].strip()[7:].replace(' ', ',')    # store the names of the variables as a string, split with ','
    varlist = list(symbols(varnames))                # create and store the symbols themselves in a list

    try:
        models = []
        sat = satisfiable(expr, all_models = True)
        while True:
            models.append(next(sat))
    except StopIteration:
        pass

    return(models)

satsolver_main()
  
# TO DO: multiple propositions

