grammar C;

compilationUnit
    : (
          assignment
        | variableInitialization
        | variableDeclaration
        | functionCall
        | declarationList
        | definitionList
      )* EOF
    ;

expression
    : constant                                #constantExpression
    | functionCallExpression                  #funcCallExpression
    | identifier                              #identiferExpression
    | SIZEOF (expression | LP expression RP)  #sizeofExpression
    | expression STAR expression              #multiplyExpression
    | expression DIV expression               #divideExpression
    | expression PLUS expression              #addExpression
    | expression MINUS expression             #subtractExpression
    ;

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

variableInitialization: typeSpecifier identifier ASSIGN expression SEMI;

functionDeclaration
    : typeSpecifier? functionName LP functionArgs? RP SEMI
    ;

definitionList
    : functionDefinition
    ;
functionDefinition
    : typeSpecifier? functionName LP functionArgs? RP block
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

assignment
    : identifier ASSIGN expression SEMI
    ;

inplaceAssignment
    : identifier
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
                | SHORT? INT
                | LONG
                | FLOAT
                | LONG? DOUBLE
                | INT
            )
        | identifier
      ) STAR*
    ;


ifStatementStructure
    : ifStatement elseIfStatement* elseStatement?
    ;
ifStatement: IF LP condition+ RP block;
elseIfStatement: ELSE ifStatement;
elseStatement: ELSE block;

condition
    : expression COMMA?
    | expression COMMA expression
    ;

// I think block and functionBlock are the same?!!!
block
    : LC (
        expression
      | ifStatementStructure
      | variableInitialization
      | variableDeclaration
      | definitionList
      | declarationList
      | functionCall
      | assignment
      | inplaceAssignment
      | functionReturn
     )* RC
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
