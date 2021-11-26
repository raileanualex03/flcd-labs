class Operations:
	def __init__(self, descendentConfiguration, grammar):
		self.descendentConfiguration = descendentConfiguration
		self.grammar = grammar

	def expand(self):
		nonTerminal = descendentConfiguration.inputStack.pop()
		toBeExpanded = grammar.productions[nonTerminal][0]
		for(i=len(toBeExpanded)-1; i>=0; i--):
			nextElement = toBeExpanded[i]
			descendentConfiguration.inputStack.push(nextElement)

		descendentConfiguration.workingStack.push((nonTerminal, 0))

	def advance(self):
		nonTerminal = descendentConfiguration.inputStack.pop()
		descendentConfiguration.workingStack.push(nonTerminal)
		descendentConfiguration.inputIndex += 1

	def momentaryInsuccess(self):
		descendentConfiguration.stateParser = StateParser.BACK_STATE

	def goBack(self):
		String lastTerminal = descendentConfiguration.workingStack.pop()
		descendentConfiguration.inputIndex -= 1
		descendentConfiguration.inputStack.push(lastTerminal)

class OperationsChecker:
	def __init__(self, descendentConfiguration):
		self.descendentConfiguration = descendentConfiguration

	def isAdvanceAvailable(self, sequences):
		nonTerminal = sequences[self.descendentConfiguration.inputIndex]

		return nonTerminal == self.descendentConfiguration.inputStack[-1]

	def isExpandAvailable(self, grammar):
		nonTerminal = self.descendentConfiguration.inputStack[-1]

		return nonTerminal in grammar.non_terminal_symbols 

	def isGoingBackAvailable(self):
		lastElement = self.descendentConfiguration.workingStack[-1]

		return type(lastElement) == str
