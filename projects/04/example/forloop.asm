@100
D=A
@arr
M=D // arr=100 (base address)

@10
D=A
@n
M=D // n=10 (array length)

@i
M=0 // i=0 (start index)

// Loop

(LOOP)

@i
D=M
@n
D=D-M
@END
D ; JEQ // if (i == 0) goto END

@arr
D=M
@i
A=D+M
M=-1 // RAM[arr+i]=-1

@i
M=M+1 // i++

@LOOP
0 ; JMP

(END)

@END
0 ; JMP