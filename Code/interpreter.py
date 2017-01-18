from array import array

import AST
from sympy import Matrix
import numpy as np
operations = {
    # '+' : lambda x,y : x+y,
    # '+':  lambda x,y: list(map(print, x+y)),
    '+':  lambda x,y: np.hstack((x, y)),
    'mul' : lambda x,y :x*y,
}
stack = []
vars = {}

dictionary = {
    "'a'":[[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1]],
    "'b'":[[1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0]]
}

def add(x,y):
    for i in range(0,5):
        x[i]+y[i]


def valueOfToken(t) :
    if isinstance(t,str) :
        try :
            return vars[t]
        except KeyError :
            print("Error : variable %s undefined!" % t)
    return t

def execute(node) :
    while node :
        if node.__class__ in [AST.EntryNode , AST.ProgramNode] :
            pass
        elif node.__class__ == AST.TokenNode :
            stack.append(node.tok)
        elif node.__class__ == AST.LineNode :
            val = stack.pop()
            for i in range(0,5):
                print (valueOfToken(val)[i])
        elif node.__class__ == AST.OpNode:
            arg2 = valueOfToken(stack.pop())
            if node.nbargs == 2:
                arg1 = valueOfToken(stack.pop())
            else :
                arg1 = 0
            stack.append(operations[node.op](arg1, arg2))
        elif node.__class__ == AST.AssignNode:
            val = stack.pop()
            name = stack.pop()
            vars[name] = dictionary[val]
            # print(vars[name])
        if node.next :
            node = node.next[0]
        else :
            node = None

if __name__ ==  "__main__" :
    from parserProjet import parse
    from threader import thread
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    entry = thread(ast)

    execute(entry)