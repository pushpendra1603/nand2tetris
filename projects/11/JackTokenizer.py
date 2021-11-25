import re, sys



class JackTokenizer():


    KEYWORD = "keyword"
    SYMBOL = "symbol"
    IDENTIFIER = "identifier"
    INT_CONST = "integerConstant"
    STRING_CONST = "stringConstant"

    LIST_OF_SYMBOL = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    LIST_OF_KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var',
                'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let',
                'do', 'if', 'else', 'while', 'return']
    SPECIAL_CASE = {'<': '&lt;', '>': '&gt;', '\"': '&quot;', '&': '&amp;'}


    def __init__(self, input_file):
        self.output = re.sub(r'(\.jack)', "T.xml", input_file)
        self.input = self.process(open(input_file)).strip()
        self.charpos = 0
        self.tkn = ""
        self.writexml()


    def hasMoreTokens(self):
        if self.charpos < len(self.input):
            return True
        return False


    def advance(self):
        self.tkn = ""
        while(self.hasMoreTokens()):
            self.tkn += self.input[self.charpos]
            self.charpos += 1
            if self.tkn in [" ", "\t"]:
                return self.advance()
            if self.tkn in self.LIST_OF_SYMBOL:
                return
            if self.tkn in ["\"", "\'"]:
                temp = self.input[self.charpos:].index("\"")
                self.tkn += self.input[self.charpos:self.charpos+temp+1]
                self.charpos += temp + 1
                return
            if self.input[self.charpos] in [" ", "\t"] + self.LIST_OF_SYMBOL:
                return


    def tokenType(self):
        if self.tkn in self.LIST_OF_KEYWORDS:
            return self.KEYWORD
        elif self.tkn in self.LIST_OF_SYMBOL:
            return self.SYMBOL
        elif self.tkn[0] == "\"":
            return self.STRING_CONST
        try:
            int(self.tkn)
            return self.INT_CONST
        except:
            if len(self.tkn) > 0:
                return self.IDENTIFIER
            else:
                return None


    def keyWord(self):
        if self.tokenType() == self.KEYWORD:
            return self.tkn


    def symbol(self):
        if self.tokenType() == self.SYMBOL:
            try:
                return self.SPECIAL_CASE[self.tkn]
            except:
                return self.tkn


    def identifier(self):
        if self.tokenType() == self.IDENTIFIER:
            return self.tkn


    def intVal(self):
        if self.tokenType() == self.INT_CONST:
            return int(self.tkn)


    def stringVal(self):
        if self.tokenType() == self.STRING_CONST:
            return self.tkn[1:-1]


    def token(self):
        if self.tokenType() == self.KEYWORD:
            return self.keyWord()
        elif self.tokenType() == self.SYMBOL:
            return self.symbol()
        elif self.tokenType() == self.IDENTIFIER:
            return self.identifier()
        elif self.tokenType() == self.INT_CONST:
            return self.intVal()
        elif self.tokenType() == self.STRING_CONST:
            return self.stringVal()


    def process(self, input_file):
        result = ""
        for line in input_file:
            line = line.strip()
            line = re.sub(r"(\/\/.*)|(\/\*\*.*)|(\n)|^(\*.*)", "", line).strip()
            if line != "":
                result+=(f'{line} ')
        return result


    def writexml(self):
        xml = open(self.output, 'w')
        xml.write("<tokens>\n")
        while(self.hasMoreTokens()):
            self.advance()
            xml.write(f'<{self.tokenType()}> {self.token()} </{self.tokenType()}>\n')
        xml.write("</tokens>\n")
        xml.close()
        self.charpos = 0


def main(ip, op=None):
    tokenizer = JackTokenizer(ip)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    for input_file in arguments:
        main(input_file)
