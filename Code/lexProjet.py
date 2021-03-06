''' Created by Damien Gygi and Raphaël Schaffo
    04.02.2017
    HE-ARC
'''

import ply.lex as lex

reserved_words = (
	'line',
	'size',
	'if',
	'for',
	'del',
	'rep'
)

tokens = (
			 'NUMBER',
			 'CHAR',
			 'ADD_OP',
			 'MUL_OP',
			 'IDENTIFIER',
		 ) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '();={}<>'

def t_CHAR(t):
	r'\'([A-Za-z_]){1}\''
	return t

def t_ADD_OP(t):
	r'[+]'
	return t

def t_MUL_OP(t):
	r'mul'
	return t

def t_NUMBER(t):
	r'-*\d+'
	t.value = int(t.value)
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print ("Illegal character '%s'" % repr(t.value[0]))
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
