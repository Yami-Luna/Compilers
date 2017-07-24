
import sys
from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
from lambdaListener import lambdaListener


class MyGrammarListener(lambdaListener):
	def enterLAMBDAFUNCTION(self, ctx):
		print("lambda")
	def enterVar(self, ctx):
		print(ctx.getChild(0))
		print (", ")


	def visitLAMBDAFUNCTION(self, ctx:lambdaParser.LAMBDAFUNCTIONContext):
		print ("lambda") 
		self.visitChild(1)
		print('.')
		self.visitChild(3)


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
		print (self.visitChild(0));
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


def main(argv):
	Myinput = FileStream(argv[1])
	lexer = lambdaLexer(Myinput)
	stream = CommonTokenStream(lexer)
	parser = lambdaParser(stream)
	tree = parser.t()
	printer = MyGrammarListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)

if __name__ == '__main__':
	main(sys.argv)

