import dump_and_load as dald
import user_input
import shutil
def get_history(file_name):
    histories=dald.load_data(file_name)
    k=1
    if not histories:
        print("Ooops! No history yet")
        return
    for history in histories:
        date=history[0]
        # print(date)
        folders=history[1]
        # print(type(folders))
        for key,value in folders.items():
            print(f"{k}. Folder: {value} Date: {date}")
            k+=1
            break
    
    user=user_input.user_input("Select History to undo moves | 'back' to go back",len(histories),("back"))
    if user=="back":
        return
    else:
        undo(file_name,histories,user-1)
        

def undo(file_name,histories,index):
    for key,value in histories[index][1].items():
        shutil.move(key,value)
    histories.pop(index)
    dald.dump_data(file_name,histories)
    