# Aritmetic Classes
class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()                

# Coding logic
class CodeBlock():
    def __init__(self, *blocks):
        self.blocks = blocks
    
    def eval(self):
        for block in self.blocks:
            block.eval()

# Standard functions
class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())  