from greenery import fsm, lego
import re
import sys

A, B, C = range(3)
a, b = '0', '1'

# create the FSM
machine = fsm.fsm(
    alphabet = {a, b},
    states   = {A, B, C},
    initial  = A,
    finals   = {A},
    map      = {
            A : {a: A, b: B},
            B : {a: C, b: A},
            C : {a: B, b: C},

    },
)

# convert it to regex
rex = lego.from_fsm(machine)
print(rex)


for line in sys.stdin:
    line = line.strip()
    if re.fullmatch(r"(0|1(01*0)*1)*", line):
        print(line)
