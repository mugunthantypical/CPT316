import re

class MiniJavaLexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        # Combine all the regular expressions into a single pattern
        patterns = '|'.join(['(?P<' + pattern + '>' + regex + ')' for pattern, regex in [
            ('whitespace', whitespace), ('comment', comment),
            ('stringLiteral', stringLiteral),
            ('tagClass', tagClass), ('tagPublic', tagPublic), ('tagStatic', tagStatic),
            ('tagVoid', tagVoid), ('tagMain', tagMain), ('tagString', tagString),
            ('tagExtends', tagExtends), ('tagReturn', tagReturn), ('tagInt', tagInt),
            ('tagBoolean', tagBoolean), ('tagIf', tagIf), ('tagElse', tagElse),
            ('tagWhile', tagWhile), ('tagSystemOut', tagSystemOut), ('tagTrue', tagTrue),
            ('tagFalse', tagFalse), ('tagThis', tagThis), ('tagNew', tagNew),
            ('id', id), ('intLiteral', intLiteral),
            ('plusOp', plusOp), ('minusOp', minusOp), ('multyOp', multyOp),
            ('lessThanOp', lessThanOp), ('andOp', andOp), ('notOP', notOP),
            ('equalOp', equalOp), ('assignOp', assignOp), ('semicolonOp', semicolonOp),
            ('commaOp', commaOp), ('dotOp', dotOp),
            ('leftparentthesisOp', leftparentthesisOp), ('rightparentthesisOp', rightparentthesisOp),
            ('leftbraceOp', leftbraceOp), ('rightbraceOp', rightbraceOp),
            ('leftsqbracketOp', leftsqbracketOp), ('rightsqbracketOp', rightsqbracketOp)
        ]])

        # Iterate through the source code and match tokens
        for match in re.finditer(patterns, self.source_code):
            for name, value in match.groupdict().items():
                if value is not None:
                    token_type = 'token_' + name
                    self.tokens.append((token_type, value))
                    break

    def print_tokens(self):
        for token_type, value in self.tokens:
            print(f'{token_type}: {value}')

# Define regular expressions
tagClass      = r'class'
tagPublic     = r'public'
tagStatic     = r'static'
tagVoid       = r'void'
tagMain       = r'main'
tagString     = r'String'
tagExtends    = r'extends'
tagReturn     = r'return'
tagInt        = r'int'
tagBoolean    = r'boolean'
tagIf         = r'if'
tagElse       = r'else'
tagWhile      = r'while'
tagSystemOut  = r'System\.out\.println'
tagTrue       = r'true'
tagFalse      = r'false'
tagThis       = r'this'
tagNew        = r'new'

id        = r'[a-zA-Z][a-zA-Z0-9_]*'
intLiteral    = r'[0-9]+'

plusOp              = r'\+'
minusOp             = r'-'
multyOp             = r'\*'
lessThanOp          = r'<'
andOp               = r'&&'
notOP               = r'!'
equalOp             = r'=='
assignOp            = r'='
semicolonOp         = r';'
commaOp             = r','
dotOp               = r'\.'
leftparentthesisOp  = r'\('
rightparentthesisOp = r'\)'
leftbraceOp         = r'{'
rightbraceOp        = r'}'
leftsqbracketOp     = r'\['
rightsqbracketOp    = r'\]'

stringLiteral     = r'"[^"]*"'

whitespace        = r'[ \t\r\n]+'
comment           = r'//[^\n]*'

# Example source code
source_code = """
class Main {
    public static void main(String[] args) {
        System.out.println("Hello, MiniJava!");
    }
}
"""

# Create a lexer and tokenize the source code
lexer = MiniJavaLexer(source_code)
lexer.tokenize()

# Print the generated tokens
lexer.print_tokens()