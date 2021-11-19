
'''

Recursive descendent

'''




class Grammar:
	def __init__(self, filename):
		self.nonTerminals = []
		self.terminals = []
		self.productions = {}
		self.filename = filename
		self.symbol = ''

	def readGrammarFromFile(self):
		file = open(fileName, "r")
        lines = file.readlines()
        index = 0
        for line in lines:
        	if (line != ''):
        		if (index == 0):
        			values = line.split(' ')
        			nonterminals.extend(values)
        		elif (index == 1):
        			values = line.split(' ')
        			terminals.extend(values)
        		elif (index == 2):
        			values = line.split(' ')
        			self.symbol = values[0]
        		else:
        			self.initializeProductions()

    def initializeProductions(self):
    	pass



