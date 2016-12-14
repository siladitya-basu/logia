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
theorem = open( '.../logia/theorem', 'r').readline()
tactics = open('.../logia/tactics_base', 'r').read().split('\n')
T       = len(tactics)                                # size of the tactics base


def proofgen() :
    proof  = 'Proof.'                                 # start proof
    length = randint(1, 5)                            # length of the proof
    keys   = randint(0, T, size = length)             # picks out tactics

    for i in keys :
        proof += ' ' + tactics[i] + '.'

    proof += ' QED.\n'
    return(proof)


while qed == False :
    Proof = open('.../logia/Proof', 'w')
    Proof.write(theorem + '\n' + proofgen())
    Proof.close()
    system('coqc -compile .../logia/Proof')
    compiled = open('.../logia/Proof.vo', 'r')
    qed = isinstance(compiled, file)                  # check with coqc to see if Proof.v compiles, set qed = True
    

# ---EOF---
