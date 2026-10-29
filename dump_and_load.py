import json
import os
import csv,pathlib

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            data=json.load(file)
            return data
    else:
        dump_data(file_name,[])
        return []

def dump_data(file_name: str,data):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)
    dump_to_csv("record.csv",file_name,data)

def dump_to_csv(csv_file_name,data_file_name,histories):
    with open(csv_file_name,"w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["SN","Date","Time","File Name","Previous Location","Current Location"])
        sn,date,time,name,previous,current=1,"","","","",""
        for history in histories:
            date=history[0][:10]
            time=history[0][10:]
            for key,value in history[1].items():
                path=pathlib.Path(key)
                name=path.name
                current=path.parent
                previous=value[1]
                writer.writerow([sn,date,time,name,previous,current])
                sn+=1

