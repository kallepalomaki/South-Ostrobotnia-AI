import json

with open("../data/vocabulary_lehv_check.json", "r") as f:
    array_cleaned=json.load(f)

with open("../data/vocabulary_checked.json", "r") as f:
    array_cleaned.extend(json.load(f))

with open("../data/vocabulary_to_check.json", "r") as f:
    array_to_check=json.load(f)

dialect_words = [item["dialect"] for item in array_cleaned]
dialect_words_unchecked = [item["dialect"] for item in array_to_check]

extra_item=[]
for item in dialect_words_unchecked:
    if item not in dialect_words:
        extra_item.append(item)

idx=0
data_arr=[]
for item in array_cleaned:
    print(item, idx)
    idx+=1
    #for sub_item in item:
    data_arr.append({
        "Question": item["standard"],  # Standard Finnish
        "Complex_CoT": "",
        "Response": item["dialect"],  # South Ostrobothnian dialect
        "text": item["standard"] + " - " + item["dialect"]  # Same as Question and Response
    })

with open("../data/vocabulary_deep_seek_format.json","w") as f:
    json.dump(data_arr,f,ensure_ascii=False)
    f.write("\n")

#print(array_cleaned)
