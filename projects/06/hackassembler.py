import re



symbol = dict()
pdsymb = open("pdsymbol.txt")
currloc = 16

for line in pdsymb:
    line = line.strip().split(" ")
    symbol[line[0]] = line[1]

def main():
    asm = open("pong\\Pong.asm").read()
    with open("hack.hack", "w") as f:
        code = scan(asm)
        hack = bincode(code)
        f.write(hack)

def bincode(code):
    lines = code.splitlines()
    hack = ""
    for line in lines:
        if line[0] == "@": bncode = ainst(line[1:])
        else: bncode = cinst(line)       
        hack = hack + bncode + '\n'
    return hack

def ainst(line):
    global currloc
    bncode = ""
    try: bncode = int(line)
    except:
        if line in symbol.keys():
            bncode = int(symbol[line])
        else:
            symbol[line] = currloc
            bncode = currloc
            currloc+=1
    bncode = bin(bncode)
    bncode = bncode.replace('b', '0'*(17-len(bncode)))
    return bncode

def cinst(line):
    bncode = "111"
    comp = "0000000"
    dest = "000"
    jump = "000"
    line = line.split(';')
    if len(line) > 1: jump = jumpcode(line[1])
    line = line[0].split('=')
    if len(line) > 1:
        comp = compcode(line[1])
        dest = destcode(line[0])
    else: comp = compcode(line[0])
    bncode = bncode + comp + dest + jump
    return bncode

def jumpcode(c):
    if c == "JGT": return '001'
    if c == "JEQ": return '010'
    if c == "JGE": return '011'
    if c == "JLT": return '100'
    if c == "JNE": return '101'
    if c == "JLE": return '110'
    if c == "JMP": return '111'
    else: return '000'

def compcode(c):
    cd = ""
    if c in ['0']: cd = '101010'
    elif c in ['1']: cd = '111111'
    elif c in ['-1']: cd = '111010'
    elif c in ['D']: cd = '001100'
    elif c in ['A', 'M']: cd = '110000'
    elif c in ['!D']: cd = '001101'
    elif c in ['!A', '!M']: cd = '110001'
    elif c in ['-D']: cd = '001111'
    elif c in ['-A', '-M']: cd = '110011'
    elif c in ['D+1']: cd = '011111'
    elif c in ['A+1', 'M+1']: cd = '110111'
    elif c in ['D-1']: cd = '001110'
    elif c in ['A-1', 'M-1']: cd = '110010'
    elif c in ['D+A', 'D+M']: cd = '000010'
    elif c in ['D-A', 'D-M']: cd = '010011'
    elif c in ['A-D', 'M-D']: cd = '000111'
    elif c in ['D&A', 'D&M']: cd = '000000'
    elif c in ['D|A', 'D|M']: cd = '010101'
    
    if 'M' in c: cd = '1' + cd
    else: cd = '0' + cd
    return cd

def destcode(c):
    cd = ['0','0','0']
    if 'A' in c: cd[0] = '1'
    if 'D' in c: cd[1] = '1'
    if 'M' in c: cd[2] = '1'
    return ''.join(cd)


def scan(asm):
    code = ""
    pc = 0
    asm = cleancode(asm).splitlines()
    for line in asm:
        if line[0] == '(':
            symbol[line[1:-1]] = pc
            continue
        code = code + line + '\n'
        pc+=1
    return code.strip()


def cleancode(code):
    code = re.sub('(\/{2}.*)|([ ]*)', "", code)
    code = re.sub("^[\n]*", "", code)
    return code

if __name__ == "__main__":
    main()