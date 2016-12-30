# goedel decoder/encoder for LOGIA
# converts a formula to its goedel numbering
# converts a valid goedel number to a formula 

from math import sqrt

# goedel numbering dictionary; keep '.' as the last key because the variable numberings start from there

sym_dict = {'forall' : 1, 'exists' : 2, '=' : 3, '~': 4, '->': 5, '&': 6, '/\\': 6, 'and' : 6, '|' : 7, '\\/' : 7, 'or' : 7, '<->' : 8, 'iff' : 8,  '.': 9, ')' : 10, '(' : 11, 'Prop' : 12, 'nat' : 13, '.' : 14}

var_count = 0
var_num = []
var_list = []


# naive prime generator

def nextprime(num):
    foundprime = False
    
    while not foundprime:
        num += 2
        
        for i in range(3, int(sqrt(num) + 1), 2):
            if num%i == 0:
                foundprime = False
                break
            foundprime = True

    return num


# converts a theorem to its goedel numbering
# format -- Theorem name : forall x1 x2 ... xn : Prop, statement.
# variables are at most 2 characters long, everything else must be at least 3 chars

def goedel_encoder(wff):
    temp = wff.split(',')[0].split(' ')    # get the quatifier part out
    for ch in temp:
        if len(ch)<=2 and ch.isalpha():
            var_count += 1                 # count number of variables
            var_list.append(ch)            # add variable to the list
            var_num.append(sym_dict['.'] + var_count)    # add variable's goedel numbering
    sym_dict.update(dict(zip(var_list, var_num)))        # update symbol dictionary with the variables

    goedel_num = 1
    temp = wff.split(':')[1:]
    prime = 3
    for part in temp:
        for symbol in part.split(' '):
            symbol = symbol.strip()
            symbol = symbol.replace(',', '')
            goedel_num *= prime**sym_dict[symbol]
            prime = nextprime(prime)
    return goedel_num


# converts a valid odd number to a theorem

def goedel_decoder(num):
    sym_list = list(sym_dict.items())    # create an array of (symbol, number) pairs
    prime = 3                            # primes mark the positions and starts with 3
    wff = ''

    while num > 1:
        count = 0
        while num % prime == 0:          # number of times prime divides num = symbol
            count += 1
            num /= prime

        prime = nextprime(prime)         # get the next prime/position marker

        for pair in sym_list:                 # add the symbol
            (sym, num) = pair
            if num == count:
                wff += sym + ' '
        
    wff = wff.strip()
    wff += '.'
    return wff


# main function -- calls the encoder/decoder according to the thm_obj type in 'object' file

def goedel_main():
    obj = open('.../logia/object', 'r').readline()
    if obj.isdigit():
        val = goedel_decoder(obj)
    else:
        val = goedel_encoder(obj)
    return val

goedel_main()


# TO DO:
# include support for polymorphic functions and dependent pair types
# syn with satsolver
