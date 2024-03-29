grammar C;

compilationUnit
    : (
          assignment
        | includeDirective
        | functionCall
        | declarationList
        | definitionList
        | classDefinition
      )* EOF
    ;

expression
    : constant                                #constantExpression
    | unarySign? functionCallExpression       #funcCallExpression
    | unarySign? identifier                   #identifierExpression
    | SIZEOF (expression | LP (expression| CHAR) RP)  #sizeofExpression
    | expression STAR expression              #multiplyExpression
    | expression DIV expression               #divideExpression
    | expression PLUS expression              #addExpression
    | expression MINUS expression             #subtractExpression
    | expression EQ expression                #eqExpression
    | expression LT expression                #ltExpression
    | expression LTE expression               #lteExpression
    | expression GT expression                #gtExpression
    | expression GTE expression               #gteExpression
    | expression LEFT_SHIFT expression        #leftShiftExpression
    | unarySign? chainedCall                  #chainedCallExpression
    ;
chainedCall: identifier ((DOT | ARROW) (identifier | functionCallExpression))*;

constant
    : unarySign? INTEGER_CONSTANT
    | unarySign? FLOAT_CONSTANT
    | unarySign? CHAR_CONSTANT
    | (unarySign STAR)? STRING_LITERAL+
    ;

// unaryPlus and unaryMinus are for eg:
// +-+-+-+-5 or -+-+-identifier or +-+-+-+-foo()
unaryPlus
    : PLUS MINUS?
    | unaryPlus unaryPlus
    ;

unaryMinus
    : MINUS PLUS?
    | unaryMinus unaryMinus
    ;
unarySign
    : unaryPlus
    | unaryMinus
    ;

// expressions does not end with ';'? (question mark) what do you think?
functionCallExpression: identifier LP functionCallArgs? RP;

// NOTE: this regex (expression COMMA?)* is not good enough to detect wrong
// syntax like this func(1 + 2 D)
functionCall: identifier LP functionCallArgs? RP SEMI;
// this parser rule fixed the note above :)
functionCallArgs
    : expression (COMMA expression)*
    ;

statementList
    : expression SEMI
    | ifStatementStructure
    | whileStatement
    | doWhileStatement
    | functionCall
    | assignment
    | inplaceAssignment
    | variableDefinition
    | functionReturn
    ;

declarationList
	: functionDeclaration
	| variableDeclaration
	| structDeclaration
	;

definitionList
    : functionDefinition
    | variableDefinition
    | structDefinition
    ;

variableDeclaration: typeSpecifier identifier arrayCell* SEMI;

variableDefinition: typeSpecifier identifier ASSIGN expression SEMI;

arrayCell: LSQRB (INTEGER_CONSTANT | identifier)? RSQRB;

functionDeclaration
    : typeSpecifier identifier LP functionArgs? RP SEMI
    ;

functionDefinition
    : typeSpecifier identifier LP functionArgs? RP block
    ;

functionReturn
    : RETURN expression? SEMI
    ;

// will probably have to split functionArgs into
// functionDeclarationArgs and functionDefinitionArgs
// because omitting the parameter name in a function definition is a c2x extension
// NOTE: this regex (typeSpecifier identifier? COMMA?)* is not good enough to
// detect wrong syntax like this func(int a long b)
// functionArgs: LP (typeSpecifier identifier? COMMA?)* RP;
// this next parser rule fixes the above note make sure you use it if
// you encounter the same problem
functionArgs
    : arg (COMMA arg)* (COMMA ELLIPSIS)?
    ;

arg: typeSpecifier identifier?;

structDeclaration: STRUCT identifier SEMI;

structDefinition: STRUCT identifier structBlock SEMI;

structBlock
    : LC (
        field
      | bitField
     )* RC
   ;

field: typeSpecifier identifier SEMI;
bitField: typeSpecifier identifier COLON INTEGER_CONSTANT SEMI;

assignment
    : (identifier | chainedCall) ASSIGN expression SEMI
    ;

inplaceAssignment
    : (identifier | chainedCall)
        (
              STAR_ASSIGN
            | DIV_ASSIGN
            | MOD_ASSIGN
            | PLUS_ASSIGN
            | MINUS_ASSIGN
            | LEFT_SHIFT_ASSIGN
            | RIGHT_SHIFT_ASSIGN
            | BITWISE_AND_ASSIGN
            | BITWISE_XOR_ASSIGN
            | BITWISE_OR_ASSIGN
        )
      expression SEMI
    ;

