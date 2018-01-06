
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftLTLTEQEQNOTEQGTGTEQleftINleftPLUSMINUSleftFDIVleftEXPleftMODleftTIMESDIVIDEleftLPARENRPARENNUMBER STRING VARIABLE LPAREN RPAREN LBRACKET RBRACKET TIMES DIVIDE MOD EXP FDIV PLUS MINUS LT LTEQ EQ NOTEQ GT GTEQ COMMA SEMICOLON LCURLYBRACE RCURLYBRACE EQUALS NOT AND PRINT ELSE IF IN OR WHILEstart : blockblock : LCURLYBRACE RCURLYBRACEblock : LCURLYBRACE stmt_tail RCURLYBRACEstmt_tail : stmtstmt_tail : stmt stmt_tailstmt : while\n            | assignment\n            | conditional\n            | printprint : PRINT LPAREN expr RPAREN SEMICOLONassignment : VARIABLE EQUALS expr SEMICOLONwhile : WHILE LPAREN expression RPAREN blockconditional : IF LPAREN expression RPAREN blockconditional : IF LPAREN expression RPAREN block else_if_blockselse_if_blocks : else_if_blockelse_if_blocks : else_if_block else_if_blockselse_if_block : ELSE blockexpr : LBRACKET list_elem RBRACKETexpr : expr LBRACKET expression RBRACKETexpr : LBRACKET RBRACKETexpr : expressionlist_elem : expr list_taillist_tail : COMMA expr list_taillist_tail : expr : LPAREN expr RPARENexpression : expression LT expression\n                  | expression LTEQ expression\n                  | expression EQ expression\n                  | expression NOTEQ expression\n                  | expression GT expression\n                  | expression GTEQ expression\n                  | expression AND expression\n                  | expression OR expression\n                  | expression NOT expression\n                  | expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression FDIV expression\n                  | expression EXP expression\n                  | expression MOD expressionexpression : factor\n                    | stringexpression : VARIABLEfactor : NUMBERstring : STRING'
    
