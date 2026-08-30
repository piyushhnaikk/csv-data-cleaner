import os

def get_path(fileName):
    while  True:

        path = "data/" + fileName + ".csv"
        if os.path.exists(path):
            return path
        print("Make sure you have the file in data folder!") 


def check_Filename(fileName):
    while True:
        path = "output/" + fileName + ".xlsx"
        if os.path.exists(path):
            print("Name exist try changing FileName!\n\n") 
            fileName = input("Try again: ")
        else:
            return path