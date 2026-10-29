import extract, shutil, pathlib, os
import dump_and_load as dald
from datetime import datetime

def preview(file_dict):
    files=0
    categories=0
    for key,value in file_dict.items():
        categories+=1
        print(f"{key}/")
        k=1
        for file in value:
            print(f"  {k}. {file}")
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
            file_path=path+slash+file_name
            destination=path+slash+key
            previous_location=path
            new_location_of_file=path+slash+key+slash+file_name
            
            moves[new_location_of_file]=previous_location
            shutil.move(file_path,destination)
    data=dald.load_data("test.json")
    now=datetime.now()
    data.append((str(now),moves))
    dald.dump_data("test.json",data)

def organise(path):
    file_dict=extract.arrange(path)
    preview(file_dict)
    user=input("Type 'apply' to apply changes")
    if user=="apply":
        move(file_dict,str(path))
   
    input()
