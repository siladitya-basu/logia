# LOGIA : an automated theorem prover
# -----------------------------------
# 
# version 0.3, February 28, 2017
# for use with Coq 8.5pl3 (Oct 2016)
# written by wrick
# 
# -----------------------------------
# randomly genned tactics from a static tactics_base
# 2-parent crossover, random mutation
# longer, more correct proofs are selected


from numpy.random import randint
from os import system
from glob import glob
from re import search

abort = False
try:
    system('nano /home/wrick/Documents/logia/theorem.v')
    theorem = open('/home/wrick/Documents/logia/theorem.v', 'r').readline()
    tactics = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
    #tactics = ['assumption', 'destruct H as [a b]', '']
    T          = len(tactics)        # the last tactic is a null tactic and randint has a closed-open domain
    population = 5                   # constant population size for every generation
    maxlength  = 2                   # maximum proof length
    fit = 1.5                        # minimum fitness for survival
except FileNotFoundError:
    print('Does not exist. Abort.')
    abort = True

# create the seeds -- adds new proofs to the generation
def seedgen(generation):
    while len(generation) < population:
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


# the fitness function
def fitnesscheck(proof):
    errfile = open('/home/wrick/Documents/logia/errors', 'r')
    totlength = len(proof.strip())
    errlength = int(search('(?<=-)\w+', errfile.read()).group(0))    # search for a word after a hyphen as coqtop gives errors as '... characters xy-zw...'
    fitness = errlength/totlength
    errfile.close()    
    return(fitness)


# the main program
def logia_main():

    if(abort):
        return()
    
    generation = seedgen([])
    while True:
        newgeneration = []
        for i in range(population):
            try:
                Proof = open('/home/wrick/Documents/logia/proof.v', 'w')
                sequence = generation[i]
                proof = proofgen(sequence)
                Proof.write(theorem + proof)
                Proof.close()
                system('coqtop -compile /home/wrick/Documents/logia/proof > errors')
                if(len(glob('/home/wrick/Documents/logia/proof.vo'))!=0):
                    return()
                else:
                    fitness = fitnesscheck(proof)
                    if(fitness >= fit):
                        newgeneration.append(sequence)
            except:
                pass
        generation = generationmap(seedgen(newgeneration))
    return()


logia_main()
if(not abort):
    system('nano /home/wrick/Documents/logia/proof.v')

    
# ---EOF---
