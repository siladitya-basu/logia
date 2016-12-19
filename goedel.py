# goedel encoder/decoder for LOGIA
# converts the theorem into its goedel numbering and vice versa
# requires proper formatting -- splitting is done by whitespaces


# naive prime generator
def nextprime(num):
    while True:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                num += 1
                continue
        return(num)
        

# Goedel Numbering:
# identifier    ---    prime
# forall               2
# :Prop                3
# ,                    5
# ~                    7
# ->                   11
# &                    13
# |                    17
# <->                  19
# variables            23 onwards


def goedel_encoder(theorem_file_object):
    theorem = theorem_file_object.readline().split(' ')
    length = len(theorem)

    goedel_num = 1
    var_prime = 23

    for i in range(length):
        ident = theorem[i]
        if ident == 'forall':
            goedel_num *= 2**i
        elif ident == ':Prop':
            goedel_num *= 3**i
        elif ident == ',':
            goedel_num *= 5**i
        elif ident == '~':
            goedel_num *= 7**i
        elif ident == '->':
            goedel_num *= 11**i
        elif ident == '&':
            goedel_num *= 13**i
        elif ident == '|':
            goedel_num *= 17**i
        elif ident == '<->':
            goedel_num *= 19**i
        elif ident.isalpha():
            goedel_num *= var_prime**i
            var_prime = nextprime(var_prime)
        else:
            goedel_num *= 1
        
    return(goedel_num)
# encoder fails for incorrectly formatted propositions!
    
    
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
    
