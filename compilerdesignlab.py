import re

code = "int sum = 10;" \
" a + b = 20;"
tokens = re.findall(r'[a-zA-Z_]+|\d+|[=+;]', code)
keywords = ['int', 'float', 'if', 'else', 'return']

for token in tokens:
    if token in keywords:
        print(token, "-> Keyword")
    elif token.isdigit():
        print(token, "-> Number")
    elif token in ['=', '+']:
        print(token, "-> Operator")
    elif token == ';':
        print(token, "-> Separator")
    else:
        print(token, "-> Identifier")