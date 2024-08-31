import json
import os

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

#print(data)

#create file per name
for i in data:
    col_file = open("./scripts/"+i["name"]+"_col.script", "w")
    negatives = ""
    col_file.write("import gold\nsession create "+i["user_id"]+"\nsession attach 1\n")
    for neg_word in i["negativelist"]:
        negatives = negatives+"-!subject "+neg_word+" "
    for word in i["wordlist"]:
        col_file.write("pull -subject "+word+" "+negatives+"\n")
    col_file.write("quit")
    col_file.close()

for file in os.listdir("./scripts"):

    print(file)




