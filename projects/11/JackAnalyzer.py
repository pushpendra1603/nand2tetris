from os import path
import sys, os
from CompilationEngine import CompilationEngine



def main(ip, op=None):
    compileEngine = CompilationEngine(ip, op)
    compileEngine.compileClass()


if __name__ == "__main__":
    arguments = sys.argv[1:]
    ipfiles = []
    for ip in arguments:
        absolute_file_path = path.abspath(ip)
        if path.isfile(ip):
            ipfiles.append(ip)
        elif path.isdir(ip):
            ipfiles.extend(list(map(lambda x: path.join(absolute_file_path, x), filter(lambda x: x.endswith(".jack"), os.listdir(ip)))))
    for input_file in ipfiles:
        main(input_file)
    # main("ArrayTest\Main.jack")