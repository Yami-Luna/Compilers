# Generated from C.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#program.
    def enterProgram(self, ctx:CParser.ProgramContext):
        pass

    # Exit a parse tree produced by CParser#program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass


    # Enter a parse tree produced by CParser#includes.
    def enterIncludes(self, ctx:CParser.IncludesContext):
        pass

    # Exit a parse tree produced by CParser#includes.
    def exitIncludes(self, ctx:CParser.IncludesContext):
        pass


    # Enter a parse tree produced by CParser#statements.
    def enterStatements(self, ctx:CParser.StatementsContext):
        pass

    # Exit a parse tree produced by CParser#statements.
    def exitStatements(self, ctx:CParser.StatementsContext):
        pass


    # Enter a parse tree produced by CParser#VarDeclaration.
    def enterVarDeclaration(self, ctx:CParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#VarDeclaration.
    def exitVarDeclaration(self, ctx:CParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#FunDeclaration.
    def enterFunDeclaration(self, ctx:CParser.FunDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#FunDeclaration.
    def exitFunDeclaration(self, ctx:CParser.FunDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#Definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        pass

    # Exit a parse tree produced by CParser#Definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
        pass


    # Enter a parse tree produced by CParser#Calculation.
    def enterCalculation(self, ctx:CParser.CalculationContext):
        pass

    # Exit a parse tree produced by CParser#Calculation.
    def exitCalculation(self, ctx:CParser.CalculationContext):
        pass


    # Enter a parse tree produced by CParser#Return.
    def enterReturn(self, ctx:CParser.ReturnContext):
        pass

    # Exit a parse tree produced by CParser#Return.
    def exitReturn(self, ctx:CParser.ReturnContext):
        pass


    # Enter a parse tree produced by CParser#ifstatement.
    def enterIfstatement(self, ctx:CParser.IfstatementContext):
        pass

    # Exit a parse tree produced by CParser#ifstatement.
    def exitIfstatement(self, ctx:CParser.IfstatementContext):
        pass


    # Enter a parse tree produced by CParser#elsestatement.
    def enterElsestatement(self, ctx:CParser.ElsestatementContext):
        pass

    # Exit a parse tree produced by CParser#elsestatement.
    def exitElsestatement(self, ctx:CParser.ElsestatementContext):
        pass


    # Enter a parse tree produced by CParser#whilestatement.
    def enterWhilestatement(self, ctx:CParser.WhilestatementContext):
        pass

    # Exit a parse tree produced by CParser#whilestatement.
    def exitWhilestatement(self, ctx:CParser.WhilestatementContext):
        pass


    # Enter a parse tree produced by CParser#function.
    def enterFunction(self, ctx:CParser.FunctionContext):
        pass

    # Exit a parse tree produced by CParser#function.
    def exitFunction(self, ctx:CParser.FunctionContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#orCondition.
    def enterOrCondition(self, ctx:CParser.OrConditionContext):
        pass

    # Exit a parse tree produced by CParser#orCondition.
    def exitOrCondition(self, ctx:CParser.OrConditionContext):
        pass


    # Enter a parse tree produced by CParser#andCondition.
    def enterAndCondition(self, ctx:CParser.AndConditionContext):
        pass

    # Exit a parse tree produced by CParser#andCondition.
    def exitAndCondition(self, ctx:CParser.AndConditionContext):
        pass


    # Enter a parse tree produced by CParser#equalCondition.
    def enterEqualCondition(self, ctx:CParser.EqualConditionContext):
        pass

    # Exit a parse tree produced by CParser#equalCondition.
    def exitEqualCondition(self, ctx:CParser.EqualConditionContext):
        pass


    # Enter a parse tree produced by CParser#relationCondition.
    def enterRelationCondition(self, ctx:CParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by CParser#relationCondition.
    def exitRelationCondition(self, ctx:CParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by CParser#addCondition.
    def enterAddCondition(self, ctx:CParser.AddConditionContext):
        pass

    # Exit a parse tree produced by CParser#addCondition.
    def exitAddCondition(self, ctx:CParser.AddConditionContext):
        pass


    # Enter a parse tree produced by CParser#multCondition.
    def enterMultCondition(self, ctx:CParser.MultConditionContext):
        pass

    # Exit a parse tree produced by CParser#multCondition.
    def exitMultCondition(self, ctx:CParser.MultConditionContext):
        pass


    # Enter a parse tree produced by CParser#finalCondition.
    def enterFinalCondition(self, ctx:CParser.FinalConditionContext):
        pass

    # Exit a parse tree produced by CParser#finalCondition.
    def exitFinalCondition(self, ctx:CParser.FinalConditionContext):
        pass


    # Enter a parse tree produced by CParser#finalConditioner.
    def enterFinalConditioner(self, ctx:CParser.FinalConditionerContext):
        pass

    # Exit a parse tree produced by CParser#finalConditioner.
    def exitFinalConditioner(self, ctx:CParser.FinalConditionerContext):
        pass


    # Enter a parse tree produced by CParser#parameterlist.
    def enterParameterlist(self, ctx:CParser.ParameterlistContext):
        pass

    # Exit a parse tree produced by CParser#parameterlist.
    def exitParameterlist(self, ctx:CParser.ParameterlistContext):
        pass


    # Enter a parse tree produced by CParser#parameter.
    def enterParameter(self, ctx:CParser.ParameterContext):
        pass

    # Exit a parse tree produced by CParser#parameter.
    def exitParameter(self, ctx:CParser.ParameterContext):
        pass


    # Enter a parse tree produced by CParser#typeDecl.
    def enterTypeDecl(self, ctx:CParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by CParser#typeDecl.
    def exitTypeDecl(self, ctx:CParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by CParser#array.
    def enterArray(self, ctx:CParser.ArrayContext):
        pass

    # Exit a parse tree produced by CParser#array.
    def exitArray(self, ctx:CParser.ArrayContext):
        pass


    # Enter a parse tree produced by CParser#constant.
    def enterConstant(self, ctx:CParser.ConstantContext):
        pass

    # Exit a parse tree produced by CParser#constant.
    def exitConstant(self, ctx:CParser.ConstantContext):
        pass


