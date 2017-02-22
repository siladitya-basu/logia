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
from glob import glob

system('nano /home/wrick/Documents/logia/theorem')
theorem    = open('/home/wrick/Documents/logia/theorem', 'r').readline()
#tactics    = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
tactics = ['assumption', 'destruct H as [a b]', '']
T          = len(tactics)        # the last tactic is a null tactic and randint has a closed-open domain
population = 5                   # constant population size for every generation
maxlength  = 2                   # maximum proof length


# create the seeds -- adds new proofs to the generation
def seedgen(generation):

    for i in range(population):
        length = randint(1, maxlength + 1)
        proof  = []

        for j in range(length):
            proof.append(randint(T))

        generation.append(proof)

    return(generation)


# define reproduction -- 2-parent crossover, creates a new proof with new length and all
def crossover(proof_tuple):
    (proof1, proof2) = proof_tuple
    newproof      = []
    prooflength   = randint(1, maxlength + 1)
    combine       = proof1 + proof2
    combinelength = len(combine)

    for i in range(prooflength):
        newproof.append(randint(0, combinelength + 1))    # min combinelength = 0

    return(newproof)


# define mutation -- as random as it can be, no dependencies, doesn't change proof length
def mutagen(proof):
    mutaprob = 13                         # probability of mutation is 1 in 13, 0 means zero probability
    newproof = []
    if mutaprob != 0:
        for i in proof:
            if randint(mutaprob) == 0:    # probability of getting a zero is 1/mutaprob
                newproof.append(randint(T))

    return(newproof)


# the new generation
def generationmap(generation):
    newgeneration = []
    
    for i in range(population):
        generation[i] = mutagen(generation[i])

    for i in range(population):
        proof_tuple = (generation[randint(population)], generation[randint(population)])
        newproof = crossover(proof_tuple)
        newgeneration.append(newproof)

    return(newgeneration)


# convert integer sequences to tactic strings
def proofgen(sequence):
    #proof = 'Proof '
    proof = 'Proof. intros.'
    invalidtactics = ['']    # a list of tactics not to be used in the proof, like one-use tactics, etc
    for i in sequence:
        if(tactics[i] not in invalidtactics):
            proof += ' ' + tactics[i] + '.'
        invalidtactics.append(tactics[i])
    proof += ' Defined.\n'
    return(proof)


# the main program
def logia_main():
    generation = seedgen([])
    qed = False

    while qed == False:
        
        for i in range(population):
            if qed == False:
                try:
                    Proof = open('/home/wrick/Documents/logia/proof.v', 'w')
                    Proof.write(theorem + proofgen(generation[i]))
                    Proof.close()
                    system('coqtop -compile /home/wrick/Documents/logia/proof')
                    if(len(glob('/home/wrick/Documents/logia/proof.vo'))!=0):
                       return(1)
                       
                except:
                    pass
        generation = generationmap(generation)
        
    return(qed)


logia_main()
system('nano /home/wrick/Documents/logia/proof.v')

# ---EOF---
