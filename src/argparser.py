import argparse
import os
import pathlib


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Progetto Metodi del Calcolo Scientifico - Unimib",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-f', '--file', type=check_mtx, required=True,
                        help="Path to the .mtx file")
    parser.add_argument('-t', '--tolerance', type=check_tolerance,
                        help="The tolerance threshold, Default is 1e-6",
                        default=1e-6)
    return parser.parse_args()



def check_tolerance(value) -> float:
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"'{value}' is not a valid number. The tolerance must be a numeric value "
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
        raise argparse.ArgumentTypeError(f"{value} is not a valid .mtx file.")
    return path
