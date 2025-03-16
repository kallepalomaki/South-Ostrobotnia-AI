import json

with open("../data/vocabulary_lehv_check.json", "r") as f:
    array_cleaned=json.load(f)

with open("../data/vocabulary_checked.json", "r") as f:
    array_cleaned.extend(json.load(f))

with open("../data/vocabulary_to_check.json", "r") as f:
    array_to_check=json.load(f)

dialect_words = [item["dialect"] for item in array_cleaned]
dialect_words_unchecked = [item["dialect"] for item in array_to_check]


array_cleaned_tmp=[]
idx=0
# filter items that are the same
for item in array_cleaned:
    #print(item, idx)
    idx+=1
    if item["standard"] == item["dialect"]:
        print("is general finnish:", item["standard"])
    else:
        array_cleaned_tmp.append(item)

array_cleaned=array_cleaned_tmp

#remove duplicates
array_cleaned_tmp=[]

for item in array_cleaned:
    array_cleaned_tmp.append(str(item))

print(len(array_cleaned_tmp))
array_cleaned=list(set(array_cleaned_tmp))
print(len(array_cleaned))

array_cleaned_tmp=[]
for item in array_cleaned:
    array_cleaned_tmp.append(json.loads(item.replace("'","\"")))

array_cleaned=array_cleaned_tmp

# synonyms as list to correspond the same standard
standard_dict=dict()
for item in array_cleaned:
    if item["standard"] not in standard_dict.keys():
        standard_dict[item["standard"]]=[item["dialect"]]
    else:
        standard_dict[item["standard"]].append(item["dialect"])



extra_item=[]
for item in dialect_words_unchecked:
    if item not in dialect_words:
        extra_item.append(item)


data_arr=[]
for item in standard_dict:
    #print(item, idx)
    idx+=1
    response=", ".join(standard_dict[item])
    text=item + " - " + response
    #for sub_item in item:
    data_arr.append({
        "Question": item,  # Standard Finnish
        "Complex_CoT": "",
        "Response":  response, # South Ostrobothnian dialect
        "text": text  # Same as Question and Response
    })

print(len(data_arr))
print(len(array_cleaned))
with open("../data/vocabulary_deep_seek_format.json","w") as f:
    json.dump(data_arr,f,ensure_ascii=False)
    f.write("\n")

#print(array_cleaned)
