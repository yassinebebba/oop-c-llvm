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
     )* RC
    ;

assignment
    : typeSpecifier identifier '=' expression ';'
    ;

expression
    : constant
    | functionCallExpression
    | identifier
    | expression multiplyOp expression
    | expression divideOp expression
    | expression addOp expression
    | expression subtractOp expression
    ;


multiplyOp: '*';
divideOp: '/';
addOp: '+';
subtractOp: '-';

constant
    : INTEGER
    | stringLiteral
    ;
// expressions does not end with ';'? (question mark) what do you think?
functionCallExpression: identifier LP functionCallArgs? RP;

// NOTE: this regex (expression COMMA?)* is not good enough to detect wrong
// syntax like this func(1 + 2 D)
functionCall: identifier LP functionCallArgs? RP SEMICOLON;
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
    | variableDeclaration SEMICOLON
    ;

variableDeclaration: typeSpecifier identifier;
functionDeclaration
    : typeSpecifier? functionName LP functionArgs? RP SEMICOLON
    ;

definitionList
    : functionDefinition
    ;
functionDefinition
    : typeSpecifier? functionName LP functionArgs? RP functionBlock
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
    : (
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

stringLiteral: '"' ~('"')* '"';

// https://learn.microsoft.com/en-us/cpp/c-language/c-type-specifiers?view=msvc-170
INTEGER: '0' | [1-9][0-9]*;
SIGNED: 'signed';
UNSIGNED: 'unsigned';
VOID: 'void';
CHAR: 'char';
SHORT: 'short';
INT: 'int';
LONG: 'long';
FLOAT: 'float';
DOUBLE: 'double';
STAR: '*';
LP: '(';
RP: ')';
LC: '{';
RC: '}';
LSQRB: '[';
RSQRB: ']';
SEMICOLON: ';';
COMMA: ',';
IDENTIFIER: [a-zA-Z_][a-zA-Z_]*;

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
