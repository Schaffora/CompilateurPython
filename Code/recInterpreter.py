''' Created by Damien Gygi and Raphaël Schaffo
    04.02.2017
    HE-ARC
'''

import AST
from AST import addToClass
from functools import reduce
import numpy as np
from letterDict import dictionary

# Utilisation de numpy pour les opérations matricielles
operations = {
    '+':  lambda x,y: np.hstack((x, y)),
    'mul' : lambda x,y :(np.tile(x,y)),
}
vars ={}

# En cas de programme
@addToClass(AST.ProgramNode)
def execute(self) :
    for c in self.children :
        c.execute()

# En cas de token
@addToClass(AST.TokenNode)
def execute(self) :
    if isinstance(self.tok,str) :
        try :
            if self.tok[0]=="'":
                vars[self.tok]=[self.tok]
                return vars[self.tok]
            else:
                return vars[self.tok]
        except KeyError :
            print("Error : variable %s undefined!" % self.tok)
    return self.tok

# En cas de boucle
@addToClass(AST.ForNode)
def execute(self) :
    self.children[0].execute()
    while (self.children[1].execute() == 1):
        self.children[3].execute()
        self.children[2].execute()
        vars[self.children[0].children[0].tok]+= self.children[2].execute()

# En cas de suppresion
@addToClass(AST.DelNode)
def execute(self):
    a=-1
    for i in range(0,len(vars[self.children[0].tok[0]])):
        if str(vars[self.children[0].tok][i]) == str(self.children[1]).replace("\"", "").replace("\n",""):
            a=i
    if a is not -1:
        vars[self.children[0].tok]=np.delete(vars[self.children[0].tok],a)

# En cas de remplacement
@addToClass(AST.RepNode)
def execute(self):
    a=-1
    for i in range(0,len(vars[self.children[0].tok[0]])):
        if str(vars[self.children[0].tok][i]) == str(self.children[1]).replace("\"", "").replace("\n",""):
            a=i
    if a is not -1:
        vars[self.children[0].tok] = np.delete(vars[self.children[0].tok], a)
        vars[self.children[0].tok] = np.insert(vars[self.children[0].tok],a,str(self.children[2]).replace("\"", "").replace("\n",""))

# En cas d'opération
@addToClass(AST.OpNode)
def execute(self) :
    args = [c.execute() for c in self.children]
    if len(args) == 1 :
        args.insert(0,0)
    return reduce(operations[self.op],args)

# En cas d'assignation
@addToClass(AST.AssignNode)
def execute(self) :
    vars[self.children[0].tok] = self.children[1].execute()

# En cas d'affichage
@addToClass(AST.LineNode)
def execute(self) :
    for i in range(0, 5):
        for mot in self.children[0].execute():
            print("".join(dictionary[mot][i]),end="")
        print()
    print()

# Si plus petit que
@addToClass(AST.LessNode)
def execute(self):
    if (self.children[0].execute() < self.children[1].execute()):
        return 1
    else:
        return 0
# Si plus grand que
@addToClass(AST.MoreNode)
def execute(self):
    if (self.children[0].execute() > self.children[1].execute()):
        return 1
    else:
        return 0

# En cas de condition
@addToClass(AST.IfNode)
def execute(self):
    if (self.children[0].execute() != 0):
        return str(self.children[1].execute())

# Récupération de la taille de la matriace
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