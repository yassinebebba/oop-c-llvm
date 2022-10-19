grammar C;

compilationUnit
    : (
        assignment
        | functionCall
        | declarationList
        | definitionList
      )* EOF
    ;

functionBlock
    : LC (
        expression
      | definitionList
      | declarationList
      | functionCall
      | assignment
      | functionReturn
     )* RC
    ;

assignment
    : typeSpecifier identifier ASSIGN expression SEMI
    ;

expression
    : constant
    | functionCallExpression
    | identifier
    | expression STAR expression
    | expression DIV expression
    | expression PLUS expression
    | expression MINUS expression
    ;

// this block might be used for compiler optimisation
multiplyExpression: '*';
divideExpression: '/';
addExpression: '+';
subtractExpression: '-';
// this block might be used for compiler optimisation

constant
    : INTEGER_CONSTANT
    | FLOAT_CONSTANT
    | CHAR_CONSTANT
    | STRING_LITERAL+
    ;
// expressions does not end with ';'? (question mark) what do you think?
functionCallExpression: identifier LP functionCallArgs? RP;

// NOTE: this regex (expression COMMA?)* is not good enough to detect wrong
// syntax like this func(1 + 2 D)
functionCall: identifier LP functionCallArgs? RP SEMI;
// this parser rule fixed the note above :)
functionCallArgs
    : expression COMMA?
    | functionCallArgs COMMA functionCallArgs
    ;

statementList
    :
    ;

declarationList
	: declaration
	| declarationList declaration
	;

declaration
    : functionDeclaration
    | variableDeclaration SEMI
    ;

variableDeclaration: typeSpecifier identifier;
functionDeclaration
    : typeSpecifier? functionName LP functionArgs? RP SEMI
    ;

definitionList
    : functionDefinition
    ;
functionDefinition
    : typeSpecifier? functionName LP functionArgs? RP functionBlock
    ;

functionReturn
    : RETURN expression? SEMI
    ;

functionName: identifier;

// will probably have to split functionArgs into
// functionDeclarationArgs and functionDefinitionArgs
// because omitting the parameter name in a function definition is a c2x extension
// NOTE: this regex (typeSpecifier identifier? COMMA?)* is not good enough to
// detect wrong syntax like this func(int a long b)
// functionArgs: LP (typeSpecifier identifier? COMMA?)* RP;
// this next parser rule fixes the above note make sure you use it if
// you encounter the same problem
functionArgs
    : typeSpecifier identifier? COMMA?
    | functionArgs COMMA functionArgs
    ;


typeSpecifier
    : CONST? (
          VOID
        | (SIGNED | UNSIGNED)?
            (
                  CHAR
                | SHORT
                | SHORT? INT
                | LONG
                | FLOAT
                | LONG? DOUBLE
                | INT
            )
        | identifier
      ) STAR*
    ;

identifier: IDENTIFIER;

STRING_LITERAL: '"' ~('"')* '"';
CHAR_CONSTANT: '\'' ~('\'')* '\'';
INTEGER_CONSTANT: '0' | [1-9][0-9]*;
FLOAT_CONSTANT
    : [0-9]+ DOT [0-9]* EXPONENT?
    | DOT [0-9]+ EXPONENT?
    | [0-9]+ EXPONENT
    ;
EXPONENT: [eE] [+-]? [0-9]+;

// https://learn.microsoft.com/en-us/cpp/c-language/c-type-specifiers?view=msvc-170

RETURN: 'return';

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
