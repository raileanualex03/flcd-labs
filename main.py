import string
from collections import deque


class SymbolTable():

    def __init__(self, bucketsNumber):
        self.bucketsNumber = bucketsNumber
        self.buckets = []
        for i in range(bucketsNumber) :
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
    			return (i, hashValue)

    	return (-1, -1)

    def add(self, element):
    	if (search(element) == (-1, -1)):
    		return (-1, -1)
    	hashValue = self.getHashValue(element)
    	self.buckets[hashValue].append(element)

    	return (len(self.buckets[hashValue]), element)

