# Generated from lambda.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lambdaParser import lambdaParser
else:
    from lambdaParser import lambdaParser

# This class defines a complete generic visitor for a parse tree produced by lambdaParser.

class lambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lambdaParser#LAMBDAFUNCTION.
    def visitLAMBDAFUNCTION(self, ctx:lambdaParser.LAMBDAFUNCTIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#TOVAR.
    def visitTOVAR(self, ctx:lambdaParser.TOVARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#DOUBLETERM.
    def visitDOUBLETERM(self, ctx:lambdaParser.DOUBLETERMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#BRACKETLEFT.
    def visitBRACKETLEFT(self, ctx:lambdaParser.BRACKETLEFTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#FULLBBRACKET.
    def visitFULLBBRACKET(self, ctx:lambdaParser.FULLBBRACKETContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#var.
    def visitVar(self, ctx:lambdaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#pt.
    def visitPt(self, ctx:lambdaParser.PtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#lb.
    def visitLb(self, ctx:lambdaParser.LbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#rb.
    def visitRb(self, ctx:lambdaParser.RbContext):
        return self.visitChildren(ctx)



del lambdaParser