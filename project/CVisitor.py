# Generated from C.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#program.
    def visitProgram(self, ctx:CParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#includes.
    def visitIncludes(self, ctx:CParser.IncludesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statements.
    def visitStatements(self, ctx:CParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#VarDeclaration.
    def visitVarDeclaration(self, ctx:CParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunDeclaration.
    def visitFunDeclaration(self, ctx:CParser.FunDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Definition.
    def visitDefinition(self, ctx:CParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Calculation.
    def visitCalculation(self, ctx:CParser.CalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Return.
    def visitReturn(self, ctx:CParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ifstatement.
    def visitIfstatement(self, ctx:CParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#elsestatement.
    def visitElsestatement(self, ctx:CParser.ElsestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#whilestatement.
    def visitWhilestatement(self, ctx:CParser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function.
    def visitFunction(self, ctx:CParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#orCondition.
    def visitOrCondition(self, ctx:CParser.OrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#andCondition.
    def visitAndCondition(self, ctx:CParser.AndConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#equalCondition.
    def visitEqualCondition(self, ctx:CParser.EqualConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#relationCondition.
    def visitRelationCondition(self, ctx:CParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#addCondition.
    def visitAddCondition(self, ctx:CParser.AddConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#multCondition.
    def visitMultCondition(self, ctx:CParser.MultConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#finalCondition.
    def visitFinalCondition(self, ctx:CParser.FinalConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#finalConditioner.
    def visitFinalConditioner(self, ctx:CParser.FinalConditionerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#parameterlist.
    def visitParameterlist(self, ctx:CParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#parameter.
    def visitParameter(self, ctx:CParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#typeDecl.
    def visitTypeDecl(self, ctx:CParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#array.
    def visitArray(self, ctx:CParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#constant.
    def visitConstant(self, ctx:CParser.ConstantContext):
        return self.visitChildren(ctx)



del CParser