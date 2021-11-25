from SymbolTable import SymbolTable
from VMWriter import VMWriter
from JackTokenizer import JackTokenizer
import re



ARTH_COMMAND_DICT = {'+': "add", '-': "sub", '*': "call Math.multiply 2", '/': "call Math.divide 2", '&amp;': "AND", '|': "OR", '&lt;': "LT", '&gt;': "GT", '=': "EQ"}
class CompilationEngine:



    def __init__(self, input_file, output_file=None):
        if output_file == None:
            output_file = re.sub(r'(\.jack)', ".vm", input_file)
        self.tokenizer = JackTokenizer(input_file)
        print(output_file)
        # self.outputxml = open(output_file, 'w')
        self.symboltable = SymbolTable()
        self.vmwriter = VMWriter(output_file)
        self.spaces = 0

    
    def compileClass(self):
        if self.tokenizer.hasMoreTokens(): self.tokenizer.advance()
        if self.tokenizer.token() == "class":

            self.tokenizer.advance()
            classname = self.tokenizer.token()
            self.vmwriter.className(classname)
            self.skipTill('{')
            self.compileClassVarDec()
            print(f'class symbols --> {self.symboltable.classSymbols}')
            self.compileSubroutineDec()
            self.skipTill('}')

        self.vmwriter.close()
        # self.outputxml.close()


    def compileClassVarDec(self):
        if self.tokenizer.token() in ["static", "field"]:

            idkind = self.tokenizer.token()
            self.tokenizer.advance()
            idtype = self.tokenizer.token()
            self.tokenizer.advance()
            while(self.tokenizer.token() != ';'):
                if self.tokenizer.token() == ',':
                    self.tokenizer.advance()
                self.symboltable.define(self.tokenizer.token(), idtype, idkind)
                self.tokenizer.advance()
            self.skipTill(';')

            return self.compileClassVarDec()



    def compileSubroutineDec(self):
        if self.tokenizer.token() in ["constructor", "function", "method"]:
            self.symboltable.startSubroutine()

            self.tokenizer.advance()
            self.tokenizer.advance()
            funcname = self.tokenizer.token()
            self.skipTill('(')
            self.compileParameterList()
            self.skipTill(')')
            self.vmwriter.writeFunction(funcname, 0)
            print(f'subroutine symbols --> {self.symboltable.subroutineSymbols}')
            self.compileSubroutineBody()

            return self.compileSubroutineDec()


    def compileParameterList(self):

        while(self.tokenizer.token() != ')'):
            if self.tokenizer.token() == ',':
                self.skipTill(',')
            idtype = self.tokenizer.token()
            self.skipTill(idtype)
            idname = self.tokenizer.token()
            self.skipTill(idname)
            self.symboltable.define(idname, idtype, "arg")



    def compileSubroutineBody(self):

        self.skipTill('{')
        # self.compileVarDec()
        self.compileStatements()
        self.skipTill('}')



    def compileVarDec(self):
        if self.tokenizer.token() == "var":

            self.skipTill(';')

            return self.compileVarDec()



    def compileStatements(self):
        def compileStatement():
            if self.tokenizer.token() == "let":
                self.compileLet()
            elif self.tokenizer.token() == "if":
                self.compileIf()
            elif self.tokenizer.token() == "while":
                self.compileWhile()
            elif self.tokenizer.token() == "do":
                self.compileDo()
            elif self.tokenizer.token() == "return":
                self.compileReturn()
            else:
                return
            compileStatement()
            

        compileStatement()



    def compileLet(self):

        self.skipTill(['[', '='], False)
        if self.tokenizer.token() == "[":
            self.skipTill('[')
            self.compileExpression()
        self.skipTill('=')
        self.compileExpression()
        self.skipTill(';')



    def compileIf(self):

        self.skipTill('(')
        self.compileExpression()
        self.skipTill('{')
        self.compileStatements()
        self.skipTill('}')
        if self.tokenizer.token() == "else":
            self.skipTill('{')
            self.compileStatements()
            self.skipTill('}')



    def compileWhile(self):

        self.skipTill('(')
        self.compileExpression()
        self.skipTill('{')
        self.compileStatements()
        self.skipTill('}')



    def compileDo(self):

        self.tokenizer.advance()
        funcname = self.skipTill('(', False)
        self.skipTill('(')
        numOfArg = self.compileExpressionList()
        self.vmwriter.writeCall(funcname, numOfArg)
        self.vmwriter.writepop("temp", 0)
        self.skipTill(';')



    def compileReturn(self):

        self.skipTill("return")
        if self.tokenizer.token() != ';':
            self.compileExpression()
        else: self.vmwriter.writePush("constant", 0)
        self.vmwriter.writeReturn()
        self.skipTill(';')



    def compileExpression(self):

        self.compileTerm()
        while(self.tokenizer.token() in ARTH_COMMAND_DICT.keys()):
            command = ARTH_COMMAND_DICT[self.tokenizer.token()]
            self.skipTill(self.tokenizer.token())
            self.compileTerm()
            self.vmwriter.writeArithemetic(command)



    def compileTerm(self):

        if self.tokenizer.tokenType() in ["integerConstant", "stringConstant", "keyword", "identifier"]:
            if self.tokenizer.tokenType() == "integerConstant":
                self.vmwriter.writePush("constant", self.tokenizer.token())
            self.skipTill(self.tokenizer.token())
            if self.tokenizer.token() == '[':
                self.skipTill('[')
                self.compileExpression()
                self.skipTill(']')
            elif self.tokenizer.token() in ['(', '.']:
                self.skipTill('(')
                self.compileExpressionList()
                self.skipTill(')')
        elif self.tokenizer.token() == '(':
            self.skipTill('(')
            self.compileExpression()
            self.skipTill(')')
        elif self.tokenizer.token() in ['-', '~']:
            self.skipTill(self.tokenizer.token())
            self.compileTerm()

        

    def compileExpressionList(self):
        numOfArg = 0

        while(self.tokenizer.token() != ')'):
            numOfArg += 1
            self.compileExpression()
            if self.tokenizer.token() == ',':
                self.skipTill(',')

        return numOfArg


    def skipTill(self, stop, include=True):
        result = ""
        if type(stop) != type([]):
            stop = [stop]
        while(self.tokenizer.token() not in stop):
            result = f'{result}{self.tokenizer.token()}'
            self.tokenizer.advance()
        if include:
            result = f'{result}{self.tokenizer.token()}'
            self.tokenizer.advance()
        return result
