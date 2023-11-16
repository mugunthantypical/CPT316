import re
from tabulate import tabulate

# Define regular expressions for MiniJava tokens
token_patterns = [
    (r'\bclass\b', 'token_CLASS'),
    (r'\bpublic\b', 'token_PUBLIC'),
    (r'\bstatic\b', 'token_STATIC'),
    (r'\bvoid\b', 'token_VOID'),
    (r'\bmain\b', 'token_MAIN'),
    (r'\bString\b', 'token_STRING'),
    (r'\bextends\b', 'token_EXTENDS'),
    (r'\breturn\b', 'token_RETURN'),
    (r'\bint\b', 'token_INT'),
    (r'\bboolean\b', 'token_BOOLEAN'),
    (r'\bif\b', 'token_IF'),
    (r'\belse\b', 'token_ELSE'),
    (r'\bwhile\b', 'token_WHILE'),
    (r'\bSystem\.out\.println\b', 'token_SYSTEM_OUT'),
    (r'\btrue\b', 'token_TRUE'),
    (r'\bfalse\b', 'token_FALSE'),
    (r'\bthis\b', 'token_THIS'),
    (r'\bnew\b', 'token_NEW'),
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'token_id'),
    (r'[0-9]+', 'token_int'),
    (r'\+', 'token_plusOp'),
    (r'-', 'token_minusOp'),
    (r'\*', 'token_multyOp'),
    (r'<', 'token_LESS_THAN'),
    (r'&&', 'token_andOp'),
    (r'!', 'token_notOP'),
    (r'==', 'token_equalOp'),
    (r'=', 'token_assignOp'),
    (r';', 'token_SEMICOLON'),
    (r',', 'token_COMMA'),
    (r'\.', 'token_DOT'),
    (r'\(', 'token_LEFT_PAREN'),
    (r'\)', 'token_RIGHT_PAREN'),
    (r'{', 'token_LEFT_BRACE'),
    (r'}', 'token_RIGHT_BRACE'),
    (r'\[', 'token_LEFT_SQUARE_BRACKET'),
    (r'\]', 'token_RIGHT_SQUARE_BRACKET'),
    (r'"[^"]*"', 'token_STRING_LITERAL'),
    (r'[ \t\r\n]+', 'whitespace'),
    (r'//[^\n]*', 'comment')
]

# Combine all regular expressions into one
regexAll = '|'.join([f'(?P<{token_type}>{pattern})' for pattern, token_type in token_patterns])

# Tokenize the input and print as a table with token and token type
def tokenize(input):
    tokens = []
    matches = re.finditer(regexAll, input)
    for match in matches:
        for token_type in [token_type for _, token_type in token_patterns]:
            if match.group(token_type):
                tokens.append([match.group().strip(), token_type])
                break

    if tokens:
        headers = ['Token', 'Token Type']
        print(tabulate(tokens, headers, tablefmt="grid"))

if __name__ == "__main__":
    code = "public class MyClass { int x = 42; }"
    tokenize(code)