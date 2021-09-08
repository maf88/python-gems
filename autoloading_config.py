"""
    Load all value stored in the `.config.json` file automatically
    into a namedTuple.
    
    Example:
    ---------
    At the end of this file (`./utils/config.py`):
    ```
    field1 = get_config_file()['field1']
    ```
    Then in another file (./foo.py):
    ```
    from utils.config import field1

    print(field1.var1) # for instance
    ```
"""
from collections import namedtuple
import json



class Constant:
    """
    Load the `./.config.json` (default) file to
    """
    def __init__(self, config_path='./.config.json'):

        def _mk_constants(dct):
            return namedtuple('constants', dct.keys())(* dct.values())

        with open(config_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.cfg = json.loads(content, object_hook=_mk_constants)


# Get config file
def get_config_file():
    """
    Return the defaults configuration file
    """
    __constants = Constant()
    return __constants.cfg


# CONSTANTS DECLARATION
var1 = get_config_file()['field1']
