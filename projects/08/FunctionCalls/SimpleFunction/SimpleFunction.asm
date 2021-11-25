// function SimpleFunction.test 2
(SimpleFunction.test)
@2
D = A
(SimpleFunction.test.pushnvars)
@nvars
M = D
@SimpleFunction.test.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@SimpleFunction.test.pushnvars
0;JMP
(SimpleFunction.test.endpush)
// push local 0
@LCL
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push local 1
@LCL
D = M
@1
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// add
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D
// not
@SP
A = M - 1
M = !M
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
// add
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D
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
