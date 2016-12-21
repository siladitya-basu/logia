# goedel encoder/decoder for LOGIA
# converts the theorem into its goedel numbering and vice versa
# requires proper formatting -- splitting is done by whitespaces

from math import sqrt

# naive prime generator
def nextprime(num):
    while True:
        num += 1
        for i in range(2, sqrt(num) + 1):
            if num % i == 0:
                num += 1
                continue
        return(num)
        

# Goedel Numbering:
# Identifier    ---    Goedel number
# forall               1
# exists               2
# :Prop                3
# ~                    4
# ->                   5
# &                    6
# |                    7
# <->                  8
# .                    9
# variables            10 onwards


def goedel_encoder(theorem_file_object):
    theorem = theorem_file_object.readline().split(',')    # splits the theorem into the 'variables' part and the 'statement' part
    statement = theorem[1]
    vardict = dict
    length = len(theorem)

    goedel_num = 1
    prime = 2
    var_num = 10

    for i in range(length):
        ident = theorem[i]
        if ident == 'forall':
            goedel_num *= prime**1
        elif ident == 'exists':
            goedel_num *= prime**2
        elif ident == ':Prop':
            goedel_num *= prime**3
        elif ident == '~':
            goedel_num *= prime**4
        elif ident == '->':
            goedel_num *= prime**5
        elif ident == '&':
            goedel_num *= prime**6
        elif ident == '|':
            goedel_num *= prime**7
        elif ident == '<->':
            goedel_num *= prime**8
        elif ident.isalpha():
            goedel_num *= prime**var_num
            var_num += 1
        else:
            goedel_num *= 1    
        
        prime = nextprime(prime)
    return(goedel_num)
    
    
def goedel_decoder(number):
    # use efficient prime factorisation to decode
    # then return a string corresponding to the goedel nubering
    return 0
    
def goedel_main():
    obj = input()
    if obj.isdigit():
        result = goedel_decoder(int(obj))
    else:
        theorem_file_object = open('.../logia/theorem', 'r')
        result = goedel_encoder(theorem_file_object)
        
    return result
    

goedel_main()

# TO DO:
# decoder
# improve the encoder
    
