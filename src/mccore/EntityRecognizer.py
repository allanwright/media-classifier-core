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
        SEP = ' '
        x = preprocessing.prepare_input(name)
        x_out = postprocessing.prepare_output(name)
        x_out = x_out.split(SEP)
        y = self.model(x)
        y = [(e.label_, e.text, e.start) for e in y.ents]

        # Merge entities
        y_merged = {}
        for (label, _, start) in y:
            if label in y_merged:
                y_merged[label] = y_merged[label] + SEP + x_out[start]
            else:
                y_merged[label] = x_out[start]
        
        # Remove leading s and e from season and episode numbers
        SID = 'season_id'
        EID = 'episode_id'
        if SID in y_merged:
            y_merged[SID] = int(y_merged[SID].lstrip('sS'))
        if EID in y_merged:
            y_merged[EID] = int(y_merged[EID].lstrip('eE'))

        return [(i, y_merged[i]) for i in y_merged]