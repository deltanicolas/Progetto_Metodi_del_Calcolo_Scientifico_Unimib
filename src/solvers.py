import numpy as np
import time

class MatSolvers:
    def __init__(self, mat, b, tol, max_iter=20000):
        self.A = mat
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.n = mat.shape[0]

    # =========================
    # Utility interna
    # =========================
    
    def _stopping_criterion(self, x):
        """
        Calcola: ||Ax - b|| / ||b|| 
        """
        res = self.A.dot(x) - self.b
        return np.linalg.norm(res) / np.linalg.norm(self.b)

    def _initial_guess(self):
        return np.zeros(self.n)
      
    # =========================
    # Solvers
    # =========================

    def jacobi(self):
        x = self._initial_guess()
        it = 0
        D_diag = self.A.diagonal()
        conv = False

        if np.any(D_diag == 0):
            print("Error: The matrix has zero diagonal entries. Jacobi method may not converge.") 
            return x, it, False, 0.0

        start_t = time.perf_counter()

        while it < self.max_iter:
            residual = self.b - self.A.dot(x)
            x = x + (residual / D_diag) # the same as x = (b - (A - D) @ x) @ D^-1 but more efficient
            it += 1
            if self._stopping_criterion(x) < self.tol:
                conv = True
                break
  
        end_t = time.perf_counter()

        return x, it, conv, end_t - start_t
    
    def gauss_seidel(self):
        x = self._initial_guess()
        it = 0
        conv = False
        start_t = time.perf_counter()
        
        # --- TODO: Implementazione logica Gauss-Seidel ---

        end_t = time.perf_counter()
        
        return x, it, conv, end_t - start_t
    
    def gradient(self):
        x = self._initial_guess()
        d = - (self.A.dot(x) - self.b)
        it = 0
        conv = False
        start_t = time.perf_counter()
        
        while it < len(self.b):
            r = self.b - self.A.dot(x)
            y = self.A.dot(d)
            z = self.A.dot(r)
            alpha = d.dot(r) / d.dot(y)
            x += alpha * d
            r = self.b - self.A.dot(x)
            w = self.A.dot(r)
            beta = d.dot(w) / d.dot(y)
            d = r - beta * d
            it += 1
            if self._stopping_criterion(x) < self.tol:
                conv = True
                break
        
        end_t = time.perf_counter()
        
        return x, it, conv, end_t - start_t

    def gradient_conjugate(self):
        x = self._initial_guess()
        it = 0
        conv = False
        start_t = time.perf_counter()
        
        # Sappiamo che il metodo del gradiente converge in al piu n iterazioni
        # dove n = dimensione della matrice
        # invece che usare il numero massimo di iterazioni controllare n
        while it < len(self.b):
            r = self.b - self.A.dot(x)
            y = self.A.dot(r)
            alpha = r.dot(r) / r.dot(y)
            x = x + alpha * r
            it += 1
            if self._stopping_criterion(x) < self.tol:
                conv = True
                break
        
        end_t = time.perf_counter()
        
        return x, it, conv, end_t - start_t