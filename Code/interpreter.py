from array import array
from sympy import Matrix
import AST
import numpy as np
from letterDict import dictionary

operations = {
    '+':  lambda x,y: np.hstack((x, y)),
    'mul' : lambda x,y :(np.tile(x,y)),
}
stack = []
vars = {}

def valueOfToken(t) :
    if isinstance(t,str) :
        try :
            if t[0]=="'":
                return dictionary[t]
            else:
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
                print ("".join(valueOfToken(val)[i]))
            print()
        elif node.__class__ == AST.OpNode:
            arg2 = valueOfToken(stack.pop())
            if node.nbargs == 2:
                arg1 = valueOfToken(stack.pop())
            else :
                arg1 = 0
            stack.append(operations[node.op](arg1, arg2))
        elif node.__class__ == AST.AssignNode:
            val = valueOfToken(stack.pop())
            name = stack.pop()
            vars[name] = val
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