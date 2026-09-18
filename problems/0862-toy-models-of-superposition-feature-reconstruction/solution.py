import numpy as np

def superposition_reconstruct(W, b, X):
    """
    Compute reconstructed features for the toy superposition model.

    Args:
        W: array of shape (n_hidden, n_features)
        b: array of shape (n_features,)
        X: array of shape (batch_size, n_features)

    Returns:
        list of lists of shape (batch_size, n_features) with reconstructed features
    """

    W = np.asarray(W, dtype = float)
    b = np.asarray(b, dtype = float)
    X = np.asarray(X, dtype = float)

    hidden = X @ W.T
    decoded = hidden @ W + b 
    reconstructed  = np.maximum(0, decoded)

    return reconstructed.tolist()
    pass
