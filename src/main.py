
symbol_table = {}

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class PrintNode(Node):
    def __init__(self, statement):
        self.statement = statement

    def execute(self):
        global symbol_table
        if self.statement in symbol_table:
            print(symbol_table[self.statement])
        else:
            print(self.statement)
        return 0

class IfNodeSingle(Node):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def execute(self):
        if (self.condition.evaluate() == 1):
            self.block.execute()

class WhileNode(Node):
    def __init__(self, condition, expression):
        self.condition = condition
        self.expression = expression

    def execute(self):
        print(self.expression)
        while self.condition.evaluate() == 1:
            self.expression.execute()


class StringNode(Node):
    def __init__(self, v):
        self.value = v.replace("\"", "")

    def evaluate(self):
        return self.value

class VariableNameNode(Node):
    global symbol_table
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return self.name

class VariableNode(Node):
    global symbol_table
    def __init__(self, name, val):
        self.name = name
        self.val = val
        symbol_table[self.name] = self.val

    def execute(self):
        symbol_table[self.name] = self.val

    def evaluate(self):
        return symbol_table[self.name]

class NumberNode(Node):
    def __init__(self, v):
        if ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value


class ListNode(Node):
    def __init__(self):
        self.value = []

    def add(self, v):
        self.value.insert(0, v)

    def evaluate(self):
        return self.value


class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == '//'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == '%'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '<'):
            return 1 if self.v1.evaluate() < self.v2.evaluate() else 0
        elif (self.op == '<='):
            return 1 if self.v1.evaluate() <= self.v2.evaluate() else 0
        elif (self.op == '=='):
            return 1 if self.v1.evaluate() == self.v2.evaluate() else 0
        elif (self.op == '>'):
            return 1 if self.v1.evaluate() > self.v2.evaluate() else 0
        elif (self.op == '>='):
            return 1 if self.v1.evaluate() >= self.v2.evaluate() else 0
        elif (self.op == '<>'):
            return 1 if self.v1.evaluate() != self.v2.evaluate() else 0
        elif (self.op == 'and' and type(self.v1.evaluate()) == int and type(self.v2.evaluate()) == int):
            return 1 if self.v1.evaluate() != 0 and self.v2.evaluate() != 0 else 0
        elif (self.op == 'or' and type(self.v1.evaluate()) == int and type(self.v2.evaluate()) == int):
            return 1 if self.v1.evaluate() != 0 or self.v2.evaluate() != 0 else 0
        elif (self.op == 'in'):
            return 1 if self.v1.evaluate() in self.v2.evaluate() else 0
        elif (self.op == 'not' and type(self.v1.evaluate()) == int):
            return 1 if not self.v1.evaluate() else 0
        elif (self.op == '['):
            return self.v1[self.v2]

reserved = {
    'if' : 'IF',
    'print' : 'PRINT',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'in' : 'IN',
    'not' : 'NOT',
    'or' : 'OR',
    'and' : 'AND'

}

tokens = [
    'NUMBER',
    'STRING',
    'VARIABLE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EXP',
    'FDIV',
    'PLUS',
    'MINUS',
    'LT',
    'LTEQ',
    'EQ',
    'NOTEQ',
    'GT',
    'GTEQ',
    'COMMA',
    'SEMICOLON',
    'LCURLYBRACE',
    'RCURLYBRACE',
    'EQUALS'
] + list(reserved.values())

# Tokens
t_SEMICOLON = r';'
t_LCURLYBRACE = r'{'
t_RCURLYBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN=r'\)'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_EXP = r'\*\*'
t_FDIV = r'//'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LT = r'<'
t_LTEQ = r'<='
t_EQ = r'=='
t_NOTEQ = r'<>'
t_GT = r'>'
t_GTEQ = r'>='
t_COMMA = r','
t_EQUALS = r'='


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_STRING(t):
    r'\"[^\"]*\"'
    try:
        t.value = StringNode(t.value)
    except ValueError:
        print("String is invalid %s", t.value)
        t.value = 0
    return t


