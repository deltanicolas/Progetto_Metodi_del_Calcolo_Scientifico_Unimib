#!/usr/bin/env python3

import sys
import os
import argparser
import utility
import solvers


if __name__ == '__main__':

    args = vars(argparser.parse_arguments())

    A = utility.load_matrix(args['file'])
    x_exact, b = utility.setup_system(A)
    solver = solvers.MatSolvers(A, b, args['tolerance'])
    utility.plot_sparsity(A, matrix_name=args['file'].stem)  #.stem is used to get filename without extension
    #TODO For each solver method print result
