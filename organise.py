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
        
   
def get_new_name(folder:str,file_name:str):
    new_name="01"+file_name
    slash="/"
    if os.name=="nt":
        slash="\\"
    while True:
        if not pathlib.Path(folder+slash+new_name).exists():
            return new_name
        else:
            new_name="01"+new_name
                 
def move(file_dict,path: str):
    moves={}
    slash="/"
    if os.name=="nt":
        slash="\\"
    for key,value in file_dict.items():
        try:
            pathlib.Path(path+f"{slash}{key}").mkdir()
        except FileExistsError:
            pass

        for file_name in value:
        
            file_path=str(file_name)
            destination=path+slash+key
            previous_location=str(pathlib.Path(file_name).parent)
            new_location_of_file=path+slash+key+slash+str(pathlib.Path(file_name).name)
            
            if previous_location==destination:
                continue
            file_name_path=pathlib.Path(file_name)
            old_name=file_name_path.name
            new_name=file_name
            while True:
                if pathlib.Path(destination+slash+file_name_path.name).exists():
                    new_name=get_new_name(str(file_name_path.parent),str(file_name_path.name))
                    file_name_path=file_name_path.rename(str(file_name_path.parent)+slash+new_name)
                    file_path=str(file_name_path.parent)+slash+new_name
                    new_location_of_file=path+slash+key+slash+new_name
                else:
                    break
            moves[new_location_of_file]=(path,previous_location,old_name)
            # print("New location of file:\n", new_location_of_file)
            # print("Organised Folder:\n", moves[new_location_of_file][0])
            # print("Previous Location:\n", moves[new_location_of_file][1])
            # print("Old Name:\n", moves[new_location_of_file][2])
            # input("\nPress Enter to continue...")
            
            # print(f"Moving {file_path} to {destination}")
            # input()
            
            shutil.move(file_path,destination)
    data=dald.load_data("test.json")
    now=datetime.now()
    data.append((str(now),moves))
    dald.dump_data("test.json",data)

