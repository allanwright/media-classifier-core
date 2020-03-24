'''Helper methods for making classification predictions.

'''

import numpy as np

from mccore import persistence

def get_label(proba, labels):
    '''Gets the label from the specified class probability estimates.

    Args:
        proba (array like): The estimated class probability estimates.
        labels (dictionary): The label dictionary.

    Returns:
        label (object): The label associated with the class having the highest probability estimate.
        esimate (float): The probability estimate.
    '''
    label_id = np.argmax(proba)
    label = {
        "id": label_id,
        "name": labels[str(label_id)]
    }
    return (label, np.max(proba))

def get_labels():
    '''Gets the label dictionary.

    Returns:
        dictionary: The label dictionary.
    '''
    return persistence.json_res_to_obj('label_dictionary.json')
