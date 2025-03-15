import openai
import json
import re
from normalized_lehvenstein import normalized_levenshtein

with open("../openai.key") as f:
    openai.api_key = f.read().strip().replace("OPENAI_API_KEY=","")

client = openai #.OpenAI()

def chat_completion(prompt):
    completion = client.chat.completions.create(
    #model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
    #model="ft:gpt-3.5-turbo-0125:personal::9DxjYJle",
    #model= "ft:gpt-3.5-turbo-0125:personal::B1eKaRYa",
    #model="ft:gpt-4o-mini-2024-07-18:personal::B1hcGPmR",
    #model="ft:gpt-4o-2024-08-06:personal::B1iQ8l8h",
    #model="ft:gpt-4o-2024-08-06:personal::B3poyXlC",

    model="gpt-4o-2024-08-06",
      messages=[
        #{"role": "system", "content": "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobnia"},
        {"role": "system", "content":  "Translate each word in South Ostrobothnian dialect sentence to standard Finnish. Use the given context sentence with the same meaning in South Ostrobothnian dialect. "
                                       "Organize output as json list with tags dialect and standard like this example: {\"dialect\":\"hevoonen\",\"standard\":\"hevonen\”}"},
        #{"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Palavalla rakkaudella on surullinen loppu, tapasi isoisä vainaja sanoa."}
        {"role": "user", "content":  prompt}
      ]
    )


    return completion.choices[0].message

cnt=0
if False:
    with open("../data/vocabulary.json","w") as fw:
        with open("../data/out_partially_corrected2.json","r") as f:
            for line in f:
                data=json.loads(line)
                print(data)
                target_data = "\ndialect:" + data[list(data.keys())[0]]["orig"]
                input_data = "\nstandard:" + data[list(data.keys())[0]]["transl"]
                prompt=target_data+target_data+input_data
                result=chat_completion(prompt=prompt)
                fw.write(result.content)
                fw.write("\n")
                print(result.content)
                cnt+=1

data_as_str="["
with open("../data/vocabulary.json","r") as f:
    for line in f:
        line = re.sub(r'//.*', '', line)
        line=line.replace("}\n","},\n")
        if "```json" not in line:
            if "```" not in line:
                if ("]" in line) or ("[" in line):
                    #data_as_str+=line.strip()+",\n"
                    print("here")
                    pass
                else:
                    data_as_str+=line

data_as_str = data_as_str[::-1].replace(",", "", 1)[::-1]+"]"

try:
    data_dict = json.loads(data_as_str)
except json.JSONDecodeError as e:
    # Print the error message
    print(f"Error: {e}")
    # Print the part of the string that caused the error
    error_position = e.pos  # Position where the error occurred
    print(f"Error occurred at position: {error_position}")

    # Show a snippet of the problematic part
    start = max(0, error_position - 100)  # Show 100 chars before the error
    end = error_position + 100  # Show 100 chars after the error
    print(f"Problematic part of the JSON:\n{data_as_str[start:end]}")

vocabulary=[]
for item in data_dict:
    vocabulary.append(str(item))

print(len(vocabulary))
vocabulary=list(set(vocabulary))
print(len(vocabulary))
array_cleaned=[]
array_to_check=[]
for item in vocabulary:
    item=item.replace("'","\"")
    data=json.loads(item)
    dialect=data["dialect"].strip()
    standard=data["standard"].strip()
    if (" " in dialect) or (" " in standard):
        #print(dialect)
        pass
    elif normalized_levenshtein(dialect,standard) > 0.7:
        array_to_check.append(data)
    else:
        print(item)
        array_cleaned.append(data)

#for item in array_cleaned:
#    print(item)

if True:
    with open("../data/vocabulary_lehv_check.json","w") as f:
        json.dump(array_cleaned, f, ensure_ascii=False, indent=4)

    with open("../data/vocabulary_to_check.json","w") as f:
        json.dump(array_to_check,f, ensure_ascii=False, indent=4)

with open("../data/vocabulary_lehv_check.json", "r") as f:
    array_cleaned=json.load(f)

with open("../data/vocabulary_checked.json", "r") as f:
    array_cleaned.extend(json.load(f))

for item in array_cleaned:
    print(item)
