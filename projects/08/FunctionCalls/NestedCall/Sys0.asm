
(Sys.init)
@0
D = A
(Sys.init.pushnvars)
@R13
M = D
@Sys.init.endpush
D;JEQ
@0
D = A
@SP
M = M + 1
A = M - 1
M = D
@R13
D = M
D = D - 1
@Sys.init.pushnvars
0;JMP
(Sys.init.endpush)

@4000	//
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THIS
M = D

@5000
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THAT
M = D

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

(Sys.init$LOOP)

@Sys.init$LOOP
0;JMP

(Sys.main)
@5
D = A
(Sys.main.pushnvars)
@R13
M = D
@Sys.main.endpush
D;JEQ
@0
D = A
@SP
M = M + 1
A = M - 1
M = D
@R13
D = M
D = D - 1
@Sys.main.pushnvars
0;JMP
(Sys.main.endpush)

@4001
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THIS
M = D

@5001
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THAT
M = D

@200
D = A
@SP
M = M + 1
A = M - 1
M = D

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

@40
D = A
@SP
M = M + 1
A = M - 1
M = D

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

@6
D = A
@SP
M = M + 1
A = M - 1
M = D

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

@123
D = A
@SP
M = M + 1
A = M - 1
M = D

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

@LCL
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@LCL
D = M
@1
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@LCL
D = M
@2
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@LCL
D = M
@3
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@LCL
D = M
@4
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D

@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D

@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D

@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D

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

(Sys.add12)
@0
D = A
(Sys.add12.pushnvars)
@R13
M = D
@Sys.add12.endpush
D;JEQ
@0
D = A
@SP
M = M + 1
A = M - 1
M = D
@R13
D = M
D = D - 1
@Sys.add12.pushnvars
0;JMP
(Sys.add12.endpush)

@4002
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THIS
M = D

@5002
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@THAT
M = D

@ARG
D = M
@0
A = A + D
D = M
@SP
M = M + 1
A = M - 1
M = D

@12
D = A
@SP
M = M + 1
A = M - 1
M = D

@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M + D

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
