# This file is part of JST.
#
# JST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

# General
DUP = 'DUP'
SOURCE = 'SOURCE'
KICK = 'KICK'

# Program Sections
DATA = 'DATA'
TEXT = 'TEXT'

# Math Operations
# TODO: create versions for both int and floating point?
ADD = 'ADD'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'
MOD = 'MOD'
NEG = 'NEG'

ADDI = 'ADDI'
SUBI = 'SUBI'
MULI = 'MULI'
DIVI = 'DIVI'

ADDU = 'ADDU'
SUBU = 'SUBU'
MULU = 'MULU'
DIVU = 'DIVU'
MODU = 'MODU'
NEGU = 'NEGU'

ADDIU = 'ADDIU'
SUBIU = 'SUBIU'
MULIU = 'MULIU'
DIVIU = 'DIVIU'

ADDS = 'ADDS'
SUBS = 'SUBS'
MULS = 'MULS'
DIVS = 'DIVS'
NEGS = 'NEGS'

# Logical Operations
# These won't correspond directly to MIPS instructions, but it seems like good practice to have them in the 3AC for
# decoupling the instruction from assembly.
LAND = 'LAND'
LOR = 'LOR'

NOT = 'NOT'
EQ = 'EQ'
NE = 'NE'
GT = 'GT'
GE = 'GE'
LT = 'LT'
LE = 'LE'

# Casting
CVTSW = 'CVTSW'
CVTWS = 'CVTWS'

# Assignment
ASSIGN = 'ASSIGN'

# Memory Accesses
LOAD = 'LOAD'
STORE = 'STORE'
LA = 'LA'
LI = 'LI'

# Control Flow
LABEL = 'LABEL'
JAL = 'JAL'
JR = 'JR'
BR = 'BR'
BREQ = 'BREQ'
BRGT = 'BRGT'
BRLT = 'BRLT'
BRGE = 'BRGE'
BRLE = 'BRLE'
BRNE = 'BRNE'
HALT = 'HALT'

# Procedure/Function Call
ARGS = 'ARGS'
REFOUT = 'REFOUT'
VALOUT = 'VALOUT'
CALL_PROC = 'CALL_PROC'
BEGIN_PROC = 'BEGIN_PROC'
END_PROC = 'END_PROC'

PROCENTRY = 'PROCENTRY'
ENDPROC = 'ENDPROC'
RETURN = 'RETURN'

# Miscellaneous
BOUND = 'BOUND'
ADDR = 'ADDR'
GLOBAL = 'GLOBAL'
STRING = 'STRING'
COMMENT = 'COMMENT'

# Library
PRNTI = 'PRNTI'
PRNTF = 'PRNTF'
PRNTS = 'PRNTS'

READI = 'READI'
READF = 'READF'
READS = 'READS'
