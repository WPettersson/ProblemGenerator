#!/usr/bin/env python3
import sys
import random
mode = "TSP"


def TSP_rand(mean, stdev):
    return random.randint(mean-2*stdev, mean+2*stdev)


def main(lpname, num_cities, num_objectives):
    with open(lpname, "w") as lpfile:
        cities = [[(TSP_rand(100, 40), TSP_rand(100, 40))
                   for _ in range(num_cities)] for __ in range(num_objectives)]
        lpfile.write("Minimize 0\ns.t.\n")
        for j in range(num_cities):
            lpfile.write(" + ".join(["X%d_%d" % (i+1, j+1)
                                     for i in range(num_cities) if i != j]))
            lpfile.write(" = 1\n")
            lpfile.write(" + ".join(["X%d_%d" % (j+1, i+1)
                                     for i in range(num_cities) if i != j]))
            lpfile.write(" = 1\n")
        for i in range(num_cities):
            for j in range(num_cities):
                if i == j:
                    continue
                lpfile.write("U%d - U%d + %d X%d_%d < %d\n" %
                             (i+1, j+1, num_cities, i+1, j+1, num_cities))
        for k in range(num_objectives):
            first = True
            for i in range(num_cities):
                for j in range(i, num_cities):
                    if i == j:
                        continue
                    if not first:
                        lpfile.write(" + ")
                    displacement = (cities[k][i][0] - cities[k][j][0],
                                    cities[k][i][1] - cities[k][j][1])
                    distance = (displacement[0]**2 + displacement[1]**2)**0.5
                    lpfile.write("%5d X%d_%d\n" % (distance, j+1, i+1))
                    first = False
                    lpfile.write(" + ")
                    lpfile.write("%5d X%d_%d\n" % (distance, i+1, j+1))
            lpfile.write("< %d\n" % (k+1))

        lpfile.write("GENERAL\n")
        for i in range(num_cities):
            lpfile.write("U%d\n" % (i+1))
        lpfile.write("BINARY\n")
        for i in range(num_cities):
            for j in range(num_cities):
                if i == j:
                    continue
                lpfile.write("X%d_%d\n" % (i+1, j+1))
        lpfile.write("END\n")


if len(sys.argv) != 4:
    print("Usage: %s <lp-file> <num-cities> <num-objectives>" % (sys.argv[0]))
    sys.exit(-1)
else:
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
