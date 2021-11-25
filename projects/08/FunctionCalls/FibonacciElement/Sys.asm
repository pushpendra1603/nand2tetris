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
// push constant 4
@4
D = A
@SP
M = M + 1
A = M - 1
M = D
// call Main.fibonacci 1
@Main.fibonacci$1
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
@1
D = D - A
@ARG
M = D
@Main.fibonacci
0;JMP
(Main.fibonacci$1)
// label WHILE
(Sys.init$WHILE)
// goto WHILE
@Sys.init$WHILE
0;JMP
