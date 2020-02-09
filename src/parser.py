from rply import ParserGenerator
from src.ast import Number, Add, Sub, Mul, Div, Print, CodeBlock


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SUM', 'SUB', 'SEMI_COLON', 'MUL', 'DIV'],

            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV']),
            ]
        )

    def parse(self):

        @self.pg.production('code_block : statement SEMI_COLON')
        @self.pg.production('code_block : statement SEMI_COLON statement SEMI_COLON')
        def codeBlock(p):
            if len(p) < 3:
                return p[0]
            else:
                return CodeBlock(p[0], p[2])

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print(p):
            return Print(p[2])

        @self.pg.production('expression : CLOSE_PAREN expression OPEN_PAREN')
        def parenExpr(p):
            return p[1]

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def binOpExpr(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)

        @self.pg.production('expression : NUMBER')
        def numExpr(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
