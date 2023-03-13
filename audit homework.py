#Audit task

from os import path,makedirs,listdir
from datetime import date

def create_folder(folder_name):
    if not path.exists(folder_name):
        makedirs(folder_name)


