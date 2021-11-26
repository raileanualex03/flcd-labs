class Grammar:
    def __init__(self, file_name):
        self.non_terminal_symbols = list()
        self.terminal_symbols = list()
        self.productions = dict(list())
        self.start_symbol = None
        self.read_from_file(file_name)

    def read_from_file(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()

        self.non_terminal_symbols = lines[0].strip().split(',')
        self.terminal_symbols = lines[1].strip().split(',')
        self.start_symbol = lines[2]

        for index in range(3, len(lines)):
            elements = lines[index].strip().split('->')
            non_terminal_symbol = elements[0].strip()
            productions_for_symbol = elements[1].split('|')
            self.productions[non_terminal_symbol] = productions_for_symbol

    def check_if_cfg(self):
        # we will go through all the productions and check if the terminal node is on the left side
        for symbol in self.productions:
            productions = self.productions[symbol]
            for production in productions:
                if len(production) >= 1:
                    if production[0] in self.terminal_symbols and production[1] in self.terminal_symbols:
                        return False
        return True

class Menu:
    def __init__(self, grammar):
        self.grammar = grammar

    def print_menu(self):
        print('Please choose an option: \n'
              '\t1. show non terminals\n'
              '\t2. show terminals\n'
              '\t3. show starting symbol\n'
              '\t4. show all productions\n'
              '\t5. show productions for symbol \n'
              '\t6. check if grammar is context free\n'
              '\tx. quit\n')

    def show_non_terminals(self):
        print('The non terminals: ' + str(self.grammar.non_terminal_symbols))

    def show_terminals(self):
        print('The terminals: ' + str(self.grammar.terminal_symbols))

    def show_starting_symbol(self):
        print('The starting symbol: ' + str(self.grammar.start_symbol))

    def show_productions(self):
        toPrint = ""
        print(self.grammar.productions)
        for symbol in self.grammar.productions:
            productions_for_symbol = self.grammar.productions[symbol]
            toPrint += symbol + " -> "
            for production in productions_for_symbol:
                toPrint += production + " | "
            toPrint += "\n\t"
        print('The productions: \n\t' + toPrint)
    
    def show_product_for_symbol(self):
        symbol = input('The given symbol is: ')
        toPrint = ""
        productions_for_symbol = self.grammar.productions[symbol]
        for production in productions_for_symbol:
            toPrint += symbol + " -> " + production + "\n\t"
        print('The productions for symbol ' + symbol + ' : \n\t' + toPrint)    

    def show_cfg(self):
        result = self.grammar.check_if_cfg()
        isCFG = "is" if result else "is not"
        print('The given grammar ' + isCFG + ' a cfg')

    def start(self):
        options = {
            1: self.show_non_terminals,
            2: self.show_terminals,
            3: self.show_starting_symbol,
            4: self.show_productions,
            5: self.show_product_for_symbol,
            6: self.show_cfg
        }

        print('Welcome to Lab5!\n')
        while True:
            self.print_menu()
            option = input('Your choice is: ')

            if option == 'x':
                print('Thanks for using this!')
                quit()
            try:
                options[int(option)]()
            except KeyError as e:
                print("Please provide valid key! " + str(e) + " not found!" )            


if __name__ == '__main__':
    grammar = Grammar('g1.txt')
    menu = Menu(grammar)
    menu.start()
