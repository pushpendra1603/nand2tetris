import re

    

command_dict = {'add': 'C_ARITHMETIC', 'sub': 'C_ARITHMETIC', 'neg': 'C_ARITHMETIC', 'eq': 'C_ARITHMETIC',
                'gt': 'C_ARITHMETIC', 'lt': 'C_ARITHMETIC', 'and': 'C_ARITHMETIC', 'or': 'C_ARITHMETIC',
                'not': 'C_ARITHMETIC', 'push': 'C_PUSH', 'pop': 'C_POP', 'label': 'C_LABEL', 'goto': 'C_GOTO',
                'if-goto': 'C_IF', 'function': 'C_FUNCTION', 'return': 'C_RETURN', 'call': 'C_CALL'}


class Parser:
    

    def __init__(self, input_file):
        self.currline = 0
        self.command = ""
        self.input = self.__process(input_file)


    @staticmethod
    def __process(input_file):
        input_file = open(input_file)
        res = []
        for line in input_file:
            line = line.strip()
            line =  re.sub(r"(//.*)|(\n)", "", line).strip()
            if line != "":
                line = line.split(" ")
                res.append(line)
        return res

    
    def hasMoreCommands(self):
        return self.currline < len(self.input)
    

    def advance(self):
        if self.hasMoreCommands():
            self.command = self.input[self.currline]
            self.currline += 1

    
    def commandType(self):
        return command_dict[self.command[0]]


    def arg1(self):
        if self.commandType == "C_ARITHEMETIC":
            return self.command[0]
        elif len(self.command) > 1:
            return self.command[1]
        else:
            return None

    
    def arg2(self):
        if len(self.command) > 2:
            return self.command[2]
        else:
            return None