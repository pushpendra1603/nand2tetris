import sys
from os import path
import re
import os
import fileinput


class CodeGen:
    segment_dict = {"local": "LCL", "argument": "ARG",
                    "this": "THIS", "that": "THAT", "temp": "5"}
    arth_dict = {"add": "+", "sub": "-", "neg": "-", "and": "&",
                 "or": "|", "not": "!", "lt": "<", "gt": ">", "eq": "=="}
    index = 0

    def print(self, *arg):
        text = " ".join(arg)
        text = "\n".join(map(lambda ln: ln.strip(), text.splitlines()))
        text = re.sub(r"\n+", "\n", text)
        self.file.write(text)

    def __init__(self, output_file):
        self.filename = path.basename(output_file).split(".")[0]
        self.funcname = self.filename
        self.file = open(output_file, "w")

    def __del__(self):
        self.file.close()


    def bootstrap(self):
        self.print(f'''
        @256
        D = A
        @SP
        M = D
        {self.call_command("Sys.init", "0")}
        ''')


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
        @JMP_TO_TRUE_{self.index}
        D;{jumpCondition}
        {self.stack_peek()}
        {elseExecute}
        @END_FALSE_EXIT_{self.index}
        0;JMP
        (JMP_TO_TRUE_{self.index})
        {self.stack_peek()}
        {iftrue}
        (END_FALSE_EXIT_{self.index})                
        '''

    def call_command(self, memory_segment, argument):
        self.index += 1
        return f'''
        @{memory_segment}${self.index}
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
        @{argument}
        D = D - A
        @ARG
        M = D
        @{memory_segment}
        0;JMP
        ({memory_segment}${self.index})
        '''

    def generate_code(self, command, memory_segment=None, argument=None):
        self.print("//", command, memory_segment if memory_segment else "",
                   argument if argument else "")
        if command == "push":
            if memory_segment in ["local", "argument", "this", "that", "temp"]:
                self.print(f'''
                @{self.segment_dict[memory_segment]}
                D = {"A" if memory_segment=="temp" else "M"}
                @{argument}
                A = A + D
                D = M
                {self.stack_push()}
                ''')
            elif memory_segment == "constant":
                self.print(f'''
                @{argument}
                D = A
                {self.stack_push()}
                ''')
            elif memory_segment == "static":
                self.print(f'''
                @{self.filename}.{argument}
                D = M
                {self.stack_push()}
                ''')
            elif memory_segment == "pointer":
                self.print(f'''
                @{"THAT" if int(argument) else "THIS"}
                D = M
                {self.stack_push()}
                ''')

        elif command == "pop":
            if memory_segment in ["local", "argument", "this", "that", "temp"]:
                self.print(f'''
                @{self.segment_dict[memory_segment]}
                D = {"A" if memory_segment=="temp" else "M"}
                @{argument}
                D = A + D
                @R13
                M = D
                {self.stack_pop()}
                @R13
                A = M
                M = D
                ''')
            elif memory_segment == "static":
                self.print(f'''
                {self.stack_pop()}
                @{self.filename}.{argument}
                M = D
                ''')
            elif memory_segment == "pointer":
                self.print(f'''
                {self.stack_pop()}
                @{"THAT" if int(argument) else "THIS"}
                M = D
                ''')

        elif command in ["add", "sub", "and", "or"]:
            self.print(f'''
            {self.stack_pop()}
            {self.stack_peek()}
            M = M {self.arth_dict[command]} D
            ''')

        elif command in ["not", "neg"]:
            self.print(f'''
            {self.stack_peek()}
            M = {self.arth_dict[command]}M
            ''')

        elif command == "lt":
            self.print(f'''            
            {self.if_else("JLT", "M = -1", "M = 0")}
            ''')

        elif command == "gt":
            self.print(f'''
            {self.if_else("JGT", "M = -1", "M = 0")}
            ''')

        elif command == "eq":
            self.print(f'''
            {self.if_else("JEQ", "M = -1", "M = 0")}
            ''')

        elif command == "label":
            self.print(f'''
            ({self.funcname}${memory_segment})
            ''')

        elif command == "goto":
            self.print(f'''
            @{self.funcname}${memory_segment}
            0;JMP
            ''')

        elif command == "if-goto":
            self.print(f'''
            {self.stack_pop()}
            @{self.funcname}${memory_segment}
            D;JNE
            ''')

        elif command == "call":
            self.print(self.call_command(memory_segment, argument))

        elif command == "function":
            self.funcname = memory_segment
            self.filename = self.funcname.split(".")[0]
            self.print(f'''
            ({memory_segment})
            @{argument}
            D = A
            ({memory_segment}.pushnvars)
            @nvars
            M = D
            @{memory_segment}.endpush
            D;JEQ
            D = 0
            {self.stack_push()}
            @nvars
            D = M
            D = D - 1
            @{memory_segment}.pushnvars
            0;JMP
            ({memory_segment}.endpush)
            ''')

        elif command == "return":
            self.print(f'''
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


def process(line):
    line = re.sub(r"(//.*)|(\n)", "", line).strip()
    if line == "":
        return None
    else:
        commands = line.split(" ")
        cmd = commands[0]
        memory_segment = commands[1] if len(commands) >= 2 else None
        argument = commands[2] if len(commands) >= 3 else None
        return (cmd, memory_segment, argument)


def main(ip, op=None):
    input_file = ip
    absolute_file_path = path.abspath(ip)
    output_file = op
    if path.isfile(input_file):
        output_file = path.join(
            path.dirname(absolute_file_path), ".".join(path.basename(input_file).split(".")[:-1]) + ".asm")
        ip = [ip]
    elif path.isdir(input_file):
        output_file = path.join(
            absolute_file_path, path.basename(absolute_file_path) + ".asm")
        ip = list(map(lambda x: path.join(absolute_file_path, x), filter(
            lambda x: x.endswith(".vm"), os.listdir(input_file))))
    doesSysVmExists = len(list(filter(lambda x: x.lower() == "sys.vm", os.listdir(input_file)))) == 1
    with fileinput.input(files=tuple(ip)) as f:
        # print(f)
        cg = CodeGen(output_file)
        if doesSysVmExists:
            cg.bootstrap()
        for line in f:
            x = process(line)
            if x:
                cg.generate_code(*x)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    for input_file in arguments:
        main(input_file)
