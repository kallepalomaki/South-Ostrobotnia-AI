import openai
import json

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
with open("../data/vocabulary.json","w") as fw:
    with open("../data/out_partially_corrected.json","r") as f:
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


