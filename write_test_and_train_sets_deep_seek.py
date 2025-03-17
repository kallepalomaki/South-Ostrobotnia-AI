import json
import random
from IPython.display import display, JSON

from datasets import Dataset

random.seed(42)
messages_list=[]
#with open("../data/out_saved2.json") as f:
def write_translated():
    idx = 0
    data_arr=[]
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
            #system_dict["content"] = "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobotnia"
            #{"role": "system", "content":
            #system_dict["content"]="You are a storyteller who writes in the South Ostrobothnian dialect."
            #{"role": "system",
            system_dict["content"]="You translate standard Finnish sentences into the South Ostrobothnian dialect."
            input_dict["role"] = "user"
            input_dict["content"] = "Ilmaise seuraava Etelä-Pohjanmaan murteella: " + input_data

            target_dict["role"] = "assistant"
            target_dict["content"] = target_data
            #question_arr.append(input_data)
            #complex_cot_arr.append("")
            #response_arr.append(target_data)
            #text_arr.append(input_data + " - " + target_data)
            data_arr.append({
                "Question": input_data,  # Standard Finnish
                "Complex_CoT": "",
                "Response": target_data,  # South Ostrobothnian dialect
                "text": input_data + " - " + target_data  # Same as Question and Response
            })


    return data_arr





train_set=[]
test_set=[]

if True:
    train_set=write_translated()
    display(JSON(train_set))
    print()


if True:
    with open("../data/train_set_deep_seek.json","w") as f:
        json.dump(train_set,f,ensure_ascii=False)
        f.write("\n")


