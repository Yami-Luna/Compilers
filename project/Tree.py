class Node:
	data = None
	parent = None
	children = []
	def __init__(self):
		self.data = None
		self.parent = None
		self.children = []

	def toDot(self,freeNumber,file):
		ownNumber = freeNumber
		freeNumber += 1
		for child in self.children:
			if(type(child) == TerminalCustomNode):
				file.write(str(freeNumber)+"[label = \""+ str(child.type)+'\n'+str(child.data)+ "\"];")
			else:
				file.write(str(freeNumber)+"[label = \""+str(child.data) + "\"];")
			file.write(str(ownNumber) + "--" + str(freeNumber) + ";")
			freeNumber = child.toDot(freeNumber,file)
		return freeNumber

	def addChild(self,child):
		self.children.append(child)

	def reattach(self):
		self.children[0].parent = self.parent
		for i in range(len(self.parent.children)):
			if self.parent.children[i] == self:
				self.parent.children[i] = self.children[0]
				break

	def minimize(self):
		if self.data == "statements":
			if self.parent.data == "statements":
				for i in range(len(self.parent.children)):
					if self.parent.children[i] == self:
						self.parent.children.pop(i)
						break
				for i in self.children:
					i.parent = self.parent
					self.parent.addChild(i)

		elif self.data == "ParameterList":
			if self.parent.data == "Parameterlist":
				for i in range(len(self.parent.children)):
					if self.parent.children[i] == self:
						self.parent.children.pop(i)
						break
				for i in self.children:
					i.parent = self.parent
					self.parent.addChild(i)

		elif self.data == "includes":
			if self.parent.data == "includes":
				for i in range(len(self.parent.children)):
					if self.parent.children[i] == self:
						self.parent.children.pop(i)
						break
				for i in self.children:
					i.parent = self.parent
					self.parent.addChild(i)

		elif self.data == "Expression":
			if self.children[0].data != "Or":
				self.data = "new"
			else:
				self.reattach()

		elif self.data == "Or":
			if len(self.children) == 1:
				self.reattach()
			else:
				self.data = "or"

		elif self.data == "And":
			if len(self.children) == 1:
				self.reattach()
			else:
				self.data = "and"

		elif self.data == "Equality" or self.data == "Compare" or self.data == "Addition" or self.data =="Multiplication" :
			if len(self.children) == 1:
				self.reattach()
			else:
				self.data = self.children[1].data
				self.children.pop(1)

		elif self.data == "Const" or self.data == "lowest":
			self.reattach()

		elif self.data == "typeDecl" or self.data == "finalCondition":
			if (len(self.children) == 1):
				self.reattach()

		elif self.data == "Definition":
			self.data = self.children[len(self.children)-2].data
			self.children.pop(len(self.children)-2)

		elif self.data == "Parameterlist":
			if len(self.children) == 0:
				for i in range(len(self.parent.children)):
					if self.parent.children[i] == self:
						self.parent.children.pop(i)
						break				

		#else:
			#print(self.data)

		for i in self.children:
			i.minimize()


class TerminalCustomNode(Node):
	type = None
	def __init__(self):
		self.data = None
		self.type = None
		self.parent = None
		self.children = []


class Tree:
	root = None
	def __init__(self):
		root = None

	def toDot(self,filename):
		f = open(filename,'w')
		f.write("graph{")
		f.write("0 [label = \""+str(self.root.data) + "\"];")
		self.root.toDot(0,f)
		f.write("}")

	def minimize(self):
		self.root.minimize()

