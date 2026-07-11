import os 
from utils import * 

class Config (object):

    ROOT_DIRECTORY = os.path.abspath(".")
    dir_data_radar  = os.path.join(ROOT_DIRECTORY,"data_radar")
    dir_dataset   = os.path.join(ROOT_DIRECTORY,"dataset")
    dataset   = os.path.join(dir_dataset,"radar_dataset.csv")

    def __init__(self):
        ### creamos carpeta si no existe
        create_directory(self.dir_data_radar)
        create_directory(self.dir_dataset)
    