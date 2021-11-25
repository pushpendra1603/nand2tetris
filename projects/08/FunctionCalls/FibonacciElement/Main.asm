// function Main.fibonacci 0
(Main.fibonacci)
@0
D = A
(Main.fibonacci.pushnvars)
@nvars
M = D
@Main.fibonacci.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Main.fibonacci.pushnvars
0;JMP
(Main.fibonacci.endpush)
// push argument 0
@ARG
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push constant 2
@2
D = A
@SP
M = M + 1
A = M - 1
M = D
// lt
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
D = M - D
@JMP_TO_TRUE_1
D;JLT
@SP
A = M - 1
M = 0
@END_FALSE_EXIT_1
0;JMP
(JMP_TO_TRUE_1)
@SP
A = M - 1
M = -1
(END_FALSE_EXIT_1)
// if-goto IF_TRUE
@SP
M = M - 1
A = M
D = M
@Main.fibonacci$IF_TRUE
D;JNE
// goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP
// label IF_TRUE
(Main.fibonacci$IF_TRUE)
// push argument 0
@ARG
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// return
@LCL
D = M
@5
D = D - A
A = D
D = M
@retaddr
M = D
@SP
M = M - 1
A = M
D = M
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
// label IF_FALSE
(Main.fibonacci$IF_FALSE)
// push argument 0
@ARG
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push constant 2
@2
D = A
@SP
M = M + 1
A = M - 1
M = D
// sub
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M - D
// call Main.fibonacci 1
@Main.fibonacci$2
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
(Main.fibonacci$2)
// push argument 0
@ARG
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push constant 1
@1
D = A
@SP
M = M + 1
A = M - 1
M = D
// sub
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M - D
// call Main.fibonacci 1
@Main.fibonacci$3
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
(Main.fibonacci$3)
// add
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D
// return
@LCL
D = M
@5
D = D - A
A = D
D = M
@retaddr
M = D
@SP
M = M - 1
A = M
D = M
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
