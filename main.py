import string
from collections import deque


class SymbolTable():

    def __init__(self):
        self.bucketsNumber = 37
        self.buckets = []
        for i in range(self.bucketsNumber) :
            self.buckets.append(deque())

    def getHashValue(self, element):
        sum = 0
        for character in element:
            sum = sum + ord(character)
        return sum % self.bucketsNumber

    def search(self, element):
    	hashValue = self.getHashValue(element)
    	for i in range(len(self.buckets[hashValue])):
    		if self.buckets[hashValue][i] == element:
    			return (hashValue, i)

    	return (-1, -1)

    def add(self, element):
    	if (self.search(element) != (-1, -1)):
    		return self.search(element)
    	hashValue = self.getHashValue(element)
    	self.buckets[hashValue].append(element)

    	return (hashValue, len(self.buckets[hashValue]) - 1)


def main():
	st = SymbolTable()
	print(st.add('alex'))
	assert st.search('alex') == (19, 0)

	print(st.add('alex'))
	assert st.search('alex') == (19, 0)

	print(st.add('test'))
	assert st.search('alex') == (19, 0)

main()
