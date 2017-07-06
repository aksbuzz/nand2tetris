// Initialization

@R0
D=M
@n
M=D // n = R0

@i
M=1 // i = 1

@sum
M=0 // sum = 0

// Loop

(LOOP)
@i
D=M
@n
D=D-M
@STOP
D;JGT // if i > 0 goto STOP

@sum
D=M
@i
D=D+M
@sum
M=D // sum = sum + i
@i
M=M+1 // i++

@LOOP
0;JMP

(STOP)
@sum
D=M
@R1
M=D // RAM[1] = sum
