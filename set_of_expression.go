// Regular expressions for MiniJava token_s

// Keywords
tagClass      ::= "class"
tagPublic     ::= "public"
tagStatic     ::= "static"
tagVoid       ::= "void"
tagMain       ::= "main"
tagString     ::= "String"
tagExtends    ::= "extends"
tagReturn     ::= "return"
tagInt        ::= "int"
tagBoolean    ::= "boolean"
tagIf         ::= "if"
tagElse       ::= "else"
tagWhile      ::= "while"
tagSystemOut  ::= "System.out.println"
tagTrue       ::= "true"
tagFalse      ::= "false"
tagThis       ::= "this"
tagNew        ::= "new"

// Identifiers
id        ::= [a-zA-Z][a-zA-Z0-9_]*

// Integer Literals
intLiteral    ::= [0-9]+

// Operators and Punctuation
plusOp            	::= "+"
minusOp             ::= "-"
multyOp             ::= "*"
lessThanOp          ::= "<"
andOp               ::= "&&"
notOP               ::= "!"
equalOp             ::= "=="
assignOp            ::= "="
semicolonOp         ::= ";"
commaOp             ::= ","
dotOp               ::= "\."
leftparentthesisOp  ::= "\("
rightparentthesisOp ::= "\)"
leftbraceOp         ::= "{"
rightbraceOp        ::= "}"
leftsqbracketOp 		::= "\["
rightsqbracketOp 		::= "\]"

// String Literals
stringLiteral     ::= "\"[^\"]*\""

// whitespace and Ccomments (to be ignored)
whitespace        ::= [ \t\r\n]+
comment           ::= "//[^\n]*"

// Define token types
token_CLASS       ::= tagClass
token_PUBLIC      ::= tagPublic
token_STATIC      ::= tagStatic
token_VOID        ::= tagVoid
token_MAIN        ::= tagMain
token_STRING      ::= tagString
token_EXTENDS     ::= tagExtends
token_RETURN      ::= tagReturn
token_INT         ::= tagInt
token_BOOLEAN     ::= tagBoolean
token_IF          ::= tagIf
token_ELSE        ::= tagElse
token_WHILE       ::= tagWhile
token_SYSTEM_OUT  ::= tagSystemOut
token_TRUE        ::= tagTrue
token_FALSE       ::= tagFalse
token_THIS        ::= tagThis
token_NEW         ::= tagNew
token_id  				 ::= id
token_int     		 ::= intLiteral
token_plusOp      ::= plusOp
token_minusOp     ::= minusOp
token_multyOp     ::= multyOp
token_LESS_THAN   ::= lessThanOp
token_andOp       ::= andOp
token_notOP       ::= notOP
token_equalOp     ::= equalOp
token_assignOp    ::= assignOp
token_SEMICOLON   ::= semicolonOp
token_COMMA       ::= commaOp
token_DOT         ::= dotOp
token_LEFT_PAREN  ::= leftparentthesisOp
token_RIGHT_PAREN ::= RightParenthesis
token_LEFT_BRACE  ::= leftbraceOp
token_RIGHT_BRACE ::= rightbrceOp
token_LEFT_SQUARE_BRACKET  ::= leftsq
token_RIGHT_SQUARE_BRACKET ::= rightsqbracketOp
token_STRING_LITERAL 			 ::= stringLiteral