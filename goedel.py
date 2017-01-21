# goedel decoder/encoder for LOGIA
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
        elif var not in sym_dict:
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
    obj = open('.../logia/object', 'r').readline()
    if obj.isdigit():
        val = goedel_decoder(obj)
    else:
        val = goedel_encoder(obj)
    return(val)


goedel_main()


# TO DO:
# sync with satsolver
