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
                vars[self.tok]=self.tok
                return vars[self.tok]
            else:
                return vars[self.tok]
        except KeyError :
            print("Error : variable %s undefined!" % self.tok)
    return self.tok

@addToClass(AST.ForNode)
def execute(self) :
    self.children[0].execute()
    while (self.children[1].execute() == 1):
        self.children[3].execute()
        self.children[2].execute()
        vars[self.children[0].children[0].tok]+= self.children[2].execute()

@addToClass(AST.DelNode)
def execute(self):
    a=-1
    for i in range(0,len(vars[self.children[0].tok[0]])):
        if str(vars[self.children[0].tok][i]) == str(self.children[1]).replace("\"", "").replace("\n",""):
            a=i
    if a is not -1:
        vars[self.children[0].tok]=np.delete(vars[self.children[0].tok],a)

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
    for i in range(0, 5):
        for mot in self.children[0].execute():
            print("".join(dictionary[mot][i]),end="")
        print()
    print()

@addToClass(AST.LessNode)
def execute(self):
    if (self.children[0].execute() < self.children[1].execute()):
        return 1
    else:
        return 0

@addToClass(AST.MoreNode)
def execute(self):
    if (self.children[0].execute() > self.children[1].execute()):
        return 1
    else:
        return 0

@addToClass(AST.IfNode)
def execute(self):
    if (self.children[0].execute() != 0):
        return str(self.children[1].execute())

@addToClass(AST.SizeNode)
def execute(self):
    sizeValue=np.shape(self.children[0].execute())
    return sizeValue

if __name__ == "__main__" :
    from parserProjet import parse
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    ast.execute()