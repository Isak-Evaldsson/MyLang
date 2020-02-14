from mylang.lexer import Lexer
from mylang.parser import Parser


class Compiler:
    def __init__(self, text):
        self.lexer = Lexer().get_lexer()
        self.tokens = self.lexer.lex(text)
        self.pg = Parser()
        self.pg.parse()
        self.parser = self.pg.get_parser()

    def printTokens(self):
        for token in self.tokens:
            print(token)

    def eval(self):
        self.parser.parse(self.tokens).eval()
