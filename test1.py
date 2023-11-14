import re

class MiniJavaLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.keywords = {
            'class', 'public', 'static', 'void', 'main', 'String', 'extends',
            'return', 'int', 'boolean', 'if', 'else', 'while', 'System.out.println',
            'true', 'false', 'this', 'new'
        }

    def tokenize(self):
        # Combine all the regular expressions into a single pattern
        patterns = '|'.join(['(' + pattern + ')' for pattern in [
            Whitespace, Comment, StringLiteral,
            KeywordClass, KeywordPublic, KeywordStatic, KeywordVoid, KeywordMain,
            KeywordString, KeywordExtends, KeywordReturn, KeywordInt, KeywordBoolean,
            KeywordIf, KeywordElse, KeywordWhile, KeywordSystemOut, KeywordTrue,
            KeywordFalse, KeywordThis, KeywordNew,
            Identifier, IntegerLiteral,
            Plus, Minus, Mult, LessThan, And, Not, Equal, Assign, Semicolon, Comma,
            Dot, LeftParenthesis, RightParenthesis, LeftBrace, RightBrace,
            LeftSquareBracket, RightSquareBracket
        ]])

        # Iterate through the source code and match tokens
        for match in re.finditer(patterns, self.source_code):
            for name, value in match.groupdict().items():
                if value is not None:
                    token_type = 'TOKEN_' + name.upper()
                    if token_type.startswith('TOKEN_KEYWORD') and value not in self.keywords:
                        token_type = 'TOKEN_IDENTIFIER'
                    self.tokens.append((token_type, value))
                    break

    def print_tokens(self):
        for token_type, value in self.tokens:
            print(f'{token_type}: {value}')

# Define regular expressions
KeywordClass = r'class'
KeywordPublic = r'public'
KeywordStatic = r'static'
KeywordVoid = r'void'
KeywordMain = r'main'
KeywordString = r'String'
KeywordExtends = r'extends'
KeywordReturn = r'return'
KeywordInt = r'int'
KeywordBoolean = r'boolean'
KeywordIf = r'if'
KeywordElse = r'else'
KeywordWhile = r'while'
KeywordSystemOut = r'System\.out\.println'
KeywordTrue = r'true'
KeywordFalse = r'false'
KeywordThis = r'this'
KeywordNew = r'new'

Identifier = r'[a-zA-Z][a-zA-Z0-9_]*'
IntegerLiteral = r'[0-9]+'

Plus = r'\+'
Minus = r'-'
Mult = r'\*'
LessThan = r'<'
And = r'&&'
Not = r'!'
Equal = r'=='
Assign = r'='
Semicolon = r';'
Comma = r','
Dot = r'\.'
LeftParenthesis = r'\('
RightParenthesis = r'\)'
LeftBrace = r'{'
RightBrace = r'}'
LeftSquareBracket = r'\['
RightSquareBracket = r'\]'

StringLiteral = r'"[^"]*"'

Whitespace = r'[ \t\r\n]+'
Comment = r'//[^\n]*'

# Example source code
source_code =
class Main {
    public static void main(String[] args) {
        int x = 5;
        int y = x + 3;
        System.out.println("Sum is: " + y);
    }
}


# Create a lexer and tokenize the source code
lexer = MiniJavaLexer(source_code)
lexer.tokenize()

# Print the generated tokens
lexer.print_tokens()
