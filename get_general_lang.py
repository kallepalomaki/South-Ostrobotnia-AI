from openai import OpenAI
import json
client = OpenAI()

def send_to_open_ai(content):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You will be provided with statements in Finnish South-Ostrobotnia dialect, and your task is to convert them to standard Finnish."
      },
      {
        "role": "user",
        "content": content
      }
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
  )
  return response.choices[0].message.content

idx=0
idx_json=0
line_to_sent=""
with open("../data/out.json","w") as fw:
  with open("../data/uncorrected2.txt") as f:
    for line in f:
      line=line.replace("..",".").replace("..",".").replace("..",".")
      print(line)
      criteria = lambda x: ':' if ':' in x else ','
      line_splitted=line.split(".")
      for line_in_splitted in line_splitted:
        if len(line_in_splitted.strip())>3:
          line_to_sent+=line_in_splitted.strip()+" "
          if idx==1:
            print(line_to_sent)
            line_json=dict()
            line_idx=dict()
            #line_transl=""
            line_transl=send_to_open_ai(line_to_sent)
            print(line_transl)
            line_json["orig"]=line_to_sent
            line_json["transl"]=line_transl
            line_idx[str(idx_json)]=line_json
            json.dump(line_idx, fw)
            fw.write("\n")
            line_to_sent=""
            idx_json += 1
            idx=0
          idx+=1

    #    print(line)
      #print(response.choices[0].message)
