import pathlib
def get_root():
    root=pathlib.Path().cwd()
    while root!=root.parent:
        root=root.parent
    return root

def view_folder_file(path,view=True):
    files=pathlib.Path(path).iterdir()
    k=1
    result=[]
    for file in files:
        if view:    
            print(f"{str(k)+".":>3} {file.name}")
        result.append(file)
        k+=1
    if result:
        return result

def arrange(path):
    files=view_folder_file(path,False)
    bank={
        "Images":{".jpg",".png"},
        "Documents":{".pdf",".pptx",".docx"},
        "Audio":{".mp3",".wav"},
        "Archives":{".zip"},
        "Code":{".html",".py",".css",".js",".go"},        
    }
    result={}
    for file in files:
        if file.is_file():
            found=False
            for key,value in bank.items(): 
                if file.suffix in value:
                    found=True
                    if key in result:
                        result[key].append(file.name)
                    else:
                        result[key]=[file.name]
            if not found:
                if "Others" in result:
                    result["Others"].append(file.name)
                else:
                    result["Others"]=[file.name]
    return result