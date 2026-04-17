#!/usr/bin/env python3

import argparser
from test import run_specific_test


def main():

    args = vars(argparser.parse_arguments())
    
    solver_map = {
        1: 'jacobi',
        2: 'gs',
        3: 'grad',
        4: 'cg'
    }
    if args['solver'] == 0:
        solvers_to_run = list(solver_map.values())
    else:
        solvers_to_run = [solver_map[args['solver']]]
        
    for solver_name in solvers_to_run:
        run_specific_test(args['file'], solver_name, args['tolerance'])


if __name__ == '__main__':
    main()