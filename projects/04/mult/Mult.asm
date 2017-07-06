// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Psuedo code
    // a = RAM[0]
    // b = RAM[1]
    // result = 0
    // i = 0

    // LOOP:
     // if i > 0 goto END
     // result = result + a
     // i++

    // END
     // goto END

// Initialize

@R0
D = M
@a
M = D

@R1
D = M
@b
M = D

@R2
M = 0

@i
M = 0

// LOOP

(LOOP)

@i
D = M
@b
D = D - M
@END
D ; JEQ

@a
D = M
@R2
M = M + D

@i
M = M + 1

@LOOP
0 ; JMP

(END)

@END
0 ; JMP