import json
from pickle import dump, load

def bin_to_obj(path):
    '''Deserializes a binary file into an object.

    Args:
        path (string): The path to load the object from.
    
    Returns:
        Object: The object.
    '''
    with open(path, 'rb') as bin_file:
        return load(bin_file)

def bin_res_to_obj(path):
    '''Deserializes a binary package resource into an object.

    Args:
        path (string): The path to load the object from.
    
    Returns:
        Object: The object.
    '''
    try:
        from importlib.resources import path as resource_path
    except ImportError:
        # Fallback for python < 3.7
        from importlib_resources import path as resource_path
    
    with resource_path(__package__, path) as p:
        return bin_to_obj(p)

def json_to_obj(path):
    '''Deserializes a json package into an object.

    Args:
        path (string): The file path to read from.
    
    Returns:
        Object: The object.
    '''
    with open(path, 'r') as json_file:
        return json.loads(json_file.read())

def json_res_to_obj(path):
    '''Deserializes a json package resource into an object.

    Args:
        path (string): The file path to read from.
    
    Returns:
        Object: The object.
    '''
    try:
        from importlib.resources import path as resource_path
    except ImportError:
        # Fallback for python < 3.7
        from importlib_resources import path as resource_path
    
    with resource_path(__package__, path) as p:
        return json_to_obj(p)

def obj_to_bin(obj, path):
    '''Saves an object to the specified path.

    Args:
        value (object): The object to save.
        path (string): The path to save the object to.
    '''
    with open(path, 'wb') as bin_file:
        dump(obj, bin_file)

def obj_to_json(obj, path):
    '''Serializes an object as json and writes it to the specified file path.

    Args:
        obj (object): The object to serialize.
        path (string): The file path to write to.
    '''
    obj_json = json.dumps(obj)
    with open(path, 'w') as json_file:
        json_file.write(obj_json)