class ProgramInternalForm:
    def __init__(self):
        self.content = []

    def add(self, symbolCode, symbolIndex):
        self.content.append((symbolCode, symbolIndex))


    def get_data(self):
        return self.content