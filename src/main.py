from mylang.compiler import Compiler

text_input = """
print(32);

print(32+3);
"""
Compiler(text_input).eval()
