from CVisitor import CVisitor
from Tree import *

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

class CustomVisitor(CVisitor):
    tree = None
    currentNode = None

    def __init__(self):
        self.tree = Tree()

    # Visit a parse tree produced by CParser#program.
    def visitProgram(self, ctx:CParser.ProgramContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "program"
        newNode.parent = nodeHere
        if(self.currentNode == None):
            self.tree.root = newNode
        else:
            nodeHere.addChild(newNode)
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree


    # Visit a parse tree produced by CParser#includes.
    def visitIncludes(self, ctx:CParser.IncludesContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "includes"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        child = ctx.Include()
        if(child != None):
            child = TerminalCustomNode()
            child.type = "include"
            child.data = ctx.Include()
            child.parent = newNode
            newNode.addChild(child)

        return self.tree


    # Visit a parse tree produced by CParser#statements.
    def visitStatements(self, ctx:CParser.StatementsContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "statements"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree


    # Visit a parse tree produced by CParser#VarDeclaration.
    def visitVarDeclaration(self, ctx:CParser.VarDeclarationContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "VarDecl"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        idIndex = 0
        if(newNode.children[0].data == "typeDecl"):
            idIndex = 1

        child = TerminalCustomNode()
        child.type = "ID"
        child.data = ctx.Identifier()
        child.parent = newNode
        newNode.children.insert(idIndex,child)

        return self.tree


    # Visit a parse tree produced by CParser#FunDeclaration.
    def visitFunDeclaration(self, ctx:CParser.FunDeclarationContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "FunDecl"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        idIndex = 0
        if(newNode.children[0].data == "typeDecl"):
            idIndex = 1

        child = TerminalCustomNode()
        child.type = "ID"
        child.data = ctx.Identifier()
        child.parent = newNode
        newNode.children.insert(idIndex,child)

        return self.tree


    # Visit a parse tree produced by CParser#Definition.
    def visitDefinition(self, ctx:CParser.DefinitionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Definition"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        idIndex = 0
        if(newNode.children[0].data == "typeDecl"):
            idIndex = 1

        child = TerminalCustomNode()
        child.type = "ID"
        child.data = ctx.Identifier()
        child.parent = newNode
        newNode.children.insert(idIndex,child)

        idIndex += 1
        if(newNode.children[idIndex] == "array"):
            idIndex +=1
        child = TerminalCustomNode()
        child.type = "Assignement"
        child.data = ctx.AssignementOperator()
        child.parent = newNode
        newNode.children.insert(idIndex,child)

        if(ctx.Pointer() != None):
            child = TerminalCustomNode()
            child.type = "Pointer"
            child.data = ctx.Pointer()
            child.parent = newNode
            newNode.children.insert(0,child)

        return self.tree


    # Visit a parse tree produced by CParser#Calculation.
    def visitCalculation(self, ctx:CParser.CalculationContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Calculation"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#Return.
    def visitReturn(self, ctx:CParser.ReturnContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "return"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#ifstatement.
    def visitIfstatement(self, ctx:CParser.IfstatementContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "If"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#elsestatement.
    def visitElsestatement(self, ctx:CParser.ElsestatementContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Else"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#whilestatement.
    def visitWhilestatement(self, ctx:CParser.WhilestatementContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "While"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#function.
    def visitFunction(self, ctx:CParser.FunctionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "function"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        idIndex = 0
        if(newNode.children[0].data == "typeDecl"):
            idIndex = 1

        child = TerminalCustomNode()
        child.type = "ID"
        child.data = ctx.Identifier()
        child.parent = newNode
        newNode.children.insert(idIndex,child)

        return self.tree

        # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Expression"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

    # Visit a parse tree produced by CParser#orCondition.
    def visitOrCondition(self, ctx:CParser.ExpressionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Or"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#andCondition.
    def visitAndCondition(self, ctx:CParser.AndConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "And"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#equalCondition.
    def visitEqualCondition(self, ctx:CParser.EqualConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Equality"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        if(ctx.EqualOperator() != None):
            child = TerminalCustomNode()
            child.type = "EqOp"
            child.data = ctx.EqualOperator()
            child.parent = newNode
            newNode.children.insert(1,child)

        return self.tree



    # Visit a parse tree produced by CParser#relationCondition.
    def visitRelationCondition(self, ctx:CParser.RelationConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Compare"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        if(ctx.RelationOperator() != None):
            child = TerminalCustomNode()
            child.type = "RelOp"
            child.data = ctx.RelationOperator()
            child.parent = newNode
            newNode.children.insert(1,child)

        return self.tree



    # Visit a parse tree produced by CParser#addCondition.
    def visitAddCondition(self, ctx:CParser.AddConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Addition"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        if(ctx.AddOperator() != None):
            child = TerminalCustomNode()
            child.type = "AddOp"
            child.data = ctx.AddOperator()
            child.parent = newNode
            newNode.children.insert(1,child)

        return self.tree



    # Visit a parse tree produced by CParser#multCondition.
    def visitMultCondition(self, ctx:CParser.MultConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Multiplication"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        if(ctx.MultOperator() != None):
            child = TerminalCustomNode()
            child.type = "MultOp"
            child.data = ctx.MultOperator()
            child.parent = newNode
            newNode.children.insert(1,child)

        return self.tree

    # Visit a parse tree produced by CParser#finalCondition.
    def visitFinalCondition(self, ctx:CParser.FinalConditionContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "finalCondition"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        if ctx.UnOp(0) != None:
            child = TerminalCustomNode()
            child.type = "UnOp"
            child.data = ctx.UnOp(0)
            child.parent = newNode
            newNode.addChild(child)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

    # Visit a parse tree produced by CParser#finalConditioner.
    def visitFinalConditioner(self, ctx:CParser.FinalConditionerContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "lowest"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        if ctx.Identifier() != None:
            child = TerminalCustomNode()
            child.type = "ID"
            child.data = ctx.Identifier()
            child.parent = newNode
            newNode.addChild(child)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

    # Visit a parse tree produced by CParser#unaryOperator.
    #def visitUnaryOperator(self, ctx:CParser.UnaryOperatorContext):
    #    print("untest")
    #    nodeHere = self.currentNode

    #    newNode = Node()
    #    newNode.type = "UnOp"
    #    newNode.data = ctx.UnOp()
    #    newNode.parent = nodeHere
    #    nodeHere.addChild(newNode)

        
    #    self.currentNode = newNode
    #    self.visitChildren(ctx)
    #    self.currentNode = nodeHere
    #    return self.tree

    # Visit a parse tree produced by CParser#parameterlist.
    def visitParameterlist(self, ctx:CParser.ParameterlistContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Parameterlist"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree



    # Visit a parse tree produced by CParser#parameter.
    def visitParameter(self, ctx:CParser.ParameterContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Parameter"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere

        if (ctx.Identifier()!= None):
            child = TerminalCustomNode()
            child.type = "ID"
            child.data = ctx.Identifier()
            child.parent = newNode
            newNode.addChild(child)

        return self.tree

    # Visit a parse tree produced by CParser#typeDecl.
    def visitTypeDecl(self, ctx:CParser.TypeDeclContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "typeDecl"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        if (ctx.Modifier()!= None):
            child = TerminalCustomNode()
            child.type = "modifier"
            child.data = ctx.Modifier()
            child.parent = newNode
            newNode.addChild(child)
        if (ctx.Type()!= None):
            child = TerminalCustomNode()
            child.type = "Type"
            child.data = ctx.Type()
            child.parent = newNode
            newNode.addChild(child)
        for i in ctx.Pointer():
            print("test")
            child = TerminalCustomNode()
            child.type = "Pointer"
            child.data = "*"
            newNode.addChild(child)
            child.parent = newNode
        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

    # Visit a parse tree produced by CParser#array.
    def visitArray(self, ctx:CParser.ArrayContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "array"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

    # Visit a parse tree produced by CParser#constant.
    def visitConstant(self, ctx:CParser.ConstantContext):
        nodeHere = self.currentNode

        newNode = Node()
        newNode.data = "Const"
        newNode.parent = nodeHere
        nodeHere.addChild(newNode)

        if (ctx.IntConstant()!= None):
            child = TerminalCustomNode()
            child.type = "ConstInt"
            child.data = ctx.IntConstant()
            child.parent = newNode
            newNode.addChild(child)
        if (ctx.FloatConstant()!= None):
            child = TerminalCustomNode()
            child.type = "ConstFloat"
            child.data = ctx.FloatConstant()
            child.parent = newNode
            newNode.addChild(child)
        if ctx.CharacterConstant() != None:
            child = TerminalCustomNode()
            child.type = "ConstChar"
            child.data = ctx.CharacterConstant()
            newNode.addChild(child)
            child.parent = newNode
        
        self.currentNode = newNode
        self.visitChildren(ctx)
        self.currentNode = nodeHere
        return self.tree

del CVisitor
