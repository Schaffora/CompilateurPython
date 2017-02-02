
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '4AB53F085AC1B89F0EAB7C3F9F4127A4'
    
_lr_action_items = {'CHAR':([1,3,5,13,18,19,20,],[14,14,14,14,14,14,14,]),'ADD_OP':([9,10,11,12,14,15,16,21,24,25,26,27,],[-12,19,-10,-11,-14,19,19,19,19,-8,-9,-13,]),'(':([1,3,5,13,18,19,20,],[13,13,13,13,13,13,13,]),'MUL_OP':([9,10,11,12,14,15,16,21,24,25,26,27,],[-12,20,-10,-11,-14,20,20,20,20,20,-9,-13,]),'MAT':([1,3,5,13,18,19,20,],[9,9,9,9,9,9,9,]),'}':([2,4,6,9,10,11,12,14,16,23,24,25,26,27,28,29,],[-4,-5,-1,-12,-6,-10,-11,-14,-7,-3,-15,-8,-9,-13,29,-2,]),'{':([9,11,12,14,15,25,26,27,],[-12,-10,-11,-14,22,-8,-9,-13,]),'SIZE':([0,17,22,],[5,5,5,]),'$end':([2,4,6,8,9,10,11,12,14,16,23,24,25,26,27,29,],[-4,-5,-1,0,-12,-6,-10,-11,-14,-7,-3,-15,-8,-9,-13,-2,]),')':([9,11,12,14,21,25,26,27,],[-12,-10,-11,-14,27,-8,-9,-13,]),'IF':([0,17,22,],[3,3,3,]),'=':([7,],[18,]),'NUMBER':([1,3,5,13,18,19,20,],[11,11,11,11,11,11,11,]),'LINE':([0,17,22,],[1,1,1,]),'IDENTIFIER':([0,1,3,5,13,17,18,19,20,22,],[7,12,12,12,12,7,12,12,12,7,]),';':([2,4,6,9,10,11,12,14,16,24,25,26,27,29,],[-4,-5,17,-12,-6,-10,-11,-14,-7,-15,-8,-9,-13,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignation':([0,17,22,],[2,2,2,]),'statement':([0,17,22,],[6,6,6,]),'programme':([0,17,22,],[8,23,28,]),'expression':([1,3,5,13,18,19,20,],[10,15,16,21,24,25,26,]),'structure':([0,17,22,],[4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parserProjet.py',9),
  ('structure -> IF expression { programme }','structure',5,'p_structure_if','parserProjet.py',13),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parserProjet.py',17),
  ('statement -> assignation','statement',1,'p_statement','parserProjet.py',21),
  ('statement -> structure','statement',1,'p_statement','parserProjet.py',22),
  ('statement -> LINE expression','statement',2,'p_statement_line','parserProjet.py',26),
  ('statement -> SIZE expression','statement',2,'p_statement_size','parserProjet.py',30),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parserProjet.py',34),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parserProjet.py',35),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_var','parserProjet.py',39),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parserProjet.py',40),
  ('expression -> MAT','expression',1,'p_expression_mat','parserProjet.py',44),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parserProjet.py',48),
  ('expression -> CHAR','expression',1,'p_expression_char','parserProjet.py',52),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parserProjet.py',56),
]
