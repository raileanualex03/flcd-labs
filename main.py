class FiniteAutomaton:
    def __init__(self, fileName):
        self.states = list()
        self.alphabet = list()
        self.transitions = dict()
        self.initialState = None
        self.finalStates = list()
        self.neighbours = dict(list())
        self.readFromFile(fileName)

    def readFromFile(self, fileName):
        file = open(fileName, "r")
        lines = file.readlines()

        self.states = lines[0].strip().split(',')

        for state in self.states:
            self.neighbours[state] = []

        self.alphabet = lines[1].strip().split(',')

        self.initialState = lines[2].strip()

        self.finalStates = lines[3].strip().split(',')

        for index in range(4, len(lines)):
            elements = lines[index].strip().split(',')
            first = elements[0]
            second = elements[1]
            values = elements[2:]
            self.neighbours[first].append(second)
            self.transitions[(first, second)] = values

        file.close()

    def checkIfSequenceAccepted(self, sequence, currentState):
        if len(sequence) == 0:
            return currentState in self.finalStates

        for neighbor in self.neighbours[currentState]:
            values = self.transitions[(currentState, neighbor)]
            if sequence[0] in values:
                if self.checkIfSequenceAccepted(sequence[1:], neighbor):
                    return True

        return False

    def checkSequence(self, sequence):
        return self.checkIfSequenceAccepted(sequence, self.initialState)

    def showMenu(self):
        print('Please choose an option: \n'
              '\t1. show states\n'
              '\t2. show alphabet\n'
              '\t3. show transitions\n'
              '\t4. show initial state\n'
              '\t5. show final states\n'
              '\t6. check if sequence is accepted\n'
              '\tx. quit\n')

    def showState(self):
        print('The states are: ' + str(self.states))

    def showAlphabet(self):
        print('The alphabet is: ' + str(self.alphabet))

    def showTransitions(self):
        print('The transitions are: ' + str(self.transitions))

    def showInitialState(self):
        print('The initial state is: ' + str(self.initialState))

    def showFinalStates(self):
        print('The final states are: ' + str(self.finalStates))

    def showAcceptance(self):
    	sequence = input('The sequence to be checked: ')
    	isAccepted = self.checkSequence(sequence)
    	action = ' is ' if isAccepted else ' is not '
    	result = 'The sequence ' + sequence + action + 'accepted by the current FA\n'
    	print(result)

    def menu(self):
    	options = {
    		'1': self.showState,
    		'2': self.showAlphabet,
    		'3': self.showTransitions,
    		'4': self.showInitialState,
    		'5': self.showFinalStates,
    		'6': self.showAcceptance
    	}
    	while True:
            self.showMenu()
            option = input('Your choice is: ')
            if option == 'x':
                print('Thanks for using this!')
                return
            try:
            	options[option]()
            except KeyError as e:
            	print('ERROR: Please add a valid choice!')


if __name__ == '__main__':
    fa = FiniteAutomaton('fa.in')
    fa.menu()

