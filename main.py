import pathlib, os, shutil, time, json, csv, extract, user_input, organise,undo
def clear():
    os.system("cls" if os.name=="nt" else "clear")

root=extract.get_root()
current=pathlib.Path(root)
while True:
    clear()
    try:
        files=extract.view_folder_file(current)
    except PermissionError:
        print("Sorry you're not authorised to go into this folder!")
        input("Press Enter to go back")
        current=current.parent
        continue

    user_folder=user_input.user_input("Select Folder No | 'history' to view history | 'back' to go back | 'organise' to organise: ",len(files),("back","organise","history"))
    if user_folder=="back":
        if current==root:
            print("Ooops! Sorry can't go back!")
            time.sleep(2)
            continue
        else:
            current=current.parent
            continue
    if user_folder=="organise":
        organise.organise(current)
        continue

    if user_folder=="history":
        undo.get_history("test.json")
        input()
        continue
    
    if files[user_folder-1].is_dir():
        current=files[user_folder-1]
    else:
        print("You clicked a file! You can't view a file! Nor vex")
        time.sleep(3)
  
