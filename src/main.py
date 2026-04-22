#!/usr/bin/env python3

import traceback

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
        
    print(f"\n{'='*50}")
    print(f" PROGETTO MCS - Solutori iterativi per Sistemi Lineari - UNIMIB")
    print(f" File: {args['file']}")
    print(f" Tolleranza: {args['tolerance']}")
    print(f"{'='*50}")

    for solver_name in solvers_to_run:
        try:
            res = run_specific_test(args['file'], solver_name, args['tolerance'])
 
            print(f"\n> METODO: {solver_name.upper()}")
            print(f"  - Iterazioni:  {res['iterations']}")
            print(f"  - Tempo:       {res['time']:.4f} s")
            print(f"  - Convergenza: {"True" if res['converged'] else 'False'}")
            print(f"  - Errore Rel:  {res['error']:.2e}")
            
        except Exception as e:
            print(f"\n[!] Errore durante l'esecuzione di {solver_name.upper()}:")
            print(f"    {e}")

    print(f"\n{'='*50}\n")


if __name__ == '__main__':
    main()