from utility import load_matrix, setup_system, compute_relative_error
from solvers import MatSolvers
import numpy as np

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
        print(f"Metodo {method_name} non trovato.")
        return

    print(f"\nEseguendo {method_name.upper()} su {path.stem} (tol: {tol})")
    x_c, it, conv, dt = methods[method_name]()
    err = compute_relative_error(x_exact, x_c)

   # print("\nCONFRONTO VETTORI (Soluzione Esatta vs Calcolata):")
   # print(f"{'Indice':<8} | {'x_esatta':<12} | {'x_calcolata':<18}")
   # print("-" * 45)
   # for i in range(len(x_exact)):
   #     print(f"{i:<8} | {x_exact[i]:<12.1f} | {x_c[i]:<18.15f}")
   # print("-" * 45)  
   #------    The above printout is for debugging and comparison purposes.      -------- 
   #-------It shows the exact solution vs the computed solution for each index. --------
        
    print(f"-> Iter: {it} | Tempo: {dt:.4f}s | Conv: {conv} | Err: {err:.2e}")
    


if __name__ == "__main__":
    run_specific_test("../Data/spa1.mtx", "jacobi", 1e-8)
