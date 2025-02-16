import json
import random
random.seed(42)
messages_list=[]
idx=0
#with open("../data/out_saved2.json") as f:
with open("../data/out_partially_corrected.json") as f:
    for line in f:
        #print(line)
        data=json.loads(line)
        target_data=data[list(data.keys())[0]]["orig"]
        input_data=data[list(data.keys())[0]]["transl"]

        print(str(idx)+",target,"+target_data)
        print(str(idx)+",input,"+input_data)

        system_dict=dict()
        input_dict=dict()
        target_dict=dict()
        system_dict["role"] = "system"
        system_dict["content"] = "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobotnia"

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
        idx+=1
random.shuffle(messages_list)

test_set=messages_list[0:100]
train_set=messages_list[101:]

if True:
    with open("../data/train_set2.json","w") as f:
        for message in train_set:
            json.dump(message,f)
            f.write("\n")

    with open("../data/test_set2.json","w") as f:
        for message in test_set:
            json.dump(message,f)
            f.write("\n")
