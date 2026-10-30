import os
import pathlib

def get_root():
    root=pathlib.Path().cwd()
    while root!=root.parent:
        root=root.parent
    return root

def view(path,view=True):
    files=pathlib.Path(path).iterdir()
    k=1
    result=[]
    for file in files:
        if file.name.startswith("."):
            continue
        if view:    
            print(f"{str(k)+".":>3} {file.name}")
        result.append(file)
        k+=1
    return result
    
def arrange(original_path,path,banks={},depth=0):
    
    files=view(path,False)
    if len(files)==0:
        return banks
    bank={
        "Images":{".jpg",".png"},
        "Documents":{".pdf",".pptx",".docx"},
        "Audio":{".mp3",".wav"},
        "Archives":{".zip"},
        "Code":{".html",".py",".css",".js",".go"},  
        "Videos":{".mp4",".mkv",".avi"},      
    }
    slash="/"
    if os.name=="nt":
        slash="\\"  

    for file in files:
        
        if file.is_file():
            found=False
            for folder_name,extensions in bank.items():
                if file.suffix in extensions:
                    if pathlib.Path(file.parent)==pathlib.Path(str(original_path)+slash+folder_name):
                        # print(f"File {file.name} is already in the correct folder: {folder_name}")
                        found=True
                        continue
            
                    found=True
                    if folder_name not in banks:
                        banks[folder_name]=[str(file)]
                    else:
                        banks[folder_name].append(str(file))
            if not found:
                if "Others" not in banks:
                    banks["Others"]=[str(file)]
                else:
                    banks["Others"].append(str(file))
                    
        else:
            if depth==0:
                continue
            else:
                banks=arrange(original_path,str(file),banks,depth-1)
    return banks



    