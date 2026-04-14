#!/usr/bin/env python3

import sys
import os

import utility
import solvers


def main(argv, argc):
    if argc < 3:
        print(f'Usage: {argv[0]} <mmx file> <tolerance>')
        return -1

    # Check if tolerance is integer
    try:
        tolerance = float(argv[2])
    except ValueError:
        print('Specify float value for tolerance')
        return -1

    #m = mmread(argv[1], spmatrix=True)
    #array_mat = m.toarray()

    m = utility.load_matrix(argv[1]).toarray()
    x_exact, b = utility.setup_system(m)
    
    solver = solvers.MatSolvers(m,b, tolerance)

    #TODO For each solver method print result
    

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))