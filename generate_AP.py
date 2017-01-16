#!/usr/bin/env python3
import sys
import random
mode = "AP"


def AP_rand(mean, stdev):
    return random.randint(0, 19)

if len(sys.argv) != 4:
    print("Usage: %s <lp-file> <num-tasks> <num-objectives>" % (sys.argv[0]))
    sys.exit(-1)

n = int(sys.argv[2])
nObjectives = int(sys.argv[3])
with open(sys.argv[1], "w") as lpfile:
    lpfile.write("Minimize 0\ns.t.\n")
    for k in range(n):
        lpfile.write("X%dX%d\n" % (k+1, 1))
        for j in range(n-1):
            lpfile.write(" + X%dX%d\n" % (k+1, j+2))
        lpfile.write("= 1\n")
    for k in range(n):
        lpfile.write("X%dX%d\n" % (1, k+1))
        for j in range(n-1):
            lpfile.write(" + X%dX%d\n" % (j+2, k+1))
        lpfile.write("= 1\n")
    for k in range(nObjectives):
        first = True
        for j in range(n):
            for i in range(n):
                if not first:
                    lpfile.write(" + ")
                lpfile.write("%5d X%dX%d\n" % (AP_rand(9, 6), j+1, i+1))
                first = False
        lpfile.write("< %d\n" % (k+1))

    lpfile.write("BINARY\n")
    for k in range(n):
        for j in range(n):
            lpfile.write("X%dX%d\n" % (k+1, j+1))
    lpfile.write("END\n")
