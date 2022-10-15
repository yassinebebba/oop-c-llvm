grammar C;

compilationUnit
    : (declarationList | definitionList)* EOF
    ;

block
    : LC RC
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
    : 'void' functionName functionArgs
 //   | functionName functionArgs
    ;

definitionList
    : functionDefinition
    ;
functionDefinition: functionDeclaration block;


functionName: IDENTIFIER;
functionArgs: LP RP;

typeSpecifier
    : VOID
    | INT
    ;

// FunctionDeclarationArgs: WS? '(' WS? ')' WS?;
// FunctionDefinitionScope: WS? '{' WS? '}' WS?;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;




STRING_LITERAL: '"' ~('"')* '"';

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
