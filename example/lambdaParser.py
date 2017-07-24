# Generated from lambda.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\b")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\5\2\36\n\2\3\2\3\2\7\2\"\n\2\f\2\16\2%\13\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\2\3\2\7\2\4\6\b\n\2\2-\2")
        buf.write("\35\3\2\2\2\4&\3\2\2\2\6(\3\2\2\2\b*\3\2\2\2\n,\3\2\2")
        buf.write("\2\f\r\b\2\1\2\r\36\5\4\3\2\16\17\7\5\2\2\17\20\5\4\3")
        buf.write("\2\20\21\5\6\4\2\21\22\5\2\2\6\22\36\3\2\2\2\23\24\5\b")
        buf.write("\5\2\24\25\5\2\2\2\25\26\5\n\6\2\26\27\5\2\2\4\27\36\3")
        buf.write("\2\2\2\30\31\5\b\5\2\31\32\5\2\2\2\32\33\5\2\2\2\33\34")
        buf.write("\5\n\6\2\34\36\3\2\2\2\35\f\3\2\2\2\35\16\3\2\2\2\35\23")
        buf.write("\3\2\2\2\35\30\3\2\2\2\36#\3\2\2\2\37 \f\5\2\2 \"\5\2")
        buf.write("\2\6!\37\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3\2")
        buf.write("\2\2%#\3\2\2\2&\'\7\3\2\2\'\5\3\2\2\2()\7\4\2\2)\7\3\2")
        buf.write("\2\2*+\7\6\2\2+\t\3\2\2\2,-\7\7\2\2-\13\3\2\2\2\4\35#")
        return buf.getvalue()


class lambdaParser ( Parser ):

    grammarFileName = "lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'.'", "'lambda'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "VAR", "POINT", "LAMBDA", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "WS" ]

    RULE_t = 0
    RULE_var = 1
    RULE_pt = 2
    RULE_lb = 3
    RULE_rb = 4

    ruleNames =  [ "t", "var", "pt", "lb", "rb" ]

    EOF = Token.EOF
    VAR=1
    POINT=2
    LAMBDA=3
    LEFT_BRACKET=4
    RIGHT_BRACKET=5
    WS=6

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_t

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LAMBDAFUNCTIONContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lambdaParser.LAMBDA, 0)
        def var(self):
            return self.getTypedRuleContext(lambdaParser.VarContext,0)

        def pt(self):
            return self.getTypedRuleContext(lambdaParser.PtContext,0)

        def t(self):
            return self.getTypedRuleContext(lambdaParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLAMBDAFUNCTION" ):
                listener.enterLAMBDAFUNCTION(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLAMBDAFUNCTION" ):
                listener.exitLAMBDAFUNCTION(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLAMBDAFUNCTION" ):
                return visitor.visitLAMBDAFUNCTION(self)
            else:
                return visitor.visitChildren(self)


    class TOVARContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(lambdaParser.VarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTOVAR" ):
                listener.enterTOVAR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTOVAR" ):
                listener.exitTOVAR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTOVAR" ):
                return visitor.visitTOVAR(self)
            else:
                return visitor.visitChildren(self)


    class DOUBLETERMContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDOUBLETERM" ):
                listener.enterDOUBLETERM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDOUBLETERM" ):
                listener.exitDOUBLETERM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDOUBLETERM" ):
                return visitor.visitDOUBLETERM(self)
            else:
                return visitor.visitChildren(self)


    class BRACKETLEFTContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lb(self):
            return self.getTypedRuleContext(lambdaParser.LbContext,0)

        def t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TContext,i)

        def rb(self):
            return self.getTypedRuleContext(lambdaParser.RbContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBRACKETLEFT" ):
                listener.enterBRACKETLEFT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBRACKETLEFT" ):
                listener.exitBRACKETLEFT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBRACKETLEFT" ):
                return visitor.visitBRACKETLEFT(self)
            else:
                return visitor.visitChildren(self)


    class FULLBBRACKETContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lb(self):
            return self.getTypedRuleContext(lambdaParser.LbContext,0)

        def t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TContext,i)

        def rb(self):
            return self.getTypedRuleContext(lambdaParser.RbContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFULLBBRACKET" ):
                listener.enterFULLBBRACKET(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFULLBBRACKET" ):
                listener.exitFULLBBRACKET(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFULLBBRACKET" ):
                return visitor.visitFULLBBRACKET(self)
            else:
                return visitor.visitChildren(self)



    def t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lambdaParser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = lambdaParser.TOVARContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.var()
                pass

            elif la_ == 2:
                localctx = lambdaParser.LAMBDAFUNCTIONContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(lambdaParser.LAMBDA)
                self.state = 13
                self.var()
                self.state = 14
                self.pt()
                self.state = 15
                self.t(4)
                pass

            elif la_ == 3:
                localctx = lambdaParser.BRACKETLEFTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.lb()
                self.state = 18
                self.t(0)
                self.state = 19
                self.rb()
                self.state = 20
                self.t(2)
                pass

            elif la_ == 4:
                localctx = lambdaParser.FULLBBRACKETContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.lb()
                self.state = 23
                self.t(0)
                self.state = 24
                self.t(0)
                self.state = 25
                self.rb()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lambdaParser.DOUBLETERMContext(self, lambdaParser.TContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                    self.state = 29
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 30
                    self.t(4) 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(lambdaParser.VAR, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = lambdaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(lambdaParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINT(self):
            return self.getToken(lambdaParser.POINT, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_pt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPt" ):
                listener.enterPt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPt" ):
                listener.exitPt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPt" ):
                return visitor.visitPt(self)
            else:
                return visitor.visitChildren(self)




    def pt(self):

        localctx = lambdaParser.PtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(lambdaParser.POINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LbContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(lambdaParser.LEFT_BRACKET, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_lb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLb" ):
                listener.enterLb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLb" ):
                listener.exitLb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLb" ):
                return visitor.visitLb(self)
            else:
                return visitor.visitChildren(self)




    def lb(self):

        localctx = lambdaParser.LbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(lambdaParser.LEFT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RbContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RIGHT_BRACKET(self):
            return self.getToken(lambdaParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_rb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRb" ):
                listener.enterRb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRb" ):
                listener.exitRb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRb" ):
                return visitor.visitRb(self)
            else:
                return visitor.visitChildren(self)




    def rb(self):

        localctx = lambdaParser.RbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(lambdaParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def t_sempred(self, localctx:TContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




