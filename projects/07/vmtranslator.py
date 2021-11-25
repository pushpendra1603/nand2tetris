import sys
from os import path
import re


class CodeGen:
    segment_dict = {"local": "LCL", "argument": "ARG",
                    "this": "THIS", "that": "THAT", "temp": "5"}
    arth_dict = {"add": "+", "sub": "-", "neg": "-", "and": "&",
                 "or": "|", "not": "!", "lt": "<", "gt": ">", "eq": "=="}

    def print(self, *arg):
        text = " ".join(arg)
        text = "\n".join(map(lambda ln: ln.strip(), text.splitlines()))
        text = re.sub(r"\n+", "\n", text)
        self.file.write(text)

    def __init__(self, output_file):
        self.filename = path.basename(output_file)[0]
        self.index = 0
        self.file = open(output_file, "w")

    def __del__(self):
        self.file.close()

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


def process(line):
    line =  re.sub(r"(//.*)|(\n)", "", line).strip()
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
    if output_file == None:
        output_file = path.join(
            path.dirname(absolute_file_path), ".".join(path.basename(input_file).split(".")[:-1]) + ".asm")
    with open(ip, "r") as input_file:
        cg = CodeGen(output_file)
        for line in input_file:
            x = process(line)
            if x:
                cg.generate_code(*x)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        for input_file in arguments:
            main(input_file)
    else:
        main(arguments[0], arguments[1])
