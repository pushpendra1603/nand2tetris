import re



class CodeWriter:

    segment_dict = {"local": "LCL", "position": "ARG",
                    "this": "THIS", "that": "THAT", "temp": "5"}
    symbol_dict = {"add": "+", "sub": "-", "neg": "-", "and": "&",
                 "or": "|", "not": "!", "lt": "<", "gt": ">", "eq": "=="}

    def __init__(self, output_file):
        self.output = open(output_file, "a")
        self.index = 0
        self.filename = ""
        self.funcname = self.filename


    @staticmethod
    def stack_push():
        return '''
        @SP
        M = M + 1
        A = M - 1
        M = D
        '''

    @staticmethod
    def stack_pop():
        return '''
        @SP
        M = M - 1
        A = M
        D = M
        '''

    @staticmethod
    def stack_peek():
        return '''
        @SP
        A = M - 1
        '''


    def if_else(self, jumpCondition, iftrue, elseExecute):
        self.index += 1
        return f'''
        {self.stack_pop()}
        {self.stack_peek()}
        D = M - D
        @JMP_IF_NOT_LGT_{self.index}
        D;{jumpCondition}
        {self.stack_peek()}
        {elseExecute}
        @END_LGT_{self.index}
        0;JMP
        (JMP_IF_NOT_LGT_{self.index})
        {self.stack_peek()}
        {iftrue}
        (END_LGT_{self.index})                
        '''


    def print(self, *arg):
        text = " ".join(arg)
        text = "\n".join(map(lambda ln: ln.strip(), text.splitlines()))
        text = re.sub(r"\n+", "\n", text)
        self.output.write(text)
        

    def writeArithemetic(self, operation):
        self.print(f'// {operation}')
        if operation in ["add", "sub", "and", "or"]:
            self.print(f'''
            {self.stack_pop()}
            {self.stack_peek()}
            M = M {self.symbol_dict[operation]} D
            ''')

        elif operation in ["not", "neg"]:
            self.print(f'''
            {self.stack_peek()}
            M = {self.symbol_dict[operation]}M
            ''')

        elif operation == "lt":
            self.print(f'''            
            {self.if_else("JLT", "M = -1", "M = 0")}
            ''')

        elif operation == "gt":
            self.print(f'''
            {self.if_else("JGT", "M = -1", "M = 0")}
            ''')

        elif operation == "eq":
            self.print(f'''
            {self.if_else("JEQ", "M = -1", "M = 0")}
            ''')


    def writePushPop(self, command, segment, position):
        self.print(f'// {command} {segment} {position}')
        if command == "push":
            if segment in ["local", "position", "this", "that", "temp"]:
                self.print(f'''
                @{self.segment_dict[segment]}
                D = {"A" if segment=="temp" else "M"}
                @{position}
                A = A + D
                D = M
                {self.stack_push()}
                ''')
            elif segment == "constant":
                self.print(f'''
                @{position}
                D = A
                {self.stack_push()}
                ''')
            elif segment == "static":
                self.print(f'''
                @{self.funcname}.{position}
                D = M
                {self.stack_push()}
                ''')
            elif segment == "pointer":
                self.print(f'''
                @{"THAT" if int(position) else "THIS"}
                D = M
                {self.stack_push()}
                ''')

        elif command == "pop":
            if segment in ["local", "position", "this", "that", "temp"]:
                self.print(f'''
                @{self.segment_dict[segment]}
                D = {"A" if segment=="temp" else "M"}
                @{position}
                D = A + D
                @R13
                M = D
                {self.stack_pop()}
                @R13
                A = M
                M = D
                ''')
            elif segment == "static":
                self.print(f'''
                {self.stack_pop()}
                @{self.funcname}.{position}
                M = D
                ''')
            elif segment == "pointer":
                self.print(f'''
                {self.stack_pop()}
                @{"THAT" if int(position) else "THIS"}
                M = D
                ''')

    
    def setFileName(self, filename):
        pass


    def writeInit(self):
        pass


    def writeLabel(self, label):
        self.print(f'''
        // label {label}
        ({self.funcname}${label})
        ''')

    
    def writeGoto(self, label):
        self.print(f'''
        // goto {label}
        @{self.funcname}${label}
        0;JMP
        ''')


    def writeIf(self, label):
        self.print(f'''
        // if-goto {label}
        {self.stack_pop()}
        @{self.funcname}${label}
        D;JNE
        ''')


    def writeFunction(self, funcname, numvars):
        self.funcname = funcname
        self.print(f'''
        // function {funcname} {numvars}
        ({funcname})
        @{numvars}
        D = A
        ({funcname}.pushnvars)
        @R13
        M = D
        @{funcname}.endpush
        D;JEQ
        @0
        D = A
        {self.stack_push()}
        @R13
        D = M
        D = D - 1
        @{funcname}.pushnvars
        0;JMP
        ({funcname}.endpush)
        ''')


    def writeCall(self, funcname, numargs):
        self.index += 1
        self.print(f'''
        // call {funcname} {numargs}
        @{funcname}${self.index}
        D = A
        {self.stack_push()}
        @LCL
        D = M
        {self.stack_push()}
        @ARG
        D = M
        {self.stack_push()}
        @THIS
        D = M
        {self.stack_push()}
        @THAT
        D = M
        {self.stack_push()}
        @SP
        D = M
        @LCL
        M = D
        @5
        D = D - A
        @{numargs}
        D = D - A
        @ARG
        M = D
        @{funcname}
        0;JMP
        ({funcname}${self.index})
        ''')


    def writeReturn(self):
        self.print(f'''
        // return
        @LCL
        D = M
        @5
        D = D - A
        A = D
        D = M
        @retaddr
        M = D
        {self.stack_pop()}
        @ARG
        A = M
        M = D
        @ARG
        D = M
        @SP
        M = D + 1
        @1
        D = A
        @LCL
        A = M - D
        D = M
        @THAT
        M = D
        @2
        D = A
        @LCL
        A = M - D
        D = M
        @THIS
        M = D
        @3
        D = A
        @LCL
        A = M - D
        D = M
        @ARG
        M = D
        @4
        D = A
        @LCL
        A = M - D
        D = M
        @LCL
        M = D
        @retaddr
        A = M
        0;JMP
        ''')


    def close(self):
        self.output.close()