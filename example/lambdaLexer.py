# Generated from lambda.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\b")
        buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\6\7 \n\7\r\7\16\7!\3\7\3\7\2\2\b\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\3\2\4\3\2c|\5\2\13\f\17\17\"\"%\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3\2\2\2")
        buf.write("\t\32\3\2\2\2\13\34\3\2\2\2\r\37\3\2\2\2\17\20\t\2\2\2")
        buf.write("\20\4\3\2\2\2\21\22\7\60\2\2\22\6\3\2\2\2\23\24\7n\2\2")
        buf.write("\24\25\7c\2\2\25\26\7o\2\2\26\27\7d\2\2\27\30\7f\2\2\30")
        buf.write("\31\7c\2\2\31\b\3\2\2\2\32\33\7*\2\2\33\n\3\2\2\2\34\35")
        buf.write("\7+\2\2\35\f\3\2\2\2\36 \t\3\2\2\37\36\3\2\2\2 !\3\2\2")
        buf.write("\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\b\7\2\2$\16\3\2")
        buf.write("\2\2\4\2!\3\b\2\2")
        return buf.getvalue()


class lambdaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    VAR = 1
    POINT = 2
    LAMBDA = 3
    LEFT_BRACKET = 4
    RIGHT_BRACKET = 5
    WS = 6

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'lambda'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "POINT", "LAMBDA", "LEFT_BRACKET", "RIGHT_BRACKET", "WS" ]

    ruleNames = [ "VAR", "POINT", "LAMBDA", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "WS" ]

    grammarFileName = "lambda.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


