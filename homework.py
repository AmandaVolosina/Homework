#Third practical task
def sum_numbers(*numbers: tuple) -> float:
    """Sum numbers """
    return sum(numbers)
print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20,2,))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))

#Audit system task

from os import path, makedirs, listdir
from datetime import date

name = input("Name: ")
surname = input("Surname: ")
personal_id_number = int(input("ID number: "))

file_created = ""
today_date = date.today().strftime("%Y-%m-%d")


def create_folder():
    if not path.exists(today_date):
        makedirs(today_date)

def create_file():
    global file_created
    file_created = path.join(today_date, f"{personal_id_number}.txt")


def write_file_info():
    with open(file_created, "w") as f:
        f.write(f"Name: {name}\nSurname: {surname}\nPersonal ID number: {personal_id_number}\n")


def output_to_screen():
    for file in listdir(today_date):
        with open(path.join(today_date, file), "r") as f:
            print(f.read())


create_folder()
create_file()
write_file_info()
output_to_screen()
