import ply.yacc as yacc

from lexProjet import tokens
import AST

vars = {}

def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])

def p_structure_if(p):
    ''' structure : IF expression '{' programme '}' '''
    p[0] = AST.IfNode([p[2],p[4]])

def p_structure_for(p):
    ''' structure : FOR '(' assignation ';' expression ';' expression ')'  '{' programme '}' '''
    p[0] = AST.ForNode([p[3],p[5],p[7],p[10]])

def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : assignation
            | structure '''
    p[0] = p[1]

def p_statement_line(p):
    ''' statement : LINE expression '''
    p[0] = AST.LineNode(p[2])

def p_statement_size(p):
    ''' statement : SIZE expression '''
    p[0] = AST.SizeNode(p[2])

def p_expression_op(p):
    '''expression : expression ADD_OP expression
            | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_expression_num_or_var(p):
    '''expression : NUMBER
        | IDENTIFIER'''
    p[0] = AST.TokenNode(p[1])

def p_expression_mat(p):
    '''expression : MAT'''
    p[0] = AST.TokenNode(p[1])

def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

def p_expression_less(p):
    ''' expression : expression '<' expression '''
    p[0] = AST.LessNode([p[1], p[3]])

def p_expression_more(p):
    ''' expression : expression '>' expression '''
    p[0] = AST.MoreNode([p[1], p[3]])

def p_expression_char(p):
    '''expression : CHAR'''
    p[0] = AST.TokenNode(p[1])

def p_statement_del(p):
    '''statement : expression DEL expression '''
    p[0] = AST.DelNode(p[1])

def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('left', 'DEL'),
    ('right', '<'),
    ('right', '>'),
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    if result:
        print (result)

        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name)
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")