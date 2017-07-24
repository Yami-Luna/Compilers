import sys
from antlr4 import *
from Tree import *
from CLexer import CLexer
from CParser import CParser
from CustomVisitor import *

def main(argv):
	Myinput = FileStream(argv[1])
	lexer = CLexer(Myinput)
	stream = CommonTokenStream(lexer)
	parser = CParser(stream)
	antlrtree = parser.program()
	visitor = CustomVisitor()

	t = visitor.visit(tree = antlrtree)

	t.toDot("test.dot")

	t.minimize()

	t.toDot("test3.dot")

if __name__ == '__main__':
	main(sys.argv)
