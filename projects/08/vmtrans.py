from Parser import Parser as parser
from CodeWriter import CodeWriter as codewriter



file1 = parser(r"ProgramFlow\BasicLoop\BasicLoop.vm")
out1 = codewriter(r"Test.asm")
while file1.hasMoreCommands():
    file1.advance()
    print(f'{file1.currline} {file1.command}')
# print(file1.currline)