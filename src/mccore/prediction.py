'''Helper methods for making classification predictions.

'''

import numpy as np

def get_class(proba, labels):
    '''Gets the class label from the specified class probability estimates.

    Args:
        proba (array like): The estimated class probability estimates.
        labels (dictionary): The label dictionary.

    Returns:
        class (object): The class label and associated probability estimate.
    '''
    label_id = np.argmax(proba)
    return {
        "label": {
            "id": int(label_id),
            "name": labels[str(label_id)]
        },
        "probability": float(np.max(proba))
    }
