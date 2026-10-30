import json
import os
import csv,pathlib

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            histories=json.load(file)
            return histories
    else:
        dump_data(file_name,[])
        return []

def dump_data(file_name: str,histories):
    with open(file_name,"w") as file:
        json.dump(histories,file,indent=4)
    dump_to_csv("record.csv",file_name,histories)

def dump_to_csv(csv_file_name,data_file_name,histories):
    with open(csv_file_name,"w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["SN","Date","Time","File Name","Old Name","Previous Location","Current Location"])
        sn,date,time,name,old_name,previous,current=1,"","","","","",""
        for history in histories:
            date=history[0][:10]
            time=history[0][10:]
            for key,value in history[1].items():
                # print(history[1])
                path=pathlib.Path(key)
                name=path.name
                old_name=value[2]
                current=path.parent
                previous=value[1]
                writer.writerow([sn,date,time,name,old_name,previous,current])
                sn+=1

