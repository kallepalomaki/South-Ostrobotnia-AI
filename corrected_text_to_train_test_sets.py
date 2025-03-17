#from openai import OpenAI
import json
#client = OpenAI()
import Levenshtein
import numpy as np
idx=0
idx_json=0
line_to_sent=""
line_idx2=0


def normalized_levenshtein(s1, s2):
  dist = Levenshtein.distance(s1, s2)
  max_len = max(len(s1), len(s2))
  return dist / max_len if max_len > 0 else 0

lehv_arr=[]
with open("../data/out_partially_corrected.json","w") as fw:
  with open("../data/dataset_to_correct8.txt") as f:
    for line in f:
      if "**" in line:
        break
      line=line.replace("..",".").replace("..",".").replace("..",".")
      #print(line,end="")
      criteria = lambda x: ':' if ':' in x else ','
      line_splitted=line.split(".")
      if "input" in line:
        line_input="".join(line.split(',')[2:]).strip().replace('.','')
        print(line_input)
        print(normalized_levenshtein(line_target, "Sitten yhden kerran menimme oikein keskustaan elokuvateatteriin"))
        lehv=normalized_levenshtein(line_target, line_input)
        print(lehv)
        line_json = dict()
        line_idx = dict()
        # line_transl=""
        line_json["orig"] = line_target
        line_json["transl"] = line_input
        line_idx[str(idx_json)] = line_json
        json.dump(line_idx, fw, ensure_ascii=False)
        fw.write("\n")
        line_to_sent = ""
        idx_json += 1
        lehv_arr.append(lehv)
        if lehv >0.5:
          print('large')
          print(line)
          print()
      elif "target" in line:
        line_target="".join(line.split(',')[2:]).strip().replace('.','')
        print(line_target)
        #print(Levenshtein.distance(line_target, line_input))
      else:
        raise(KeyError)

      line_idx2+=1

      if False:
        for line_in_splitted in line_splitted:
          if len(line_in_splitted.strip())>3:
            line_to_sent+=line_in_splitted.strip()+" "
            if idx==1:
              #print(line_to_sent)
              line_json=dict()
              line_idx=dict()
              #line_transl=""
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
print(max(lehv_arr))
print(np.mean(lehv_arr))
print(np.std(lehv_arr))
print(lehv_arr)