from os import system, chdir
from numpy.random import randint
from glob import glob
from sympy import *
import readline

def shell():
    path = '/home/wrick/Documents/logia/'
    system('clear')
    errmsg = ['! But it\'s the semantics that matters.', '. I don\'t understand meatspeak.', '! Once a monkey found a typewriter...', '. It\'s okay to be human!', '... I\'m sorry, I\'m afraid I cannot do that.', '! Entropy sure is high today!']
    #errmsg = [' ']
    print('Logia Shell 0.1. Welcome aboard!\n')
    init_printing(use_unicode=True)
    log = []

    
    while True:
        try:
            usr = input('\n\N{LEFT VERTICAL BAR WITH QUILL}  ').lower()
            log.append(usr)
            expr = usr.split(' ')[-1].strip()
            try:
                exps = sympify(expr)
                a, b, c, d, i, j, k, l, m, n, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d i j k l m n p q r s t u v w x y z')
            except:
                pass

            
            if('prove' in usr):
                print('\nLoading Universes...    ')
                system('python3 ' + path + '03_logia.py')
                print('Done.')
            elif('com' in usr):
                usr = input('Enter file name:  ')
                system('coqtop -compile $PWD/'+usr)
            elif('edit' in usr):
                usr = input('Enter file name:  ')
                system('nano ' + '$PWD/' + usr.strip() + '.v')
                
                
            elif('eval' in usr):
                ans = exps.evalf()
                print(ans)
            elif('dif' in usr):
                ans = diff(exps, x)
                print(ans)
            elif('int' in usr):
                ans = integrate(exps, x)
                print(ans)
            elif('expand' in usr):
                ans = expand(exps.series())
                print(ans)
            elif('solve' in usr):

                    # add a linear solver
                                    
                ans = solveset(exps, x)
                print(ans)
            elif('sat' in usr):
                models = satisfiable(exps, all_models=True)
                try:
                    while True:
                        print(next(models))
                except StopIteration:
                    pass
            elif('prime' in usr):
                n = int(usr.split(' ')[-1].strip())
                sieve.extend_to_no(n-1)
                if('primes' in usr):
                    for i in range(n):
                        print(sieve._list[i], end='  ', flush=True)
                else:
                    print(sieve._list[n-1], end=' ', flush=True)
                print()
            elif('fac' in usr):
                if('x' in usr or 'y' in usr or 'z' in usr or 'w' in usr):
                    ans = factor(exps)
                else:
                    n = int(usr.split(' ')[-1].strip())
                    ans = factorint(n)
                print(ans)
                
                
            elif('proofnum' in usr):
                system('python3 ' + path + 'goedel_proofs.py')
            elif('typenum' in usr):
                system('python3 ' + path + 'goedel_types.py')


            elif('del' in usr):
                system('python3 ' + path + 'del.py')
            elif('qed' in usr):
                system('clear')
                return(0)
            elif('cls' in usr):
                system('clear')
            elif('help' in usr):
                help = open(path + 'shell_help', 'r').read()
                print('\n' + help)
            elif('find' in usr):
                usr = '*' + expr + '*'
                for name in glob(usr):
                    print(name)
            elif('cd' in usr):
                usr = input('Enter path:  ')
                try:
                    chdir(usr)
                except FileNotFoundError:
                    system('pwd')
            elif(len(usr.replace(' ',''))==0):
                continue
            else:
                print('Syntax Error' + errmsg[randint(len(errmsg))])

        except:
            print('Critical Error! Please reinstall Universe and reboot.')
    
shell()
