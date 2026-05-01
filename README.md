# Mini Libreria per Sistemi Lineari - Metodi per il Calcolo Scientifico

Progetto per il corso di **Metodi per il Calcolo Scientifico** (AA 2025-2026) presso Unimib.
L'obiettivo è l'implementazione e la validazione di solutori iterativi per sistemi lineari con matrici simmetriche e definite positive (SPD).

---

## 🚀 Caratteristiche

Il cuore del progetto è contenuto nella libreria `solvers.py`, la quale implementa i seguenti metodi iterativi partendo da un vettore iniziale nullo ($x^{(0)} = 0$):

* **Jacobi**
* **Gauss-Seidel**
* **Gradiente**
* **Gradiente Coniugato**

---

## 🛠️ Requisiti e Installazione

* **Linguaggio:** Python
* **Gestione Dati:** NumPy / SciPy
* **Plot dei Grafici:** Matplotlib
* **Gestione file CSV:** Pandas
* **Interfaccia TUI:** Textual

Tutte le dipendenze necessarie sono specificate nel file `requirements.txt`.
Puoi installarle eseguendo:

```bash
pip install -r requirements.txt
```

---

## 💻 Utilizzo da Riga di Comando (CLI)

Il file `main.py` permette di eseguire rapidamente i solutori.

### Sintassi

```bash
python main.py -f FILE -t TOLERANCE [-s {0,1,2,3,4}]
```

### Argomenti

* `-f`, `--file` : file `.mtx` contenente la matrice SPD (**obbligatorio**)
* `-t`, `--tolerance`: tolleranza sul residuo relativo (**obbligatorio**)
* `-s`, `--solver` : metodo risolutivo (**opzionale, default: 0**)

| Valore | Metodo              |
| ------ | ------------------- |
| 0      | Tutti               |
| 1      | Jacobi              |
| 2      | Gauss-Seidel        |
| 3      | Gradiente           |
| 4      | Gradiente Coniugato |

### Esempio

```bash
python main.py -f spa1.mtx -t 1e-6 -s 4
```

---

## 🖥️ Interfaccia TUI (Textual)

Il progetto include anche una dashboard interattiva da terminale (`app.py`) basata su **Textual**.

Permette di eseguire i test in modo più intuitivo rispetto alla CLI.

### ✨ Funzionalità

* Selezione interattiva dei file `.mtx`
* Scelta del metodo iterativo
* Inserimento della tolleranza
* Esecuzione multipla (tutti i metodi)
* Output tabellare con:

  * convergenza
  * iterazioni
  * tempo
  * errore
* Console con log colorati

---

### ▶️ Avvio

```bash
python app.py
```

---

### 🎮 Controlli

| Tasto    | Azione          |
| -------- | --------------- |
| Ctrl + R | Esegui          |
| Ctrl + C | Pulisci console |
| Ctrl + Q | Esci            |

---

### 📂 Ricerca automatica dei dataset

L'applicazione cerca automaticamente i file `.mtx` nelle directory:

* `../Data`
* `./Data`
* `../../Data`

Se non vengono trovati file validi, verrà mostrato un messaggio di errore.

---

## 📊 Benchmark

Il progetto include strumenti per eseguire benchmark completi dei metodi iterativi.

### ⚙️ benchmark.py

Il file `benchmark.py` consente di:

* Eseguire tutti i metodi su tutte le matrici disponibili
* Testare diverse tolleranze
* Raccogliere metriche di performance:

  * tempo di esecuzione
  * numero di iterazioni
  * errore

I risultati vengono salvati automaticamente in un file `.csv`.

---

### 📈 plotter.py

Il file `plotter.py` utilizza i dati generati dal benchmark per produrre grafici:

* **Tempo vs Tolleranza**
* **Iterazioni vs Tolleranza**

I grafici permettono di confrontare visivamente le prestazioni dei diversi metodi.

---

## 📂 Dataset

La libreria è testata sulle matrici sparse fornite per il progetto:

* `spa1.mtx`, `spa2.mtx`
* `vem1.mtx`, `vem2.mtx`

---

## 🧩 Struttura del progetto

```bash
.
├── solvers.py        # Implementazione metodi iterativi
├── main.py           # CLI
├── app.py            # Interfaccia TUI
├── benchmark.py      # Esecuzione benchmark
├── plotter.py        # Generazione grafici
├── test.py           # Funzioni di testing
├── Data/             # Matrici .mtx
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autori

* Nicolas Chines (899536)
* Jacopo Borgato (866305)
