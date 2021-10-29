from symbolTable import SymbolTable
from pif  import ProgramInternalForm
from scanner import Scanner
from tokens import *

if __name__ == '__main__':
    #file = open('firstExercise', 'r')
    file = open('secondExercise', 'r')
    st = SymbolTable()
    pif = ProgramInternalForm()

    line_index = 0
    for line in file:
        line_index += 1

        if line[-1] == '\n':
            line = line[0:-1]

        for token in Scanner.getTokensFromLine(line):
            if token == ' ':
                continue
            if token in OPERATORS_SEPARATORS_WORDS:
                pif.add(token, -1)
            elif Scanner.isIdentifier(token):
                pif.add('identifier', st.add(token))
            elif Scanner.isConstant(token):
                pif.add('constant', st.add(token))
            else:
                raise ValueError(f"Unknown token '{token}' at line {line_index}!")

    print("PIF{\n")
    for element in pif.get_data():
        print(f"{element[0]} ---- {element[1]}\n")
    print("}\n")

    print("Symbol table: ")
    for element in st.buckets:
        if (len(element) != 0):
            print(f"({element})")

