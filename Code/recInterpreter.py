import AST
from AST import addToClass
from functools import reduce
import numpy as np
from letterDict import dictionary

operations = {
    '+':  lambda x,y: np.hstack((x, y)),
    'mul' : lambda x,y :(np.tile(x,y)),
}
vars ={}

@addToClass(AST.ProgramNode)
def execute(self) :
    for c in self.children :
        c.execute()

@addToClass(AST.TokenNode)
def execute(self) :
    if isinstance(self.tok,str) :
        try :
            if self.tok[0]=="'":
                return dictionary[self.tok]
            else:
                return vars[self.tok]
        except KeyError :
            print("Error : variable %s undefined!" % self.tok)
    # if isinstance(self.tok,np.ndarray):
    #     try:
    #         return dictionary[self.tok]
    #     except KeyError:
    #         print("Error : variable %s undefined!" % self.tok)
    return self.tok

@addToClass(AST.OpNode)
def execute(self) :
    args = [c.execute() for c in self.children]
    if len(args) == 1 :
        args.insert(0,0)
    return reduce(operations[self.op],args)

@addToClass(AST.AssignNode)
def execute(self) :
    vars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.WhileNode)
def execute(self) :
    while (self.children[0].execute() == 1):
        self.children[1].execute()

@addToClass(AST.LineNode)
def execute(self) :
    #print(self.children[0].execute())
    #print(np.array_str(self.children[0].execute()))
    print ("\n".join(" ".join(map(str, line)) for line in self.children[0].execute()))
    #print(''.join(self.children[0].execute()))
    print()

@addToClass(AST.LessNode)
def compile(self):
    if (self.children[0].compile() < self.children[1].compile()):
        return 1
    else:
        return 0

@addToClass(AST.MoreNode)
def compile(self):
    if (self.children[0].compile() > self.children[1].compile()):
        return 1
    else:
        return 0

@addToClass(AST.IfNode)
def compile(self):
    self.children[0].compile()
    return 1


def size(node):
    #sizeValue = np.shape(valueOfToken(node))
    return 1

if __name__ == "__main__" :
    from parserProjet import parse
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    #print(ast)
    ast.execute()