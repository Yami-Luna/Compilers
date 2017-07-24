grammar lambda;
t  : var 			 #TOVAR
   | LAMBDA var pt t #LAMBDAFUNCTION
   | t  t			 #DOUBLETERM
   | lb t rb  t		 #BRACKETLEFT
   | lb t  t rb 	 #FULLBBRACKET
   ;

var : VAR;
VAR : [a-z];

pt: POINT;
POINT: '.';

LAMBDA: 'lambda';

lb: LEFT_BRACKET;
LEFT_BRACKET: '(';

rb: RIGHT_BRACKET;
RIGHT_BRACKET: ')';

WS : [ \r\t\n]+ -> skip ;
