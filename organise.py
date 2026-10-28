import extract, shutil, pathlib, os

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
            shutil.move(file_path,destination)

def organise(path):
    file_dict=extract.arrange(path)
    preview(file_dict)
    user=input("Type 'apply' to apply changes")
    if user=="apply":
        move(file_dict,str(path))
   
    input()
