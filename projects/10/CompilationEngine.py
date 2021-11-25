from JackTokenizer import JackTokenizer
import re



class CompilationEngine:


    def __init__(self, input_file, output_file=None):
        if output_file == None:
            output_file = re.sub(r'(\.jack)', ".xml", input_file)
        self.tokenizer = JackTokenizer(input_file)
        self.output = open(output_file, 'w')
        self.spaces = 0

    
    def compileClass(self):
        if self.tokenizer.hasMoreTokens(): self.tokenizer.advance()
        if self.tokenizer.token() == "class":
            self.printOutput("<class>", 2)
            self.writeTill('{')
            self.compileClassVarDec()
            self.compileSubroutineDec()
            self.writeTill('}')
            self.printOutput("</class>", -2)
        self.output.close()


    def compileClassVarDec(self):
        if self.tokenizer.token() in ["static", "field"]:
            self.printOutput("<classVarDec>", 2)
            self.writeTill(';')
            self.printOutput("</classVarDec>", -2)
            return self.compileClassVarDec()



    def compileSubroutineDec(self):
        if self.tokenizer.token() in ["constructor", "function", "method"]:
            self.printOutput("<subroutineDec>", 2)
            self.writeTill('(')
            self.compileParameterList()
            self.writeTill(')')
            self.compileSubroutineBody()
            self.printOutput("</subroutineDec>", -2)
            return self.compileSubroutineDec()


    def compileParameterList(self):
        self.printOutput("<parameterList>", 2)
        self.writeTill(')', False)
        self.printOutput("</parameterList>", -2)


    def compileSubroutineBody(self):
        self.printOutput("<subroutineBody>", 2)
        self.writeTill('{')
        self.compileVarDec()
        self.compileStatements()
        self.writeTill('}')
        self.printOutput("</subroutineBody>", -2)


    def compileVarDec(self):
        if self.tokenizer.token() == "var":
            self.printOutput("<varDec>", 2)
            self.writeTill(';')
            self.printOutput("</varDec>", -2)
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
            
        self.printOutput("<statements>", 2)
        compileStatement()
        self.printOutput("</statements>", -2)


    def compileLet(self):
        self.printOutput("<letStatement>", 2)
        self.writeTill(['[', '='], False)
        if self.tokenizer.token() == "[":
            self.writeTill('[')
            self.compileExpression()
        self.writeTill('=')
        self.compileExpression()
        self.writeTill(';')
        self.printOutput("</letStatement>", -2)


    def compileIf(self):
        self.printOutput("<ifStatement>", 2)
        self.writeTill('(')
        self.compileExpression()
        self.writeTill('{')
        self.compileStatements()
        self.writeTill('}')
        if self.tokenizer.token() == "else":
            self.writeTill('{')
            self.compileStatements()
            self.writeTill('}')
        self.printOutput("</ifStatement>", -2)


    def compileWhile(self):
        self.printOutput("<whileStatement>", 2)
        self.writeTill('(')
        self.compileExpression()
        self.writeTill('{')
        self.compileStatements()
        self.writeTill('}')
        self.printOutput("</whileStatement>", -2)


    def compileDo(self):
        self.printOutput("<doStatement>", 2)
        self.writeTill('(')
        self.compileExpressionList()
        self.writeTill(';')
        self.printOutput("</doStatement>", -2)


    def compileReturn(self):
        self.printOutput("<returnStatement>", 2)
        self.writeTill("return")
        if self.tokenizer.token() != ';':
            self.compileExpression()
        self.writeTill(';')
        self.printOutput("</returnStatement>", -2)


    def compileExpression(self):
        self.printOutput("<expression>", 2)
        self.compileTerm()
        while(self.tokenizer.token() in ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']):
            self.writeTill(self.tokenizer.token())
            self.compileTerm()
        self.printOutput("</expression>", -2)


    def compileTerm(self):
        self.printOutput("<term>", 2)
        if self.tokenizer.tokenType() in ["integerConstant", "stringConstant", "keyword", "identifier"]:
            self.writeTill(self.tokenizer.token())
            if self.tokenizer.token() == '[':
                self.writeTill('[')
                self.compileExpression()
                self.writeTill(']')
            elif self.tokenizer.token() in ['(', '.']:
                self.writeTill('(')
                self.compileExpressionList()
                self.writeTill(')')
        elif self.tokenizer.token() == '(':
            self.writeTill('(')
            self.compileExpression()
            self.writeTill(')')
        elif self.tokenizer.token() in ['-', '~']:
            self.writeTill(self.tokenizer.token())
            self.compileTerm()
        self.printOutput("</term>", -2)
        

    def compileExpressionList(self):
        self.printOutput("<expressionList>", 2)
        while(self.tokenizer.token() != ')'):
            self.compileExpression()
            if self.tokenizer.token() == ',':
                self.writeTill(',')
        self.printOutput("</expressionList>", -2)


    def writeTag(self):
        self.printOutput(f'<{self.tokenizer.tokenType()}> {self.tokenizer.token()} </{self.tokenizer.tokenType()}>')
        self.tokenizer.advance()


    def writeTill(self, stop, include=True):
        if type(stop) != type([]):
            stop = [stop]
        while(self.tokenizer.token() not in stop):
            self.writeTag()
        if include:
            self.writeTag()


    def printOutput(self, string="", spacing=0):
        if spacing < 0:
            self.spaces += spacing
        self.output.write(f'{" "*self.spaces}{string}\n')
        # self.output.flush()
        # print(f'{" "*self.spaces}{string}', file = self.output, flush=True)
        if spacing > 0:
            self.spaces += spacing