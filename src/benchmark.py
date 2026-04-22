import csv
import os
from pathlib import Path
from test import run_specific_test

def run_benchmark():
    data_dir = Path("../Data")
    matrices = sorted(list(data_dir.glob("*.mtx")))
    solvers = ["jacobi", "gs", "grad", "cg"]
    tolerances = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
    output_file = "../Data/benchmark_results.csv"

    fieldnames = ["matrix", "solver", "tolerance", "iter", "time", "conv", "error"]
    
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for mat in matrices:
            print(f"\n📂 Analizzando: {mat.name}")
            for s in solvers:
                for tol in tolerances:
                    try:
                        print(f"  > {s:<7} | tol: {tol:.1e}", end="\r")
                        res = run_specific_test(str(mat), s, tol)
                        
                        writer.writerow({
                            "matrix": mat.name,
                            "solver": s,
                            "tolerance": tol,
                            "iter": res["iterations"],
                            "time": res["time"],
                            "conv": res["converged"],
                            "error": res["error"]
                        })
                        f.flush()
                    except Exception as e:
                        print(f"\n  [!] Errore {s} su {mat.name}: {e}")

    print(f"\n\n✅ Benchmark completato! Dati salvati in {output_file}")

if __name__ == "__main__":
    run_benchmark()