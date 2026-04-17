import argparse
from html import parser
import os
import pathlib


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Progetto Metodi del Calcolo Scientifico - Unimib" \
        " - Linear System Solvers for SPD Matrices",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Solvers: Jacobi, Gauss-Seidel, Gradient, and Conjugate Gradient."
    )
    parser.add_argument('-f', '--file', type=check_mtx, required=True,
                        help="Path to the Symmetric Positive Definite matrix in .mtx format")
    parser.add_argument('-t', '--tolerance', type=check_tolerance, required=True,
                        help="Relative residual tolerance for the stopping criterion: ||Ax-b||/||b|| < tol",
                        default=1e-6)
    parser.add_argument('-s', '--solver', type=check_solver, required=False,
                        choices=[0, 1, 2, 3, 4], 
                        default=0,
                        help="Solver method to run: 0=run all, 1=Jacobi, 2=Gauss-Seidel, 3=Gradient, 4=Conjugate Gradient")
    return parser.parse_args()



def check_tolerance(value) -> float:
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{value}' is not a valid value. The tolerance must be a numeric value "
            "(e.g., 0.000001 or 1e-6)."
        )
    if not fvalue > 0:
        raise argparse.ArgumentTypeError(
            f"Tolerance value {value} must be a positive number."
        )
    return fvalue


def check_mtx(value) -> pathlib.Path:
    path = pathlib.Path(value)
    if not path.is_file() or not str(path).endswith('.mtx'):
        raise argparse.ArgumentTypeError(f"{value} the file does not exist or is not a .mtx file.")
    return path

def check_solver(value) -> int:
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{value}' not a valid integer. Solver ID must be an integer (0, 1, 2, 3, or 4)."
        )
    if ivalue not in [0, 1, 2, 3, 4]:
        raise argparse.ArgumentTypeError(
            f"ID {value} is not valid. Solver ID must be 0 (all), 1 (Jacobi), 2 (Gauss-Seidel), 3 (Gradient), or 4 (Conjugate Gradient)."
        )
    return ivalue