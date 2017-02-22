#!/usr/bin/env python3
import sys
import random
mode = "TSP"


def TSP_rand(mean, stdev):
    return random.randint(mean-2*stdev, mean+2*stdev)

if len(sys.argv) != 4:
    print("Usage: %s <lp-file> <num-cities> <num-objectives>" % (sys.argv[0]))
    sys.exit(-1)

nCities = int(sys.argv[2])
nObjectives = int(sys.argv[3])
with open(sys.argv[1], "w") as lpfile:
    lpfile.write("Minimize 0\ns.t.\n")
    for j in range(nCities):
        lpfile.write("X%d_%d\n" % (1, j+1))
        for i in range(nCities):
            if i == j:
                continue
            lpfile.write(" + X%d_%d\n" % (i+1, j+1))
        lpfile.write("= 1\n")
    for i in range(nCities):
        lpfile.write("X%d_%d\n" % (i+1, 1))
        for j in range(nCities):
            if i == j:
                continue
            lpfile.write(" + X%d_%d\n" % (i+1, j+1))
        lpfile.write("= 1\n")
    for i in range(nCities):
        for j in range(nCities):
            if i == j:
                continue
            lpfile.write("U%d - U%d + %d X%d_%d < %d\n" %
                         (i+1, j+1, nCities, i+1, j+1, nCities))
    for k in range(nObjectives):
        first = True
        for i in range(nCities):
            for j in range(i, nCities):
                if i == j:
                    continue
                if not first:
                    lpfile.write(" + ")
                w = TSP_rand(100, 40)
                lpfile.write("%5d X%d_%d\n" % (w, j+1, i+1))
                first = False
                lpfile.write(" + ")
                lpfile.write("%5d X%d_%d\n" % (w, i+1, j+1))
        lpfile.write("< %d\n" % (k+1))

    lpfile.write("GENERAL\n")
    for i in range(nCities):
        lpfile.write("U%d\n" % (i+1))
    lpfile.write("BINARY\n")
    for i in range(nCities):
        for j in range(nCities):
            if i == j:
                continue
            lpfile.write("X%d_%d\n" % (i+1, j+1))
    lpfile.write("END\n")
