.macro SAVE_T_REGISTERS
# brace yourself for a long, unrolled loop...
sw           $t0,    ($sp)
subiu        $sp,      $sp,        4
sw           $t1,    ($sp)
subiu        $sp,      $sp,        4
sw           $t2,    ($sp)
subiu        $sp,      $sp,        4
sw           $t3,    ($sp)
subiu        $sp,      $sp,        4
sw           $t4,    ($sp)
subiu        $sp,      $sp,        4
sw           $t5,    ($sp)
subiu        $sp,      $sp,        4
sw           $t6,    ($sp)
subiu        $sp,      $sp,        4
sw           $t7,    ($sp)
subiu        $sp,      $sp,        4
sw           $t8,    ($sp)
subiu        $sp,      $sp,        4
sw           $t9,    ($sp)
subiu        $sp,      $sp,        4
.end_macro

.macro RESTORE_T_REGISTERS
# brace yourself for a long, unrolled loop...
addiu        $sp,      $sp,        4
lw           $t9,    ($sp)
addiu        $sp,      $sp,        4
lw           $t8,    ($sp)
addiu        $sp,      $sp,        4
lw           $t7,    ($sp)
addiu        $sp,      $sp,        4
lw           $t6,    ($sp)
addiu        $sp,      $sp,        4
lw           $t5,    ($sp)
addiu        $sp,      $sp,        4
lw           $t4,    ($sp)
addiu        $sp,      $sp,        4
lw           $t3,    ($sp)
addiu        $sp,      $sp,        4
lw           $t2,    ($sp)
addiu        $sp,      $sp,        4
lw           $t1,    ($sp)
addiu        $sp,      $sp,        4
lw           $t0,    ($sp)
.end_macro

.macro SAVE_SPILL_MEM
# brace yourself for a long, unrolled loop...
lw           $a3, SPILL_MEMORY
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 4
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 8
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 12
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 16
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 20
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 24
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 28
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 32
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 36
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 40
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 44
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 48
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 52
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 56
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
lw           $a3, SPILL_MEMORY + 60
sw           $a3,    ($sp)
subiu        $sp,      $sp,        4
.end_macro

.macro RESTORE_SPILL_MEM
# brace yourself for a long, unrolled loop...
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 60
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 56
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 52
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 48
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 44
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 40
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 36
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 32
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 28
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 24
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 20
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 16
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 12
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 8
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY + 4
addiu        $sp,      $sp,        4
lw           $a3,    ($sp)
sw           $a3, SPILL_MEMORY
.end_macro

.macro CALLEE_FUNCTION_PROLOGUE (%variable_size)
# set $fp to the proper spot by recovering the value from $a0
add          $fp,      $a0,    $zero
# allocate stack space for variables ($sp = $sp - space for variables)
li           $a0,        4
mulu         $a1,      $a0, %variable_size
sub          $sp,      $sp,      $a1
.end_macro

.macro CALLEE_FUNCTION_EPILOGUE
# de-allocate the memory used for local variables and parameters
add          $sp,      $fp,    $zero
# jump back to the caller
jr           $ra
.end_macro

.macro CALLER_FUNCTION_PROLOGUE
# caller should save it's own $ra, $fp, and registers
sw           $ra,    ($sp)
subiu        $sp,      $sp,        4
sw           $fp,    ($sp)
subiu        $sp,      $sp,        4
# caller pushes registers and spill memory onto the stack as well
SAVE_T_REGISTERS()
SAVE_SPILL_MEM()
# save the value of $sp here into $a0 as temporary storage until the arguments are moved
# $fp needs to stay where it's at while the arguments are copied after this macro
add          $a0,      $sp,    $zero
.end_macro

.macro CALLER_FUNCTION_EPILOGUE
# recover the spill memory and the stored registers
RESTORE_SPILL_MEM()
RESTORE_T_REGISTERS()
# recover the caller's $fp and $ra
addiu        $sp,      $sp,        4
lw           $fp,    ($sp)
addiu        $sp,      $sp,        4
lw           $ra,    ($sp)
.end_macro

