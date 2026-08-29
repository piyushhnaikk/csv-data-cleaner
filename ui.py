import os

def get_path(fileName):
    is_correct = True
    while(is_correct):

        path = "data/" + fileName
        if os.path.exists(path):
            is_correct = False
            return path
        print("Make sure you have the file in data folder!") 


def check_Filename(fileName):
    while True:
        path = "output/" + fileName
        if os.path.exists(path):
            print("Name exist try changing FileName!\n\n") 
            fileName = input("Try again: ")
        else:
            return fileName