grammar C;

compilationUnit
    : (assignment | declarationList | definitionList)* EOF
    ;

block
    : LC RC
    ;

assignment: typeSpecifier? identifier '=' expression ';';

expression
    : constant
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

statementList
    :
    ;

declarationList
	: declaration
	| declarationList declaration
	;

declaration
    : functionDeclaration SEMICOLON
    ;
functionDeclaration
    : typeSpecifier? functionName functionArgs
    ;

definitionList
    : functionDefinition
    ;
functionDefinition: functionDeclaration block;


functionName: identifier;
functionArgs: LP RP;

identifier: IDENTIFIER;

INTEGER: '0' | [1-9][0-9]*;

typeSpecifier: VOID | INT;
stringLiteral: '"' ~('"')* '"';


VOID: 'void';
INT: 'int';
STAR: '*';
LP: '(';
RP: ')';
LC: '{';
RC: '}';
LSQRB: '[';
RSQRB: ']';
SEMICOLON: ';';
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
