import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    x = np.asarray(x , dtype = float)
    analytical_grad = np.asarray(analytical_grad, dtype = float)

    numerical_grad = np.zeros_like(x)

    for idx in np.ndindex(x.shape):
        x_plus = x.copy()
        x_minus = x.copy()

        x_plus[idx] += epsilon
        x_minus[idx] -= epsilon

        numerical_grad[idx] = (f(x_plus) - f(x_minus)) / (2 * epsilon)

        denominator  = ( np.linalg.norm(numerical_grad) +  np.linalg.norm(analytical_grad))


        if denominator == 0:
            relative_error = 0
        else:
            relative_error = np.linalg.norm(analytical_grad - numerical_grad) / (denominator)
    return numerical_grad, relative_error


    pass