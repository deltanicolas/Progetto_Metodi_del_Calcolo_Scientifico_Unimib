# Mini Libreria per Sistemi Lineari - Metodi per il Calcolo Scientifico

Progetto per il corso di **Metodi per il Calcolo Scientifico** (AA 2025-2026) presso Unimib.  
L'obiettivo è l'implementazione e la validazione di solutori iterativi per sistemi lineari con matrici simmetriche e definite positive (SPD).

## 🚀 Caratteristiche
Il cuore del progetto è contenuto nella libreria `solvers.py`, la quale implementa i seguenti metodi iterativi partendo da un vettore iniziale nullo ($x^{(0)} = 0$):
* **Jacobi**
* **Gauss-Seidel**
* **Gradiente**
* **Gradiente Coniugato**

## 🛠️ Requisiti e Installazione
* **Linguaggio:** Python
* **Gestione Dati:** NumPy / SciPy 
* **Plot dei Grafici:** Matplotlib

Tutte le dipendenze necessarie sono specificate nel file `requirements.txt`. Puoi installarle comodamente tramite `pip` eseguendo questo comando nel tuo terminale:

```bash
pip install -r requirements.txt
```

## 💻 Utilizzo da Riga di Comando
Oltre alla libreria `solvers.py`, il progetto espone un'interfaccia a riga di comando tramite il file `main.py` per eseguire e testare i solutori in modo rapido.

**Sintassi di base:**
```bash
python main.py -f FILE -t TOLERANCE [-s {0,1,2,3,4}]
```

**Argomenti disponibili:**
* `-f`, `--file` : Percorso del file contenente la matrice SPD in formato `.mtx` **(obbligatorio)**.
* `-t`, `--tolerance`: Tolleranza sul residuo relativo per il criterio di arresto (||Ax-b||/||b|| < tol) **(obbligatorio)**.
* `-s`, `--solver` : Metodo risolutivo da eseguire **(opzionale, default: 0)**. 
  * `0` = Esegui tutti i solutori
  * `1` = Jacobi
  * `2` = Gauss-Seidel
  * `3` = Gradiente
  * `4` = Gradiente Coniugato

**Esempio di utilizzo:**
```bash
python main.py -f spa1.mtx -t 1e-6 -s 4
```
*(Questo comando eseguirà il Gradiente Coniugato sulla matrice spa1.mtx con una tolleranza di 1e-6)*

## 📂 Dataset
La libreria è testata sulle matrici sparse fornite per il progetto:
* `spa1.mtx`, `spa2.mtx`
* `vem1.mtx`, `vem2.mtx`

---
**Autori:** 
- Nicolas Chines (899536)
- Jacopo Borgato (866305)