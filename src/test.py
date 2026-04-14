from utility import load_matrix, setup_system, compute_relative_error
from solvers import MatSolvers


def run_specific_test(matrix_name, method_name, tol):
    path = f"Data/{matrix_name}.mtx"
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
        print(f"Metodo {method_name} non trovato.")
        return

    print(f"\nEseguendo {method_name.upper()} su {matrix_name} (tol: {tol})")
    x_c, it, conv, dt = methods[method_name]()
    err = compute_relative_error(x_exact, x_c)
    
    print(f"-> Iter: {it} | Tempo: {dt:.4f}s | Conv: {conv} | Err: {err:.2e}")


if __name__ == "__main__":
    run_specific_test("spa2", "jacobi", 1e-10)
