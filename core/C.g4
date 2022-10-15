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
    | functionCallAssignment
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

functionCallAssignment: identifier LP (expression COMMA?)* RP;
functionCall: identifier LP (expression COMMA?)* RP SEMICOLON;

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
    : typeSpecifier? functionName functionArgs SEMICOLON
    ;

definitionList
    : functionDefinition
    ;
functionDefinition
    : typeSpecifier? functionName functionArgs functionBlock
    ;


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
