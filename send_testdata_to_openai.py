import openai
import json

with open("../openai.key") as f:
    openai.api_key = f.read().strip()

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
        {"role": "system", "content":  "You translate standard Finnish sentences into the South Ostrobothnian dialect."},
        #{"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Palavalla rakkaudella on surullinen loppu, tapasi isoisä vainaja sanoa."}
        {"role": "user", "content":  prompt}
      ]
    )


    return completion.choices[0].message

cnt=0
with open("../data/baseline_test_results.json","w") as fw:
    with open("../data/test_set4.json") as f:
        for line in f:
            data=json.loads(line)
            messages=data["messages"]
            for item in messages:
                if item["role"] == "system":
                    if "translate" in item["content"]:
                        task_to_do=item["content"]
                    else:
                        task_to_do=None
                elif item["role"] == "user":
                    user=item["content"]
                elif item["role"] == "assistant":
                    assistant=item["content"]
            if task_to_do!=None:
                print(task_to_do)
                print(assistant)
                result=chat_completion(user)
                json.dump({"result": result.content, "target": assistant, "user": user},fw, ensure_ascii=False)
                fw.write("\n")
                print()
                cnt+=1
            if cnt > 2:
                break


