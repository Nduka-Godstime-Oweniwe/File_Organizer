import json
import os
# data = {
#     "name": "Godstime",
#     "age": 25,
#     "skills": ["Python", "HTML", "CSS"]
# }

# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)


# import json

# with open("data.json", "r") as file:
#     data = json.load(file)

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

# dump_data("test.json",data)
# result=load_data("test.json")
# print("Result: ",result)