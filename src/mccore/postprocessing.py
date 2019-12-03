from mccore import preprocessing

def prepare_output(name):
    '''Prepares the name of a file for named entity recognition output.
    '''
    # Remove commas
    name = name.replace(',', '')
    
    # Remove paths
    name = name.split('/')[-1]

    # Normalize word separators
    for c in '._-[]+':
        name = name.replace(c, ' ')

    # Remove any non word characters
    for c in '\"`~#^*()-_+=[]|;:<>,./{}':
        name = name.replace(c, '')

    # Split season and episode numbers
    name = preprocessing.split_season_episode(name)

    # Remove duplicate spaces
    name = ' '.join(name.split())

    return name