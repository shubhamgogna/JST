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
ARRAY_DIM: .word 2
.text
add          $fp,      $sp,    $zero
add          $a0,      $fp,    $zero
jal         main
j       PROG_END
main:
CALLEE_FUNCTION_PROLOGUE(16)
la           $t0,    ($fp)
li           $t1,        0
sw           $t1,    ($t0)
LOOP_CONDITION_00011:
lw           $t1,    ($fp)
lw           $t0, ARRAY_DIM
slt          $t2,      $t1,      $t0
bne          $t2,    $zero, LOOP_BODY_00011
j       LOOP_EXIT_00011
LOOP_BODY_00011:
la           $t0,  -4($fp)
li           $t1,        0
sw           $t1,    ($t0)
LOOP_CONDITION_00012:
lw           $t1,  -4($fp)
lw           $t0, ARRAY_DIM
slt          $t3,      $t1,      $t0
bne          $t3,    $zero, LOOP_BODY_00012
j       LOOP_EXIT_00012
LOOP_BODY_00012:
lw           $t0,    ($fp)
mulu         $t0,      $t0,        2
lw           $t1,  -4($fp)
addu         $t0,      $t0,      $t1
mulu         $t0,      $t0,        4
la           $t1,  16($fp)
la           $t4,  32($fp)
add          $t0,      $t0,      $t1
tlt          $t0,      $t1
tge          $t0,      $t4
lw           $t4,    ($fp)
mulu         $t4,      $t4,        2
lw           $t1,  -4($fp)
addu         $t4,      $t4,      $t1
mulu         $t4,      $t4,        4
la           $t1,  32($fp)
la           $t5,  48($fp)
add          $t4,      $t4,      $t1
tlt          $t4,      $t1
tge          $t4,      $t5
li           $t5,        2
sw           $t5,    ($t4)
sw           $t5,    ($t0)
la           $t5,  -4($fp)
lw           $t0,    ($t5)
add          $t4,      $t0,    $zero
addiu        $t0,      $t0,        1
sw           $t0,    ($t5)
j       LOOP_CONDITION_00012
LOOP_EXIT_00012:
la           $t4,    ($fp)
lw           $t0,    ($t4)
add          $t5,      $t0,    $zero
addiu        $t0,      $t0,        1
sw           $t0,    ($t4)
j       LOOP_CONDITION_00011
LOOP_EXIT_00011:
la           $t5,    ($fp)
li           $t0,        0
sw           $t0,    ($t5)
LOOP_CONDITION_00013:
lw           $t0,    ($fp)
lw           $t5, ARRAY_DIM
slt          $t4,      $t0,      $t5
bne          $t4,    $zero, LOOP_BODY_00013
j       LOOP_EXIT_00013
LOOP_BODY_00013:
la           $t5,  -4($fp)
li           $t0,        0
sw           $t0,    ($t5)
LOOP_CONDITION_00014:
lw           $t0,  -4($fp)
lw           $t5, ARRAY_DIM
slt          $t1,      $t0,      $t5
bne          $t1,    $zero, LOOP_BODY_00014
j       LOOP_EXIT_00014
LOOP_BODY_00014:
la           $t5, -12($fp)
li           $t0,        0
sw           $t0,    ($t5)
la           $t0,  -8($fp)
li           $t5,        0
sw           $t5,    ($t0)
LOOP_CONDITION_00015:
lw           $t5,  -8($fp)
lw           $t0, ARRAY_DIM
slt          $t6,      $t5,      $t0
bne          $t6,    $zero, LOOP_BODY_00015
j       LOOP_EXIT_00015
LOOP_BODY_00015:
la           $t0, -12($fp)
lw           $t5, -12($fp)
lw           $t7,    ($fp)
mulu         $t7,      $t7,        2
lw           $t8,  -8($fp)
addu         $t7,      $t7,      $t8
mulu         $t7,      $t7,        4
la           $t8,  16($fp)
la           $t9,  32($fp)
add          $t7,      $t7,      $t8
tlt          $t7,      $t8
tge          $t7,      $t9
lw           $t7,    ($t7)
lw           $t9,  -8($fp)
mulu         $t9,      $t9,        2
lw           $t8,  -4($fp)
addu         $t9,      $t9,      $t8
mulu         $t9,      $t9,        4
la           $t8,  32($fp)
sw           $t2, SPILL_MEMORY
la           $t2,  48($fp)
add          $t9,      $t9,      $t8
tlt          $t9,      $t8
tge          $t9,      $t2
lw           $t9,    ($t9)
mul          $t2,      $t7,      $t9
add          $t9,      $t5,      $t2
sw           $t9,    ($t0)
la           $t9,  -8($fp)
lw           $t0,    ($t9)
add          $t2,      $t0,    $zero
addiu        $t0,      $t0,        1
sw           $t0,    ($t9)
j       LOOP_CONDITION_00015
LOOP_EXIT_00015:
lw           $t2,    ($fp)
mulu         $t2,      $t2,        2
lw           $t0,  -4($fp)
addu         $t2,      $t2,      $t0
mulu         $t2,      $t2,        4
la           $t0,  48($fp)
la           $t9,  64($fp)
add          $t2,      $t2,      $t0
tlt          $t2,      $t0
tge          $t2,      $t9
lw           $t9, -12($fp)
sw           $t9,    ($t2)
la           $t9,  -4($fp)
lw           $t2,    ($t9)
add          $t0,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t9)
j       LOOP_CONDITION_00014
LOOP_EXIT_00014:
la           $t0,    ($fp)
lw           $t2,    ($t0)
add          $t9,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t0)
j       LOOP_CONDITION_00013
LOOP_EXIT_00013:
la           $t9,    ($fp)
li           $t2,        0
sw           $t2,    ($t9)
LOOP_CONDITION_00016:
lw           $t2,    ($fp)
lw           $t9, ARRAY_DIM
slt          $t0,      $t2,      $t9
bne          $t0,    $zero, LOOP_BODY_00016
j       LOOP_EXIT_00016
LOOP_BODY_00016:
la           $t9,  -4($fp)
li           $t2,        0
sw           $t2,    ($t9)
LOOP_CONDITION_00017:
lw           $t2,  -4($fp)
lw           $t9, ARRAY_DIM
slt          $t5,      $t2,      $t9
bne          $t5,    $zero, LOOP_BODY_00017
j       LOOP_EXIT_00017
LOOP_BODY_00017:
CALLER_FUNCTION_PROLOGUE()
lw           $t9,    ($fp)
mulu         $t9,      $t9,        2
lw           $t2,  -4($fp)
addu         $t9,      $t9,      $t2
mulu         $t9,      $t9,        4
la           $t2,  48($fp)
la           $t7,  64($fp)
add          $t9,      $t9,      $t2
tlt          $t9,      $t2
tge          $t9,      $t7
lw           $t9,    ($t9)
sw           $t9,    ($sp)
sub          $sp,      $sp,        4
jal     print_int
CALLER_FUNCTION_EPILOGUE()
add          $t7,      $v0,    $zero
la           $t7,  -4($fp)
lw           $t2,    ($t7)
add          $t8,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t7)
j       LOOP_CONDITION_00017
LOOP_EXIT_00017:
la           $t8,    ($fp)
lw           $t2,    ($t8)
add          $t7,      $t2,    $zero
addiu        $t2,      $t2,        1
sw           $t2,    ($t8)
j       LOOP_CONDITION_00016
LOOP_EXIT_00016:
li           $t7,        0
add          $v0,      $t7,    $zero
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