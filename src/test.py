from utility import load_matrix, setup_system, compute_relative_error
from solvers import MatSolvers


def run_specific_test(path, method_name, tol):
    A = load_matrix(path)
    x_exact, b = setup_system(A)
    
    solver = MatSolvers(A, b, tol)

    methods = {
        "jacobi": solver.jacobi,
        "gs": solver.gauss_seidel,
        "grad": solver.gradient,
        "cg": solver.gradient_conjugate
    }
    
    if method_name not in methods:
        raise ValueError(f"Metodo {method_name} non trovato.")

    x_c, it, conv, dt = methods[method_name]()
    err = compute_relative_error(x_exact, x_c)

    return {
        "iterations": it,
        "time": dt,
        "converged": conv,
        "error": err,
        "x_sol": x_c
    }

if __name__ == "__main__":

    res = run_specific_test("../Data/spa1.mtx", "grad", 1e-10)
    print(f"Risultato: {res['iterations']} iterazioni in {res['time']:.4f}s")