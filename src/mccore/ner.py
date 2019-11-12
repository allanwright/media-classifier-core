import spacy

def get_model():
    ''' Builds and returns a blank named entity recognition model.

    Returns:
        object: The model.
    '''
    nlp = spacy.blank('en')
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
    return nlp