import json
from settings import *


with open(get_path_actual("archivos.json")) as i:
    files = json.load(i)
