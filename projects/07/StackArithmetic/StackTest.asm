// push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// eq
@SP
A = M - 1
D = M
@JMP_IF_NOT_LGT_1
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_1
0;JMP
(JMP_IF_NOT_LGT_1)
@SP
A = M - 1
M = 1
(END_LGT_1)
// push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 16
@16
D = A
@SP
M = M + 1
A = M - 1
M = D
// eq
@SP
A = M - 1
D = M
@JMP_IF_NOT_LGT_2
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_2
0;JMP
(JMP_IF_NOT_LGT_2)
@SP
A = M - 1
M = 1
(END_LGT_2)
// push constant 16
@16
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// eq
@SP
A = M - 1
D = M
@JMP_IF_NOT_LGT_3
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_3
0;JMP
(JMP_IF_NOT_LGT_3)
@SP
A = M - 1
M = 1
(END_LGT_3)
// push constant 892
@892
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 891
@891
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
@JMP_IF_NOT_LGT_4
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_4
0;JMP
(JMP_IF_NOT_LGT_4)
@SP
A = M - 1
M = 1
(END_LGT_4)
// push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 892
@892
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
@JMP_IF_NOT_LGT_5
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_5
0;JMP
(JMP_IF_NOT_LGT_5)
@SP
A = M - 1
M = 1
(END_LGT_5)
// push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 891
@891
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
@JMP_IF_NOT_LGT_6
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_6
0;JMP
(JMP_IF_NOT_LGT_6)
@SP
A = M - 1
M = 1
(END_LGT_6)
// push constant 32767
@32767
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// gt
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
D = D - M
@JMP_IF_NOT_LGT_7
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_7
0;JMP
(JMP_IF_NOT_LGT_7)
@SP
A = M - 1
M = 1
(END_LGT_7)
// push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 32767
@32767
D = A
@SP
M = M + 1
A = M - 1
M = D
// gt
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
D = D - M
@JMP_IF_NOT_LGT_8
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_8
0;JMP
(JMP_IF_NOT_LGT_8)
@SP
A = M - 1
M = 1
(END_LGT_8)
// push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// gt
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
D = D - M
@JMP_IF_NOT_LGT_9
D;JGT
@SP
A = M - 1
M = 0
@END_LGT_9
0;JMP
(JMP_IF_NOT_LGT_9)
@SP
A = M - 1
M = 1
(END_LGT_9)
// push constant 57
@57
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 31
@31
D = A
@SP
M = M + 1
A = M - 1
M = D
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
A = M - 1
M = -M
// and
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M & D
// push constant 82
@82
D = A
@SP
M = M + 1
A = M - 1
M = D
// or
@SP
M = M - 1
A = M
D = M
@SP
A = M - 1
M = M | D
// not
@SP
A = M - 1
M = !M
