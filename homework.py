#Audit task
from os import path, makedirs, listdir
from datetime import date

def create_folder(folder_name):
    if not path.exists(folder_name):
        makedirs(folder_name)

def create_file(folder_name,personal_id_number):
    file_created = path.join(folder_name, f"{personal_id_number}.txt")
    return file_created

def write_file_info(file_path, name, surname, personal_id_number):
    with open(file_path, "w")as f:
        f.write(f"Name:{name}/nSurname: {surname}/nPersonal ID number:{personal_id_number}/n")

def output_to_screen(folder_name):
    for file in listdir(folder_name):
        with open(path.join(folder_name, file), "r")as f:
            print(f.read())

name = input("Name:")
surname = input("Surname")
personal_id_number = int(input("ID number:"))

folder_name = date.today().strftime("%Y-%m-%d")
create_folder(folder_name)

file_path = create_file(folder_name, personal_id_number)
write_file_info(file_path, name, surname, personal_id_number)

output_to_screen(folder_name)