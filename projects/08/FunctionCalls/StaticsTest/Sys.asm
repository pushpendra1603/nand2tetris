// function Sys.init 0
(Sys.init)
@0
D = A
(Sys.init.pushnvars)
@nvars
M = D
@Sys.init.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Sys.init.pushnvars
0;JMP
(Sys.init.endpush)
// push constant 6
@6
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 8
@8
D = A
@SP
M = M + 1
A = M - 1
M = D
// call Class1.set 2
@Class1.set$1
D = A
@SP
M = M + 1
A = M - 1
M = D
@LCL
D = M
@SP
M = M + 1
A = M - 1
M = D
@ARG
D = M
@SP
M = M + 1
A = M - 1
M = D
@THIS
D = M
@SP
M = M + 1
A = M - 1
M = D
@THAT
D = M
@SP
M = M + 1
A = M - 1
M = D
@SP
D = M
@LCL
M = D
@5
D = D - A
@2
D = D - A
@ARG
M = D
@Class1.set
0;JMP
(Class1.set$1)
// pop temp 0
@5
D = A
@0
D = A + D
@R13
M = D
@SP
M = M - 1
A = M
D = M
@R13
A = M
M = D
// push constant 23
@23
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 15
@15
D = A
@SP
M = M + 1
A = M - 1
M = D
// call Class2.set 2
@Class2.set$2
D = A
@SP
M = M + 1
A = M - 1
M = D
@LCL
D = M
@SP
M = M + 1
A = M - 1
M = D
@ARG
D = M
@SP
M = M + 1
A = M - 1
M = D
@THIS
D = M
@SP
M = M + 1
A = M - 1
M = D
@THAT
D = M
@SP
M = M + 1
A = M - 1
M = D
@SP
D = M
@LCL
M = D
@5
D = D - A
@2
D = D - A
@ARG
M = D
@Class2.set
0;JMP
(Class2.set$2)
// pop temp 0
@5
D = A
@0
D = A + D
@R13
M = D
@SP
M = M - 1
A = M
D = M
@R13
A = M
M = D
// call Class1.get 0
@Class1.get$3
D = A
@SP
M = M + 1
A = M - 1
M = D
@LCL
D = M
@SP
M = M + 1
A = M - 1
M = D
@ARG
D = M
@SP
M = M + 1
A = M - 1
M = D
@THIS
D = M
@SP
M = M + 1
A = M - 1
M = D
@THAT
D = M
@SP
M = M + 1
A = M - 1
M = D
@SP
D = M
@LCL
M = D
@5
D = D - A
@0
D = D - A
@ARG
M = D
@Class1.get
0;JMP
(Class1.get$3)
// call Class2.get 0
@Class2.get$4
D = A
@SP
M = M + 1
A = M - 1
M = D
@LCL
D = M
@SP
M = M + 1
A = M - 1
M = D
@ARG
D = M
@SP
M = M + 1
A = M - 1
M = D
@THIS
D = M
@SP
M = M + 1
A = M - 1
M = D
@THAT
D = M
@SP
M = M + 1
A = M - 1
M = D
@SP
D = M
@LCL
M = D
@5
D = D - A
@0
D = D - A
@ARG
M = D
@Class2.get
0;JMP
(Class2.get$4)
// label WHILE
(Sys.init$WHILE)
// goto WHILE
@Sys.init$WHILE
0;JMP
