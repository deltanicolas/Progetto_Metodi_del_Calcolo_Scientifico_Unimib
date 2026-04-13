import numpy as np
from scipy.io import mmread
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

def load_matrix(filepath):
    """
    Carica una matrice in formato .mtx e la converte in formato CSR (Compressed Sparse Row).
    
    Args:
        filepath (str): Il percorso del file .mtx (es. 'Data/spa1.mtx').
        
    Returns:
        scipy.sparse.csr_matrix: La matrice sparsa caricata.
    """
    try:
        A_coo = mmread(filepath)
        A_csr = csr_matrix(A_coo)
        return A_csr
        
    except FileNotFoundError:
        print(f"Errore: Il file {filepath} non è stato trovato.")
        raise
    except Exception as e:
        print(f"Errore durante il caricamento della matrice: {e}")
        raise

def setup_system(A):
    """
    Costruisce il sistema lineare di test seguendo gli step 1 e 2 del progetto.
    
    Args:
        A (scipy.sparse.csr_matrix): La matrice dei coefficienti.
        
    Returns:
        tuple: (x_exact, b) dove x_exact è un vettore di 1 e b = A*x.
    """
    n = A.shape[0]
    x_exact = np.ones(n)
    b = A.dot(x_exact)
    
    return x_exact, b

def compute_relative_error(x_exact, x_approx):
    """
    Calcola l'errore relativo in norma 2 tra la soluzione esatta e quella computata.
    
    Args:
        x_exact (numpy.ndarray): Vettore della soluzione esatta.
        x_approx (numpy.ndarray): Vettore della soluzione approssimata dal solutore.
        
    Returns:
        float: L'errore relativo scalare.
    """
    # Errore = ||x_esatta - x_approssimata|| / ||x_esatta||
    norm_diff = np.linalg.norm(x_exact - x_approx)
    norm_exact = np.linalg.norm(x_exact)
    
    return norm_diff / norm_exact

def plot_sparsity(A, matrix_name="Matrice"):
    """
    Genera e salva un grafico <matrix_name>.png in Data/Plot rappressentante la sparsità della matrice.
    
    L'estetica del grafico viene adattata dinamicamente in base alla dimensione
    e alla densità della matrice per garantire la leggibilità.
    
    Args:
        A (scipy.sparse.csr_matrix): La matrice sparsa da visualizzare.
        matrix_name (str): Il nome della matrice usato per titolo e file.
        
    Returns:
        None
    """
    plt.figure(figsize=(10, 10))
    
    n_rows = A.shape[0]
    total_elements = A.shape[0] * A.shape[1]
    density = A.nnz / total_elements

    m_size = 500 / n_rows 
    m_size = max(0.001, min(m_size, 5.0))
  
    a_val = 1.0 if density < 0.05 else 0.4
    if n_rows > 5000: a_val = 0.2 

    plt.spy(A, markersize=m_size, color='blue', alpha=a_val)
    
    plt.title(f"Sparsity: {matrix_name}\nDim: {A.shape[0]}x{A.shape[1]} | NNZ: {A.nnz} | Densità: {density:.2%}")
    plt.xlabel("Colonne")
    plt.ylabel("Righe")
    
    clean_name = matrix_name.replace(".mtx", "")
    output_path = f"Data/Plot/{clean_name}_sparsity.png"
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Grafico ottimizzato ({n_rows}x{n_rows}) salvato in: {output_path}")


if __name__ == "__main__":
    test_file = "Data/spa1.mtx" 
    
    print(f"--- Test Utility ---")
    try:
        A = load_matrix(test_file)
        print(f"Matrice caricata: {test_file}")
        print(f"Dimensioni: {A.shape[0]}x{A.shape[1]}") # type: ignore
        print(f"Elementi diversi da zero (nnz): {A.nnz}")

        print("Generazione grafico di sparsità...")
        plot_sparsity(A, test_file.split("/")[-1])

  
        x_e, b = setup_system(A)
        print(f"Vettore b generato con successo. Dimensione: {len(b)}")

        x_fake = x_e + 1e-5 
        err = compute_relative_error(x_e, x_fake)
        print(f"Test Errore Relativo (dummy): {err:.2e}")
        
        print("\nUtility test passato!")

    except FileNotFoundError:
        print(f"\n[!] Errore: Assicurati che il file '{test_file}' sia nella cartella corretta.")
    except Exception as e:
        print(f"\n[!] Errore durante il test: {e}")