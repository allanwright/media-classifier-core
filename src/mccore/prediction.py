import numpy as np

def get_label(proba, labels):
    '''Gets the label from the specified class probability estimates.

    Args:
        proba (array like): The estimated class probability estimates.
        labels (dictionary): The label dictionary.
    
    Returns:
        label (string): The label associated with the class having the highest probability estimate.
        esimate (float): The probability estimate.
    '''
    return (labels[str(np.argmax(proba))], np.max(proba))