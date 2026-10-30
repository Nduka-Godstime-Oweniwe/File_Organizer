import dump_and_load as dald
import user_input
import shutil,pathlib,os
def get_history(file_name):
    histories=dald.load_data(file_name)
    k=1
    if not histories:
        print("Ooops! No history yet")
        input("Press Enter to go back")
        return
    for history in histories:
        date=history[0]
        folders=history[1]
        for key,value in folders.items():
            print(f"{k}.You organised this  Folder: {value[0]} on this Date: {date}")
            k+=1
            break
    
    user=user_input.user_input("Select history to undo | 'back' to go back: ",len(histories),("back"))
    if user=="back":
        return
    else:
        undo(file_name,histories,user-1)
        

def undo(file_name,histories,index):
    slash="/"
    if os.name=="nt":
        slash="\\"
    for key,value in histories[index][1].items():
        file=pathlib.Path(key)
        file.rename(value[1]+slash+value[2])
        # shutil.move(key,value[1])
    histories.pop(index)
    dald.dump_data(file_name,histories)
    