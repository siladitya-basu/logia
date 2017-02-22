# goedel converter for proofs
# assigns a goedel numbering for tactics in the tactics_base 

def goedel_proofs_main():
    tactics = open('/home/wrick/Documents/logia/tactics_base', 'r').read().split('\n')
    code = [str(i) for i in range(1,2*len(tactics), 2)]
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

    A = open('/home/wrick/Documents/logia/ans', 'w')
    A.write(ans)
    A.close()
#   return(ans)

goedel_proofs_main()
