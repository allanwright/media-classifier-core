import re

def prepare_input(name):
    '''Prepares the name of a file for classification or prediction.
    '''
    # Remove commas
    name = name.replace(',', '')

    # Lowercase filename
    name = name.lower()
    
    # Remove paths
    name = name.split('/')[-1]

    # Normalize word separators
    for c in '._-[]+':
        name = name.replace(c, ' ')

    # Remove any remaining punctuation and non word characters
    for c in '\'\"`~!@#$%^&*()=|;:<>,/?{}':
        name = name.replace(c, '')

    # Split season and episode numbers
    name = split_season_episode(name)

    # Remove duplicate spaces
    name = ' '.join(name.split())

    return name

def split_season_episode(name):
    patterns = [
        [r'(?P<sid>s\d+)(?P<eid>e\d+)', '{sid} {eid}'], #s01e01
        [r'(?P<sid>\d+)x(?P<eid>\d+)', 's{sid} e{eid}'] #01x01
    ]
    for pattern in patterns:
        match = re.search(pattern[0], name)
        if match != None:
            name = name.replace(
                match.group(0),
                pattern[1].format(
                    sid=match.group('sid'),
                    eid=match.group('eid')))
    return name