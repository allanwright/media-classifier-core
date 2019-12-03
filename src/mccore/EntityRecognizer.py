import spacy
from mccore import ner
from mccore import persistence
from mccore import preprocessing
from mccore import postprocessing

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
        nlp, _ = ner.get_model()
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
        x_out = postprocessing.prepare_output(name)
        x_out = x_out.split(' ')
        y = self.model(x)
        entities = [(e.label_, e.text, e.start) for e in y.ents]

        # TODO: This works but I can make it cleaner
        merged = {}
        for e in entities:
            label, _, start = e
            if label in merged:
                merged[label] = merged[label] + ' ' + x_out[start]
            else:
                merged[label] = x_out[start]
        return [(i, merged[i]) for i in merged]