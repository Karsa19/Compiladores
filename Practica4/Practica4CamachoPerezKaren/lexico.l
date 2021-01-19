/* ANALIZADOR LEXICO C CAMACHO PEREZ KF */


D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include <stdio.h>

%}

%%
"/*"			{ printf("<Comentario>"); }

"auto"			{ printf("<Palabra Reservada>"); }
"break"			{ printf("<Palabra Reservada>"); }
"case"			{ printf("<Palabra Reservada>"); }
"char"			{ printf("<Palabra Reservada>"); }
"const"			{ printf("<Palabra Reservada>"); }
"continue"		{ printf("<Palabra Reservada>"); }
"default"		{ printf("<Palabra Reservada>"); }
"do"			{ printf("<Palabra Reservada>"); }
"double"		{ printf("<Palabra Reservada>"); }
"else"			{ printf("<Palabra Reservada>"); }
"enum"			{ printf("<Palabra Reservada>"); }
"extern"		{ printf("<Palabra Reservada>"); }
"float"			{ printf("<Palabra Reservada>"); }
"for"			{ printf("<Palabra Reservada>"); }
"goto"			{ printf("<Palabra Reservada>"); }
"if"			{ printf("<Palabra Reservada>"); }
"int"			{ printf("<Palabra Reservada>"); }
"long"			{ printf("<Palabra Reservada>"); }
"register"		{ printf("<Palabra Reservada>"); }
"return"		{ printf("<Palabra Reservada>"); }
"short"			{ printf("<Palabra Reservada>"); }
"signed"		{ printf("<Palabra Reservada>"); }
"sizeof"		{ printf("<Palabra Reservada>"); }
"static"		{ printf("<Palabra Reservada>"); }
"struct"		{ printf("<Palabra Reservada>"); }
"switch"		{ printf("<Palabra Reservada>"); }
"typedef"		{ printf("<Palabra Reservada>"); }
"union"			{ printf("<Palabra Reservada>"); }
"unsigned"		{ printf("<Palabra Reservada>"); }
"void"			{ printf("<Palabra Reservada>"); }
"volatile"		{ printf("<Palabra Reservada>"); }
"while"			{ printf("<Palabra Reservada>"); }

{L}({L}|{D})*		{ printf("<Identificador>"); }

0[xX]{H}+{IS}?		{ printf("<Constante Entera>"); }
0{D}+{IS}?		{ printf("<Constante Entera Octal>"); }
{D}+{IS}?		{ printf("<Constante Entera Decimal>"); }
L?'(\\.|[^\\'])+'	{ printf("<Constante Cadena>"); }

{D}+{E}{FS}?		{ printf("<Constante Flotante>"); }
{D}*"."{D}+({E})?{FS}?	{ printf("<Constante Flotante>"); }
{D}+"."{D}*({E})?{FS}?	{ printf("<Constante Flotante>"); }

L?\"(\\.|[^\\"])*\"	{ printf("<Literal>"); }

"..."			{ printf("<Elipsis>"); }
">>="			{ printf("<Operador>"); }
"<<="			{ printf("<Operador>"); }
"+="			{ printf("<Operador>"); }
"-="			{ printf("<Operador>"); }
"*="			{ printf("<Operador>"); }
"/="			{ printf("<Operador>"); }
"%="			{ printf("<Operador>"); }
"&="			{ printf("<Operador>"); }
"^="			{ printf("<Operador>"); }
"|="			{ printf("<Operador>"); }
">>"			{ printf("<Operador>"); }
"<<"			{ printf("<Operador>"); }
"++"			{ printf("<Operador>"); }
"--"			{ printf("<Operador>"); }
"->"			{ printf("<Operador>"); }
"&&"			{ printf("<Operador>"); }
"||"			{ printf("<Operador>"); }
"<="			{ printf("<Operador>"); }
">="			{ printf("<Operador>"); }
"=="			{ printf("<Operador>"); }
"!="			{ printf("<Operador>"); }
";"			{ printf("<Final Sentencia>"); }
("{"|"<%")		{ printf("<Delimitador>"); }
("}"|"%>")		{ printf("<Delimitador>"); }
","			{ printf("<Delimitador>"); }
":"			{printf("<Delimitador>"); }
"="			{ printf("<Delimitador>"); }
"("			{ printf("<Delimitador>"); }
")"			{ printf("<Delimitador>"); }
("["|"<:")		{ printf("<Delimitador>"); }
("]"|":>")		{ printf("<Delimitador>"); }
"."			{ printf("<Operador>"); }
"&"			{ printf("<Operador>"); }
"!"			{ printf("<Operador>"); }
"~"			{ printf("<Operador>"); }
"-"			{ printf("<Operador>"); }
"+"			{ printf("<Operador>"); }
"*"			{ printf("<Operador>"); }
"/"			{ printf("<Operador>"); }
"%"			{ printf("<Operador>"); }
"<"			{ printf("<Operador>"); }
">"			{ printf("<Operador>"); }
"^"			{ printf("<Operador>"); }
"|"			{ printf("<Operador>"); }
"?"			{ printf("<Operador>"); }

[ \t\v\n\f]		{ printf("<Literal>"); }
.			{ /* ignore bad characters */ }

%%