typeSpecifier
    : CONST? (
          VOID
        | (SIGNED | UNSIGNED)?
            (
                  CHAR
                | SHORT
                | (SHORT | LONG LONG?)? INT
                | LONG LONG?
                | FLOAT
                | LONG? DOUBLE
            )
        | identifier
      ) STAR*
    ;


ifStatementStructure
    : ifStatement elseIfStatement* elseStatement?
    ;
ifStatement: IF LP expression RP block;
elseIfStatement: ELSE ifStatement;
elseStatement: ELSE block;

whileStatement
    : WHILE LP expression RP block
    ;

doWhileStatement
    : DO block WHILE LP expression RP SEMI
    ;

// START OOP SECTION
classDefinition
    : CLASS identifier classBlock
    ;

classAttributeDefinition: typeSpecifier identifier ASSIGN expression SEMI;
classAttributeDeclaration: typeSpecifier identifier arrayCell* SEMI;

classBlock
    : LC (
        classAttributeDefinition
      | classAttributeDeclaration
      | classConstructor
      | classMethod
     )* RC
   ;

classConstructor: identifier LP functionArgs? RP block;

classMethod: typeSpecifier identifier LP functionArgs? RP block;

classInstantiation: typeSpecifier identifier ASSIGN NEW identifier LP functionCallArgs? RP SEMI;
// END OOP SECTION

block
    : LC (
        statementList
      | definitionList
      | declarationList
      | classInstantiation
     )* RC
   ;

identifier: IDENTIFIER;

// must be handled separately by the pre processor
includeDirective: INCLUDE_DIRECTIVE;
INCLUDE_DIRECTIVE
    :   '#' WS? 'include' WS? (('"' ~[\r\n]* '"') | ('<' ~[\r\n]* '>' )) WS? NEWLINE
     //   -> channel(HIDDEN)
    ;

STRING_LITERAL
    : '"' (ESC|.)*? '"' ('"' (ESC|.)*? '"')* ;

fragment ESC
    : '\\' (["\\/bfnrt] | UNICODE) ;

fragment UNICODE
    : 'u' HEX HEX HEX HEX ;

fragment HEX
    : [0-9a-fA-F] ;
CHAR_CONSTANT: '\'' (~('\'') | '\'')* '\'';
INTEGER_CONSTANT: '0' | [1-9][0-9]*;
FLOAT_CONSTANT
    : [0-9]+ DOT [0-9]* EXPONENT?
    | DOT [0-9]+ EXPONENT?
    | [0-9]+ EXPONENT
    ;
EXPONENT: [eE] [+-]? [0-9]+;

// https://learn.microsoft.com/en-us/cpp/c-language/c-type-specifiers?view=msvc-170

CLASS: 'class';
NEW: 'new';

AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
DO: 'do';
ELSE: 'else';
ENUM: 'enum';
EXTERN : 'extern';
FOR: 'for';
GOTO: 'goto';
IF: 'if';
INLINE: 'inline';
REGISTER: 'register';
RESTRICT: 'restrict';
RETURN: 'return';
SIZEOF: 'sizeof'; // sizeof is an operator
STATIC : 'static';
STRUCT : 'struct';
SWITCH : 'switch';
TYPEDEF: 'typedef';
UNION: 'union';
VOLATILE: 'volatile';
WHILE: 'while';

CONST: 'const';
SIGNED: 'signed';
UNSIGNED: 'unsigned';
VOID: 'void';
CHAR: 'char';
SHORT: 'short';
INT: 'int';
LONG: 'long';
FLOAT: 'float';
DOUBLE: 'double';

PLUS: '+';
PLUS_PLUS: '++';
MINUS: '-';
MINUS_MINUS: '--';
STAR: '*';
DIV: '/';
MOD: '%';

LP: '(';
RP: ')';
LC: '{';
RC: '}';
LSQRB: '[';
RSQRB: ']';

LT : '<';
LTE : '<=';
GT : '>';
GTE : '>=';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';

AND : '&';
OR : '|';
AND_AND : '&&';
OR_OR : '||';
CARET : '^';
NOT : '!';
TILDE : '~';

QUESTION: '?';
COLON: ':';
SEMI: ';';
COMMA: ',';


ASSIGN : '=';
// inplace assignment
// '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
STAR_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
PLUS_ASSIGN : '+=';
MINUS_ASSIGN : '-=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
BITWISE_AND_ASSIGN : '&=';
BITWISE_XOR_ASSIGN : '^=';
BITWISE_OR_ASSIGN : '|=';

EQ : '==';
NEQ : '!=';

ARROW : '->';
DOT : '.';
ELLIPSIS : '...';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;

NEWLINE
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BLOCK_COMMENT
    :   '/*' .*? '*/'
        -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]*
        -> skip
    ;
ANY: .;