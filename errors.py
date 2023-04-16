import numpy as np

def MSE(y_true:np.array, y_pred:np.array) -> float:
    """
    Calculate mean squared error.
    """
    # Checking if there are NaNs in arrays, if detected, delete records in two arrays
    indexes = list(np.where(np.isnan(y_pred)==1))
    indexes.reverse()
    for i in indexes:
        y_true = np.drop(y_true, i)
    y_pred = y_pred[~np.isnan(y_pred)]

    if n:=len(y_true) != len(y_pred):
        raise ValueError('y_true and y_pred must have the same size.')
    return np.sum(np.power(y_true-y_pred, 2)) / n

def MAE(y_true:np.array, y_pred:np.array) -> float:
    # Checking if there are NaNs in arrays, if detected, delete records in two arrays
    indexes = list(np.where(np.isnan(y_pred)==1))
    indexes.reverse()
    for i in indexes:
        y_true = np.drop(y_true, i)
    y_pred = y_pred[~np.isnan(y_pred)]
    
    if n:=len(y_true) != len(y_pred):
        raise ValueError('y_true and y_pred must have the same size.')
    return np.sum(np.abs(y_true - y_pred, 2)) / n