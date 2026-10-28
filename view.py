import pathlib

def view_folder_file(path):
    files=pathlib.Path(path).iterdir()
    k=1
    result=[]
    for file in files:
        print(f"{str(k)+".":>3} {file.name}")
        result.append(file)
        k+=1
    if result:
        return result
    else:
        return None