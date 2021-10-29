from tokens import *
import re


class Scanner:
    @staticmethod
    def isOperator(token):
        return token in OPERATORS

    @staticmethod
    def isIdentifier(token):
        # a sequence of letters and digits, such that the first character is a letter
        return re.match(r"^[a-zA-Z]([a-zA-Z]|[0-9])*$", token) is not None

    @staticmethod
    def isConstant(token):
        # Integer or string between ""
        return re.match('^(0|[+-]?[1-9][0-9]*)$', token) is not None or re.match('^\".*\"$', token) is not None

    @staticmethod
    def getWholeOperator(line, index):
        # in case of an operator with multiple characters
        token = ''
        while index < len(line) and Scanner.isOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def getString(line, index):
        token = ''
        quotes = 0
        # Get the string from the first quote to the second quote
        while index < len(line) and quotes < 2:
            if line[index] == '"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def getTokensFromLine(line):
        token = ''
        index = 0
        while index < len(line):
            if line[index] == '"':
                if token:
                    yield token
                token, index = Scanner.getString(line, index)
                yield token
                token = ''  # Reset token after we've found a string
            elif Scanner.isOperator(line[index]):
                if token:
                    yield token
                # Check for <=, >= etc (composed operators)
                token, index = Scanner.getWholeOperator(line, index)
                yield token
                token = ''  # Reset token
            elif line[index] in SEPARATORS:
                if token:
                    yield token
                token, index = line[index], index + 1
                yield token
                token = ''  # Reset token
            else:
                token += line[index]  # Add a new character to the token
                index += 1  # Increase line index
        if token:
            yield token