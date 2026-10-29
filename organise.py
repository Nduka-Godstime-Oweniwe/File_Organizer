import extract, shutil, pathlib, os
import dump_and_load as dald
from datetime import datetime
import time


def organise(path,depth):
    file_dict=extract.arrange(path,path,{},depth)
    preview(file_dict)
    user=input("Type 'apply' to apply changes: ")
    if user=="apply":
        move(file_dict,str(path))
   
    input()

def preview(file_dict):
    files=0
    categories=0
    for key,value in file_dict.items():
        categories+=1
        print(f"{key}/")
        k=1
        for file in value:
            print(f"  {k}. {pathlib.Path(file).name}")
            k+=1
        files+=k-1
    print(f"Total: {files} files, {categories} categories")
        
        
def move(file_dict,path: str):
    moves={}
    for key,value in file_dict.items():
        try:
            pathlib.Path(path+f"/{key}").mkdir()
        except FileExistsError:
            pass

        for file_name in value:
            slash="/"
            if os.name=="nt":
                slash="\\"
            file_path=str(file_name)
            destination=path+slash+key
            previous_location=str(pathlib.Path(file_name).parent)
            new_location_of_file=path+slash+key+slash+str(pathlib.Path(file_name).name)
            
            moves[new_location_of_file]=(path,previous_location)
           
            shutil.move(file_path,destination)
    data=dald.load_data("test.json")
    now=datetime.now()
    data.append((str(now),moves))
    dald.dump_data("test.json",data)

