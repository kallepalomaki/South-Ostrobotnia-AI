import json
import random
random.seed(42)
messages_list=[]

with open("../data/out_saved.json") as f:
    for line in f:
        #print(line)
        data=json.loads(line)
        target_data=data[list(data.keys())[0]]["orig"]
        input_data=data[list(data.keys())[0]]["transl"]
        system_dict=dict()
        input_dict=dict()
        target_dict=dict()
        system_dict["role"] = "system"
        system_dict["content"] = "Hupulaanen is a factual chatbot that is funny and speaks also Finnish language dialect of South-Ostrobnia"

        input_dict["role"] = "user"
        input_dict["content"] = "Ilmaise seuraava Etelä-Pohjanmaan murteella: " + input_data

        target_dict["role"] = "assistant"
        target_dict["content"] = target_data
        messages=[]
        messages.append(system_dict)
        messages.append(input_dict)
        messages.append(target_dict)
        messages_dict=dict()
        messages_dict["messages"]=messages
        messages_list.append(messages_dict)

random.shuffle(messages_list)

test_set=messages_list[0:100]
train_set=messages_list[101:]

with open("../data/train_set.json","w") as f:
    for message in train_set:
        json.dump(message,f)
        f.write("\n")

with open("../data/test_set.json","w") as f:
    for message in test_set:
        json.dump(message,f)
        f.write("\n")