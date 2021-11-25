



class VMWriter:


    def __init__(self, output_file):
        self.output = open(output_file, 'w')
        self.classname = ""


    def writePush(self, segment, index):
        self.printOut(f'push {segment} {index}')


    def writepop(self, segment, index):
        self.printOut(f'pop {segment} {index}')


    def writeArithemetic(self, command):
        self.printOut(f'{command}')


    def writeLabel(self, label):
        pass


    def writeGoto(self, label):
        pass


    def writeIf(self, label):
        pass


    def writeCall(self, name, nargs):
        self.printOut(f'call {name} {nargs}')


    def writeFunction(self, name, nLocals):
        self.printOut(f'function {self.classname}.{name} {nLocals}')


    def writeReturn(self):
        self.printOut(f'return')


    def printOut(self, code):
        # self.output.write(f'{code}\n')
        print(f'{code}')
    
    def className(self, name):
        self.classname = name

    def close(self):
        self.output.close()