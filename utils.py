import numpy as np

def χ_sq(fn, x, params, y, σ):
    resid = y - fn(x, *params)
    χ_sq_val = np.sum((resid / σ)**2)
    return χ_sq_val
