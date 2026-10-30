import pathlib, os, shutil, json, csv, extract, user_input, organise,undo
def clear():
    os.system("cls" if os.name=="nt" else "clear")
    
root=extract.get_root()
current=pathlib.Path(root)
while True:
    clear()
    try:
        files=extract.view(current)
    except PermissionError:
        print("Sorry you're not authorised to go into this folder!")
        input("Press Enter to go back")
        current=current.parent
        continue

    user_folder=user_input.user_input("Select Folder No | exit to stop the program | 'history' to view history | 'back' to go back | 'organise' to organise: ",len(files),("back","organise","history","exit"))
    if user_folder=="exit":
        break
    if user_folder=="back":
        if current==root:
            print("Ooops! Sorry can't go back!")
            input("Press Enter to go back")
            continue
        else:
            current=current.parent
            continue
    if user_folder=="organise":
        if current==pathlib.Path().cwd():
            print("Haba now!! You wan still arrange folder wey dey help you organize files")
            current=current.parent
            input("Press enter to go back joor")
            continue
        depth=user_input.user_input("Enter depth of Arrangement\n1 for only current folder\n2 for both current and subfolders\n3 for both current, subfolders,subsubfolders and so on: ",100,())
        organise.organise(current,depth-1)
        
        continue

    if user_folder=="history":
        undo.get_history("test.json")
        continue
    
    if files[user_folder-1].is_dir():
        current=files[user_folder-1]
    else:
        print("You clicked a file! You can't view a file! Nor vex")
        input("Press Enter to go back")
  
