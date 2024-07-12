import json
from settings import *


with open(get_path_actual("musica.json")) as i:
    files = json.load(i)
