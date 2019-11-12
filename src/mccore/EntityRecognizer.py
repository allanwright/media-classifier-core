import spacy
from mccore import ner
from mccore import persistence
from mccore import preprocessing

class EntityRecognizer:
    ''' Defines a named entity recognizer.
    
    '''

    def __init__(self, model):
        ''' Initializes a new instance of the EntityRecognizer object.

        Args:
            model (object): the trained model.
        '''
        self.model = model
    
    @classmethod
    def load_default(cls):
        ''' Initializes a new instance of the Classifier object using model included with the package.
        
        '''
        nlp = ner.get_model()
        nlp.from_bytes(persistence.bin_res_to_obj('ner_mdl.pickle'))
        return cls(nlp)
    
    def predict(self, name):
        ''' Recognizes entities contained within the specified filename.

        Args:
            name (string): The name of the file to recognize entities.
        
        Returns:
            list: The list of tuples containing the entity and associated value.
        '''
        x = preprocessing.prepare_input(name)
        y = self.model(x)
        return [(e.label_, e.text) for e in y.ents]