_lr_action_items = {'MINUS':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,33,-43,-42,-45,33,33,-36,33,-37,33,33,33,-38,-39,33,-40,33,-35,33,-41,33,33,33,]),'LT':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,34,-43,-42,-45,34,34,-36,-26,-37,-28,-27,34,-38,-39,-30,-40,34,-35,-29,-41,-31,34,34,]),'TIMES':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,35,-43,-42,-45,35,35,35,35,-37,35,35,35,-38,35,35,35,35,35,35,35,35,35,35,]),'VARIABLE':([1,6,8,9,11,13,14,15,16,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,74,77,80,81,82,83,87,88,],[7,7,-2,-7,-8,-9,-6,21,-3,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-11,-13,21,-10,-12,-14,-15,-16,-17,]),'LPAREN':([4,10,12,18,19,27,28,77,],[15,19,20,27,27,27,27,27,]),'SEMICOLON':([21,22,24,25,26,29,30,52,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,86,],[-44,-46,-43,-42,-45,-21,55,-20,80,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,-25,-18,-19,]),'PLUS':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,44,-43,-42,-45,44,44,-36,44,-37,44,44,44,-38,-39,44,-40,44,-35,44,-41,44,44,44,]),'$end':([2,3,8,16,],[-1,0,-2,-3,]),'RBRACKET':([21,22,24,25,26,28,29,51,52,53,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,78,79,85,86,89,],[-44,-46,-43,-42,-45,52,-21,76,-20,-24,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,-25,-18,-22,86,-24,-19,-23,]),'IF':([1,6,8,9,11,13,14,16,55,74,80,81,82,83,87,88,],[4,4,-2,-7,-8,-9,-6,-3,-11,-13,-10,-12,-14,-15,-16,-17,]),'STRING':([15,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,77,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'NUMBER':([15,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,77,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'EQ':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,36,-43,-42,-45,36,36,-36,-26,-37,-28,-27,36,-38,-39,-30,-40,36,-35,-29,-41,-31,36,36,]),'LCURLYBRACE':([0,49,57,84,],[1,1,1,1,]),'OR':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,38,-43,-42,-45,38,38,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,38,]),'DIVIDE':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,39,-43,-42,-45,39,39,39,39,-37,39,39,39,-38,39,39,39,39,39,39,39,39,39,39,]),'LBRACKET':([18,19,21,22,24,25,26,27,28,29,30,31,50,52,53,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,85,86,],[28,28,-44,-46,-43,-42,-45,28,28,-21,54,54,54,-20,54,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,-25,-18,28,54,-19,]),'GT':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,41,-43,-42,-45,41,41,-36,-26,-37,-28,-27,41,-38,-39,-30,-40,41,-35,-29,-41,-31,41,41,]),'EXP':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,42,-43,-42,-45,42,42,42,42,-37,42,42,42,-38,42,42,-40,42,42,42,-41,42,42,42,]),'FDIV':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,40,-43,-42,-45,40,40,40,40,-37,40,40,40,-38,-39,40,-40,40,40,40,-41,40,40,40,]),'NOT':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,43,-43,-42,-45,43,43,-36,-26,-37,-28,-27,43,-38,-39,-30,-40,-34,-35,-29,-41,-31,43,43,]),'RCURLYBRACE':([1,5,6,8,9,11,13,14,16,17,55,74,80,81,82,83,87,88,],[8,16,-4,-2,-7,-8,-9,-6,-3,-5,-11,-13,-10,-12,-14,-15,-16,-17,]),'NOTEQ':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,45,-43,-42,-45,45,45,-36,-26,-37,-28,-27,45,-38,-39,-30,-40,45,-35,-29,-41,-31,45,45,]),'EQUALS':([7,],[18,]),'LTEQ':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,37,-43,-42,-45,37,37,-36,-26,-37,-28,-27,37,-38,-39,-30,-40,37,-35,-29,-41,-31,37,37,]),'WHILE':([1,6,8,9,11,13,14,16,55,74,80,81,82,83,87,88,],[12,12,-2,-7,-8,-9,-6,-3,-11,-13,-10,-12,-14,-15,-16,-17,]),'MOD':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,46,-43,-42,-45,46,46,46,46,-37,46,46,46,-38,46,46,46,46,46,46,-41,46,46,46,]),'GTEQ':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,47,-43,-42,-45,47,47,-36,-26,-37,-28,-27,47,-38,-39,-30,-40,47,-35,-29,-41,-31,47,47,]),'PRINT':([1,6,8,9,11,13,14,16,55,74,80,81,82,83,87,88,],[10,10,-2,-7,-8,-9,-6,-3,-11,-13,-10,-12,-14,-15,-16,-17,]),'AND':([21,22,23,24,25,26,29,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,],[-44,-46,48,-43,-42,-45,48,48,-36,-26,-37,-28,-27,48,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,48,]),'ELSE':([8,16,74,83,88,],[-2,-3,84,84,-17,]),'COMMA':([21,22,24,25,26,29,52,53,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,85,86,],[-44,-46,-43,-42,-45,-21,-20,77,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,-25,-18,77,-19,]),'RPAREN':([21,22,23,24,25,26,29,31,32,50,52,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,86,],[-44,-46,49,-43,-42,-45,-21,56,57,75,-20,-36,-26,-37,-28,-27,-33,-38,-39,-30,-40,-34,-35,-29,-41,-31,-32,-25,-18,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt_tail':([1,6,],[5,17,]),'stmt':([1,6,],[6,6,]),'list_elem':([28,],[51,]),'else_if_blocks':([74,83,],[82,87,]),'start':([0,],[3,]),'assignment':([1,6,],[9,9,]),'factor':([15,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,77,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'conditional':([1,6,],[11,11,]),'print':([1,6,],[13,13,]),'expr':([18,19,27,28,77,],[30,31,50,53,85,]),'else_if_block':([74,83,],[83,83,]),'list_tail':([53,85,],[78,89,]),'block':([0,49,57,84,],[2,74,81,88,]),'string':([15,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,77,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'while':([1,6,],[14,14,]),'expression':([15,18,19,20,27,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,77,],[23,29,29,32,29,29,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,79,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> block','start',1,'p_start','main.py',271),
  ('block -> LCURLYBRACE RCURLYBRACE','block',2,'p_block_empty','main.py',275),
  ('block -> LCURLYBRACE stmt_tail RCURLYBRACE','block',3,'p_block_single_stmt','main.py',280),
  ('stmt_tail -> stmt','stmt_tail',1,'p_stmt_tail_end','main.py',284),
  ('stmt_tail -> stmt stmt_tail','stmt_tail',2,'p_stmt_tail','main.py',288),
  ('stmt -> while','stmt',1,'p_stmt','main.py',292),
  ('stmt -> assignment','stmt',1,'p_stmt','main.py',293),
  ('stmt -> conditional','stmt',1,'p_stmt','main.py',294),
  ('stmt -> print','stmt',1,'p_stmt','main.py',295),
  ('print -> PRINT LPAREN expr RPAREN SEMICOLON','print',5,'p_print','main.py',299),
  ('assignment -> VARIABLE EQUALS expr SEMICOLON','assignment',4,'p_assignment','main.py',303),
  ('while -> WHILE LPAREN expression RPAREN block','while',5,'p_while','main.py',308),
  ('conditional -> IF LPAREN expression RPAREN block','conditional',5,'p_if','main.py',312),
  ('conditional -> IF LPAREN expression RPAREN block else_if_blocks','conditional',6,'p_if_else','main.py',316),
  ('else_if_blocks -> else_if_block','else_if_blocks',1,'p_else_if_blocks','main.py',319),
  ('else_if_blocks -> else_if_block else_if_blocks','else_if_blocks',2,'p_else_if_blocks_mult','main.py',323),
  ('else_if_block -> ELSE block','else_if_block',2,'p_else_if_block','main.py',328),
  ('expr -> LBRACKET list_elem RBRACKET','expr',3,'p_start_list','main.py',332),
  ('expr -> expr LBRACKET expression RBRACKET','expr',4,'p_expr_list_index','main.py',341),
  ('expr -> LBRACKET RBRACKET','expr',2,'p_empty_list','main.py',354),
  ('expr -> expression','expr',1,'p_expr_single_exp','main.py',359),
  ('list_elem -> expr list_tail','list_elem',2,'p_list_elem','main.py',364),
  ('list_tail -> COMMA expr list_tail','list_tail',3,'p_list_tail','main.py',372),
  ('list_tail -> <empty>','list_tail',0,'p_single_list_tail','main.py',380),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_statement_paren','main.py',386),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','main.py',391),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_binop','main.py',392),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','main.py',393),
  ('expression -> expression NOTEQ expression','expression',3,'p_expression_binop','main.py',394),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','main.py',395),
  ('expression -> expression GTEQ expression','expression',3,'p_expression_binop','main.py',396),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','main.py',397),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','main.py',398),
  ('expression -> expression NOT expression','expression',3,'p_expression_binop','main.py',399),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',400),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','main.py',401),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','main.py',402),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','main.py',403),
  ('expression -> expression FDIV expression','expression',3,'p_expression_binop','main.py',404),
  ('expression -> expression EXP expression','expression',3,'p_expression_binop','main.py',405),
  ('expression -> expression MOD expression','expression',3,'p_expression_binop','main.py',406),
  ('expression -> factor','expression',1,'p_expression_factor','main.py',415),
  ('expression -> string','expression',1,'p_expression_factor','main.py',416),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','main.py',420),
  ('factor -> NUMBER','factor',1,'p_factor','main.py',430),
  ('string -> STRING','string',1,'p_string','main.py',434),
]
