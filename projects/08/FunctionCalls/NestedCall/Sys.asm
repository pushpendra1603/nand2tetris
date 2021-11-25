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
// push constant 4000
@4000
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5000
@5000
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 1
@SP
M = M - 1
A = M
D = M
@THAT
M = D
// call Sys.main 0
@Sys.main$1
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
@Sys.main
0;JMP
(Sys.main$1)
// pop temp 1
@5
D = A
@1
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
// label LOOP
(Sys.init$LOOP)
// goto LOOP
@Sys.init$LOOP
0;JMP
// function Sys.main 5
(Sys.main)
@5
D = A
(Sys.main.pushnvars)
@nvars
M = D
@Sys.main.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Sys.main.pushnvars
0;JMP
(Sys.main.endpush)
// push constant 4001
@4001
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5001
@5001
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 1
@SP
M = M - 1
A = M
D = M
@THAT
M = D
// push constant 200
@200
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop local 1
@LCL
D = M
@1
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
// push constant 40
@40
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop local 2
@LCL
D = M
@2
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
// push constant 6
@6
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop local 3
@LCL
D = M
@3
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
// push constant 123
@123
D = A
@SP
M = M + 1
A = M - 1
M = D
// call Sys.add12 1
@Sys.add12$2
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
@Sys.add12
0;JMP
(Sys.add12$2)
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
// push local 2
@LCL
D = M
@2
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push local 3
@LCL
D = M
@3
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D
// push local 4
@LCL
D = M
@4
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
// add
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D
// add
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D
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
// function Sys.add12 0
(Sys.add12)
@0
D = A
(Sys.add12.pushnvars)
@nvars
M = D
@Sys.add12.endpush
D;JEQ
D = 0
@SP
M = M + 1
A = M - 1
M = D
@nvars
D = M
D = D - 1
@Sys.add12.pushnvars
0;JMP
(Sys.add12.endpush)
// push constant 4002
@4002
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5002
@5002
D = A
@SP
M = M + 1
A = M - 1
M = D
// pop pointer 1
@SP
M = M - 1
A = M
D = M
@THAT
M = D
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
// push constant 12
@12
D = A
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