def t_VARIABLE(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    t.value = VariableNameNode(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

# Ignored characters
t_ignore = " \t\n"

def t_error(t):
    print("Syntax error at '%s'" % t.value)


# Build the lexer
import ply.lex as lex

lex.lex()

# Parsing rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LT', 'LTEQ', 'EQ', 'NOTEQ', 'GT', 'GTEQ'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FDIV'),
    ('left', 'EXP'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN')
)

temp_list = ListNode()


def p_start(t):
    '''start : block'''
    t[0] = t[1]

def p_block_empty(t):
    '''block : LCURLYBRACE RCURLYBRACE'''
    t[0] = None


def p_block_single_stmt(t):
    '''block : LCURLYBRACE stmt_tail RCURLYBRACE'''
    t[0] = t[2]

def p_stmt_tail_end(t):
    '''stmt_tail : stmt'''
    t[0] = t[1]

def p_stmt_tail(t):
    '''stmt_tail : stmt stmt_tail'''
    t[0] = t[2]

def p_stmt(t):
    '''stmt : while
            | assignment
            | conditional
            | print'''
    t[0] = t[1].execute()

def p_print(t):
    '''print : PRINT LPAREN expr RPAREN SEMICOLON'''
    t[0] = PrintNode(t[3].evaluate())

def p_assignment(t):
    '''assignment : VARIABLE EQUALS expr SEMICOLON'''
    global symbol_table
    t[0] = VariableNode(t[1].evaluate(), t[3].evaluate())

def p_while(t):
    '''while : WHILE LPAREN expression RPAREN block'''
    t[0] = WhileNode(t[3], t[5])

def p_if(t):
    '''conditional : IF LPAREN expression RPAREN block'''
    t[0] = IfNodeSingle(t[3], t[5])

def p_if_else(t):
    '''conditional : IF LPAREN expression RPAREN block else_if_blocks'''

def p_else_if_blocks(t):
    '''else_if_blocks : else_if_block'''
    t[0] = t[1]

def p_else_if_blocks_mult(t):
    '''else_if_blocks : else_if_block else_if_blocks'''

    t[0] = t[2]

def p_else_if_block(t):
    '''else_if_block : ELSE block'''
    t[0] = t[2]

def p_start_list(t):
    '''expr : LBRACKET list_elem RBRACKET'''

    global temp_list
    temp_list = ListNode()

    t[0] = t[2]


def p_expr_list_index(t):
    '''expr : expr LBRACKET expression RBRACKET'''

    if type(t[3].evaluate()) == int and type(t[1].evaluate()) != int and type(t[1].evaluate()) != float:
        if isinstance(t[1], VariableNameNode):
            global symbol_table
            t[0] = BopNode('[', symbol_table[t[1].evaluate()], t[3].evaluate())
        else:
            t[0] = BopNode('[', t[1].evaluate(), t[3].evaluate())
    else:
        p_error(t[1])


def p_empty_list(t):
    '''expr : LBRACKET RBRACKET'''
    t[0] = ListNode()


def p_expr_single_exp(t):
    '''expr : expression'''
    t[0] = t[1]


def p_list_elem(t):
    '''list_elem : expr list_tail'''

    global temp_list
    temp_list.add(t[1].evaluate())

    t[0] = t[2]

def p_list_tail(t):
    '''list_tail : COMMA expr list_tail'''
    global temp_list
    temp_list.add(t[2].evaluate())

    t[0] = t[3]


def p_single_list_tail(t):
    '''list_tail : '''
    global temp_list
    t[0] = temp_list


def p_statement_paren(t):
    '''expr : LPAREN expr RPAREN'''
    t[0] = t[2]


def p_expression_binop(t):
    '''expression : expression LT expression
                  | expression LTEQ expression
                  | expression EQ expression
                  | expression NOTEQ expression
                  | expression GT expression
                  | expression GTEQ expression
                  | expression AND expression
                  | expression OR expression
                  | expression NOT expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression FDIV expression
                  | expression EXP expression
                  | expression MOD expression'''

    if type(t[1].evaluate()) == str and type(t[3].evaluate()) == str and t[2] != '+':
        p_error(t[1])
    else:
        t[0] = BopNode(t[2], t[1], t[3])


def p_expression_factor(t):
    '''expression : factor
                    | string'''
    t[0] = t[1]

def p_expression_variable(t):
    '''expression : VARIABLE'''
    global symbol_table
    value = symbol_table[t[1].evaluate()]
    if type(value) == int or type(value) == float:
        t[0] = NumberNode(str(value))
    else:
        t[0] = t[1]


def p_factor(t):
    '''factor : NUMBER'''
    t[0] = t[1]

def p_string(t):
    '''string : STRING'''
    t[0] = t[1]

def p_error(t):
    if type(t.evaluate()) != str:
        print(t.evaluate())
        print("SYNTAX ERROR")
    elif type(t.evaluate()) == str:
        print("SEMANTIC ERROR")
    exit(1)



import ply.yacc as yacc

yacc.yacc()

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')

try:
    code = fd.read()

    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        # print(token)

    ast = yacc.parse(code)
    #print(symbol_table)
except IndexError:
    print("SEMANTIC ERROR")
