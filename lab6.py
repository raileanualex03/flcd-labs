from enum import Enum
from main import Grammar

class Operations:
	def __init__(self, descendentConfiguration, grammar):
		self.descendentConfiguration = descendentConfiguration
		self.grammar = grammar

	def expand(self):
		nonTerminal = descendentConfiguration.inputStack.pop()
		toBeExpanded = grammar.productions[nonTerminal][0]
		for i in range(len(toBeExpanded)-1, 0, -1):
			nextElement = toBeExpanded[i]
			descendentConfiguration.inputStack.push(nextElement)

		descendentConfiguration.workingStack.push((nonTerminal, 0))

	def advance(self):
		nonTerminal = descendentConfiguration.inputStack.pop()
		self.descendentConfiguration.workingStack.push(nonTerminal)
		self.descendentConfiguration.inputIndex += 1

	def momentaryInsuccess(self):
		self.descendentConfiguration.stateParser = StateParser.BACK_STATE

	def goBack(self):
		lastTerminal = descendentConfiguration.workingStack.pop()
		self.descendentConfiguration.inputIndex -= 1
		self.descendentConfiguration.inputStack.push(lastTerminal)

	def success(self):
		self.descendentConfiguration.stateParser = StateParser.FINAL_STATE

	def anotherTry(self):
		pass

class OperationsChecker:
	def __init__(self, descendentConfiguration):
		self.descendentConfiguration = descendentConfiguration

	def isAdvanceAvailable(self, sequences):
		nonTerminal = sequences[self.descendentConfiguration.inputIndex]

		if (len(self.descendentConfiguration.inputStack) == 0):
			return False
		return nonTerminal == self.descendentConfiguration.inputStack[-1]

	def isExpandAvailable(self, grammar):
		if (len(self.descendentConfiguration.inputStack) == 0):
			return False
		nonTerminal = self.descendentConfiguration.inputStack[-1]

		return nonTerminal in grammar.non_terminal_symbols 

	def isGoingBackAvailable(self):
		if (len(self.descendentConfiguration.inputStack) == 0):
			return False
		lastElement = self.descendentConfiguration.workingStack[-1]

		return type(lastElement) == str

	def isSuccessAvailable(self, inputSequence):
		return len(self.descendentConfiguration.inputStack) == 0 and self.descendentConfiguration.inputIndex == len(inputSequence)


class StateParser(Enum):
    NORMAL_STATE = 'normal_state'
    BACK_STATE = 'back_state'
    FINAL_STATE = 'final_state'
    ERROR_STATE = 'error_state'
    NONE = 'none'

class DescendentConfiguration:
	def __init__(self):
		self.stateParser = StateParser.NONE
		self.inputIndex = -1
		self.productionIndex = -1
		self.workingStack = list()
		self.inputStack = list()


class DescendentRecursiveParser:
	def __init__(self, inputSequence, grammarModel):
		self.descendentConfiguration = DescendentConfiguration()
		self.descendentConfiguration.stateParser = StateParser.NORMAL_STATE
		self.descendentConfiguration.inputIndex = 0
		self.descendentConfiguration.workingStack = []
		self.descendentConfiguration.inputStack = []
		self.inputSequence = inputSequence
		self.grammar = grammarModel

	def runParser(self):
		operationsChecker = OperationsChecker(self.descendentConfiguration)
		operations = Operations(self.descendentConfiguration, self.grammar)
		parsingState = self.descendentConfiguration.stateParser
		while (parsingState != StateParser.ERROR_STATE and parsingState != StateParser.FINAL_STATE):
			if parsingState == StateParser.NORMAL_STATE:
				if (operationsChecker.isSuccessAvailable(self.inputSequence)):
					operations.success()
				else:
					if (operationsChecker.isExpandAvailable(self.grammar)):
						operations.expand()
					else:
						if (operationsChecker.isAdvanceAvailable(self.inputSequence)):
							operations.advance()
						else:
							operations.momentaryInsuccess()
			if (parsingState == StateParser.BACK_STATE):
				if (operationsChecker.isGoingBackAvailable()):
					operations.goBack()
				else:
					#TODO: add another try
					operations.anotherTry()

			parsingState = self.descendentConfiguration.stateParser

		if (parsingState == StateParser.ERROR_STATE):
			print("Can not be parsed!")

def test_advance():
	print('\n\nStarting tests for advance...')
	inputSequence = ['a', 'a', 'b', 'c', 'd']
	descendentConfiguration = DescendentConfiguration()
	descendentConfiguration.inputIndex = 0
	descendentConfiguration.inputStack.append('a')
	operationsChecker = OperationsChecker(descendentConfiguration)
	assert(operationsChecker.isAdvanceAvailable(inputSequence) == True)
	print('The tests for advance passed!')

def test_expand():
	print('\n\nStarting tests for expand...')
	grammar = Grammar()
	grammar.non_terminal_symbols = ["S", "B"]
	descendentConfiguration = DescendentConfiguration()
	descendentConfiguration.inputStack.append("S")

	operationsChecker = OperationsChecker(descendentConfiguration)
	assert(operationsChecker.isExpandAvailable(grammar) == True)
	print('The tests for expand passed!')


def test_can_go_back():
	print('\n\nStarting tests for going back...')
	descendentConfiguration = DescendentConfiguration()
	descendentConfiguration.workingStack.append("S")
	descendentConfiguration.workingStack.append(("S", 1))
	
	operationsChecker = OperationsChecker(descendentConfiguration)
	assert(operationsChecker.isGoingBackAvailable() == False)

	descendentConfiguration.workingStack.pop()

	print('The tests for going back passed!')

def test_parser():
	grammar = Grammar()
	grammar.read_from_file("g1.txt")
	inputSequence = ['a', 'a', 'c', 'b', 'c']
	descendentRecursiveParser = DescendentRecursiveParser(inputSequence, grammar)
	descendentRecursiveParser.runParser()


test_advance()
test_expand()
test_can_go_back()
test_parser()