# LOGIA : an automated theorem prover
# -----------------------------------
# 
# version 0.1, December 13, 2016
# for use with Coq 8.5pl3 (Oct 2016)
# written by wrick
# 
# -----------------------------------
# randomly genned tactics from a static tactics_base
# no reproduction, mutation or natural selection


from numpy.random import randint
from os import system


qed     = False
theorem = open( '/home/wrick/Documents/logia/theorem', 'r').readline()
tactics = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
T       = len(tactics) - 1                            # size of the tactics base


def proofgen() :
    proof  = 'Proof.'                                 # start proof
    length = randint(1, 5)                            # length of the proof
    keys   = randint(0, T, size = length)             # picks out tactics

    for i in keys :
        proof += ' ' + tactics[i] + '.'

    proof += ' Defined.\n'
    return(proof)


def logia_main():
    while qed == False :
        Proof = open('/home/wrick/Documents/logia/Proof.v', 'w')
        Proof.write(theorem + '\n' + proofgen())
        Proof.close()
        system('coqtop -compile /home/wrick/Documents/logia/Proof')
        qed = system('test -e /home/wrick/Documents/logia/Proof.vo')                  
    
logia_main()

# ---EOF---
