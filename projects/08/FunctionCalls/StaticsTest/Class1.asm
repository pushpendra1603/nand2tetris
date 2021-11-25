// function Class1.set 0
(Class1.set)
@0
D = A
(Class1.set.pushnvars)
@nvars
M = D
@Class1.set.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Class1.set.pushnvars
0;JMP
(Class1.set.endpush)
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
// pop static 0
@SP
M = M - 1
A = M
D = M
@Class1.0
M = D
// push argument 1
@ARG
D = M
@1
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// pop static 1
@SP
M = M - 1
A = M
D = M
@Class1.1
M = D
// push constant 0
@0
D = A
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
// function Class1.get 0
(Class1.get)
@0
D = A
(Class1.get.pushnvars)
@nvars
M = D
@Class1.get.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Class1.get.pushnvars
0;JMP
(Class1.get.endpush)
// push static 0
@Class1.0
D = M
@SP
M = M + 1
A = M - 1
M = D
// push static 1
@Class1.1
D = M
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
