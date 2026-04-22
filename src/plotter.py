import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter, ScalarFormatter
from pathlib import Path

def generate_plots(csv_file="../Data/benchmark_results.csv"):
    if not os.path.exists(csv_file):
        print("Errore: file CSV non trovato!")
        return

    df = pd.read_csv(csv_file)
    matrices = df["matrix"].unique()
    
    output_path = Path("../Data/Plot")
    output_path.mkdir(parents=True, exist_ok=True)

    plt.style.use('seaborn-v0_8-muted') 

    for mat in matrices:
        mat_df = df[df["matrix"] == mat]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
        fig.suptitle(f'Analisi Performance Matrice: {Path(mat).stem}', fontsize=16, fontweight='bold')

        for solver in mat_df["solver"].unique():
            solver_df = mat_df[mat_df["solver"] == solver].sort_values("tolerance", ascending=False)
            
            # --- Grafico 1: Tempo  /  Tolleranza ---
            ax1.plot(solver_df["tolerance"], solver_df["time"] * 1000, 
                     marker='o', markersize=8, linewidth=2, label=solver.upper())
            
            # --- Grafico 2: Iterazioni / Tolleranza ---
            ax2.plot(solver_df["tolerance"], solver_df["iter"], 
                     marker='s', markersize=8, linewidth=2, label=solver.upper())

        for ax in [ax1, ax2]:
            ax.set_xscale('log')
            ax.invert_xaxis() 
            ax.set_xlabel('Tolleranza ($10^{-k}$)', fontsize=12)
            ax.grid(True, which="both", ls=":", alpha=0.6)
            ax.legend(frameon=True, loc='best')

        ax1.set_yscale('log')
        ax1.set_ylabel('Tempo di calcolo (ms)', fontsize=12, fontweight='bold')
        ax1.set_title('Efficienza Temporale', color='#2c3e50')
        ax1.yaxis.set_major_formatter(ScalarFormatter()) 

        ax2.set_ylabel('Numero di Iterazioni', fontsize=12, fontweight='bold')
        ax2.set_title('Velocità di Convergenza', color='#2c3e50')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        save_name = output_path / f"analysis_{Path(mat).stem}.png"
        plt.savefig(save_name, dpi=300)
        plt.close()

    print(f"✅ Analisi completata! Grafici salvati in: {output_path.absolute()}")

if __name__ == "__main__":
    generate_plots()