.data
SPILL_MEMORY: .space 64
N_ITEMS: .word 5
.text
add          $fp,      $sp,    $zero
add          $a0,      $fp,    $zero
jal         main
j       PROG_END
main:
CALLEE_FUNCTION_PROLOGUE(8)
li           $t0,        0
mulu         $t0,      $t0,        4
la           $t1,  12($fp)
la           $t2,  32($fp)
add          $t0,      $t0,      $t1
tlt          $t0,      $t1
tge          $t0,      $t2
li           $t2,        5
sw           $t2,    ($t0)
li           $t2,        1
mulu         $t2,      $t2,        4
la           $t0,  12($fp)
la           $t1,  32($fp)
add          $t2,      $t2,      $t0
tlt          $t2,      $t0
tge          $t2,      $t1
li           $t1,        1
sw           $t1,    ($t2)
li           $t1,        2
mulu         $t1,      $t1,        4
la           $t2,  12($fp)
la           $t0,  32($fp)
add          $t1,      $t1,      $t2
tlt          $t1,      $t2
tge          $t1,      $t0
li           $t0,        4
sw           $t0,    ($t1)
li           $t0,        3
mulu         $t0,      $t0,        4
la           $t1,  12($fp)
la           $t2,  32($fp)
add          $t0,      $t0,      $t1
tlt          $t0,      $t1
tge          $t0,      $t2
li           $t2,        3
sw           $t2,    ($t0)
li           $t2,        4
mulu         $t2,      $t2,        4
la           $t0,  12($fp)
la           $t1,  32($fp)
add          $t2,      $t2,      $t0
tlt          $t2,      $t0
tge          $t2,      $t1
li           $t1,        2
sw           $t1,    ($t2)
CALLER_FUNCTION_PROLOGUE()
li           $t1,        0
mulu         $t1,      $t1,        4
la           $t2,  12($fp)
la           $t0,  32($fp)
add          $t1,      $t1,      $t2
tlt          $t1,      $t2
tge          $t1,      $t0
lw           $t1,    ($t1)
sw           $t1,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t0,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t0,        1
mulu         $t0,      $t0,        4
la           $t2,  12($fp)
la           $t3,  32($fp)
add          $t0,      $t0,      $t2
tlt          $t0,      $t2
tge          $t0,      $t3
lw           $t0,    ($t0)
sw           $t0,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t3,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t3,        2
mulu         $t3,      $t3,        4
la           $t2,  12($fp)
la           $t4,  32($fp)
add          $t3,      $t3,      $t2
tlt          $t3,      $t2
tge          $t3,      $t4
lw           $t3,    ($t3)
sw           $t3,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t4,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t4,        3
mulu         $t4,      $t4,        4
la           $t2,  12($fp)
la           $t5,  32($fp)
add          $t4,      $t4,      $t2
tlt          $t4,      $t2
tge          $t4,      $t5
lw           $t4,    ($t4)
sw           $t4,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t5,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t5,        4
mulu         $t5,      $t5,        4
la           $t2,  12($fp)
la           $t6,  32($fp)
add          $t5,      $t5,      $t2
tlt          $t5,      $t2
tge          $t5,      $t6
lw           $t5,    ($t5)
sw           $t5,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t6,      $v0,    $zero
la           $t6,    ($fp)
li           $t2,        0
sw           $t2,    ($t6)
LOOP_CONDITION_00004:
lw           $t2,    ($fp)
lw           $t6,  N_ITEMS
slt          $t7,      $t2,      $t6
bne          $t7,    $zero, LOOP_BODY_00004
j       LOOP_EXIT_00004
LOOP_BODY_00004:
la           $t6,  -4($fp)
lw           $t2,    ($fp)
sw           $t2,    ($t6)
LOOP_CONDITION_00005:
lw           $t2,  -4($fp)
lw           $t6,  N_ITEMS
slt          $t8,      $t2,      $t6
bne          $t8,    $zero, LOOP_BODY_00005
j       LOOP_EXIT_00005
LOOP_BODY_00005:
lw           $t6,    ($fp)
mulu         $t6,      $t6,        4
la           $t2,  12($fp)
la           $t9,  32($fp)
add          $t6,      $t6,      $t2
tlt          $t6,      $t2
tge          $t6,      $t9
lw           $t6,    ($t6)
lw           $t9,  -4($fp)
mulu         $t9,      $t9,        4
la           $t2,  12($fp)
sw           $t1, SPILL_MEMORY
la           $t1,  32($fp)
add          $t9,      $t9,      $t2
tlt          $t9,      $t2
tge          $t9,      $t1
lw           $t9,    ($t9)
slt          $t1,      $t6,      $t9
bne          $t1,    $zero, IF_TRUE_00000
IF_FALSE_00000:
j       ENDIF_00000
IF_TRUE_00000:
la           $t9,  -8($fp)
lw           $t6,    ($fp)
mulu         $t6,      $t6,        4
la           $t2,  12($fp)
sw           $t0, SPILL_MEMORY + 4
la           $t0,  32($fp)
add          $t6,      $t6,      $t2
tlt          $t6,      $t2
tge          $t6,      $t0
lw           $t6,    ($t6)
sw           $t6,    ($t9)
lw           $t6,    ($fp)
mulu         $t6,      $t6,        4
la           $t9,  12($fp)
la           $t0,  32($fp)
add          $t6,      $t6,      $t9
tlt          $t6,      $t9
tge          $t6,      $t0
lw           $t0,  -4($fp)
mulu         $t0,      $t0,        4
la           $t9,  12($fp)
la           $t2,  32($fp)
add          $t0,      $t0,      $t9
tlt          $t0,      $t9
tge          $t0,      $t2
lw           $t0,    ($t0)
sw           $t0,    ($t6)
lw           $t0,  -4($fp)
mulu         $t0,      $t0,        4
la           $t6,  12($fp)
la           $t2,  32($fp)
add          $t0,      $t0,      $t6
tlt          $t0,      $t6
tge          $t0,      $t2
lw           $t2,  -8($fp)
sw           $t2,    ($t0)
ENDIF_00000:
la           $t1,  -4($fp)
lw           $t2,    ($t1)
add          $t0,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t1)
j       LOOP_CONDITION_00005
LOOP_EXIT_00005:
la           $t0,    ($fp)
lw           $t2,    ($t0)
add          $t1,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t0)
j       LOOP_CONDITION_00004
LOOP_EXIT_00004:
CALLER_FUNCTION_PROLOGUE()
li           $t1,        0
mulu         $t1,      $t1,        4
la           $t2,  12($fp)
la           $t0,  32($fp)
add          $t1,      $t1,      $t2
tlt          $t1,      $t2
tge          $t1,      $t0
lw           $t1,    ($t1)
sw           $t1,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t0,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t0,        1
mulu         $t0,      $t0,        4
la           $t2,  12($fp)
la           $t6,  32($fp)
add          $t0,      $t0,      $t2
tlt          $t0,      $t2
tge          $t0,      $t6
lw           $t0,    ($t0)
sw           $t0,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t6,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t6,        2
mulu         $t6,      $t6,        4
la           $t2,  12($fp)
la           $t9,  32($fp)
add          $t6,      $t6,      $t2
tlt          $t6,      $t2
tge          $t6,      $t9
lw           $t6,    ($t6)
sw           $t6,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t9,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t9,        3
mulu         $t9,      $t9,        4
la           $t2,  12($fp)
sw           $t3, SPILL_MEMORY + 8
la           $t3,  32($fp)
add          $t9,      $t9,      $t2
tlt          $t9,      $t2
tge          $t9,      $t3
lw           $t9,    ($t9)
sw           $t9,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t3,      $v0,    $zero
CALLER_FUNCTION_PROLOGUE()
li           $t3,        4
mulu         $t3,      $t3,        4
la           $t2,  12($fp)
sw           $t4, SPILL_MEMORY + 12
la           $t4,  32($fp)
add          $t3,      $t3,      $t2
tlt          $t3,      $t2
tge          $t3,      $t4
lw           $t3,    ($t3)
sw           $t3,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t4,      $v0,    $zero
li           $t4,        0
add          $v0,      $t4,    $zero
CALLEE_FUNCTION_EPILOGUE()
CALLEE_FUNCTION_EPILOGUE()
print_int:
CALLEE_FUNCTION_PROLOGUE(0)
# load $v0 with the value for the print int syscall
li           $v0,        1
# the first (and only) argument is the value to print
lw           $a0,    ($fp)
syscall 
# print a newline character for readability
# 0x0D is CR or '\r' - 0x0A is LF for '\n'
li           $v0,       11
li           $a0,       10
syscall 
CALLEE_FUNCTION_EPILOGUE()
print_string:
CALLEE_FUNCTION_PROLOGUE(0)
# load $v0 with the value for the print int syscall
li           $v0,        4
# the first (and only) argument is the base address of the null terminated ascii string
la           $a0,    ($fp)
syscall 
CALLEE_FUNCTION_EPILOGUE()
print_float:
CALLEE_FUNCTION_PROLOGUE(0)
# load $v0 with the value for the print int syscall
li           $v0,        2
# the first (and only) argument is the base address of the null terminated ascii string
lwc1        $f12,    ($fp)
syscall 
CALLEE_FUNCTION_EPILOGUE()
PROG_END: