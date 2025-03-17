import json
from fuzzywuzzy import process

dialect_with_standard_key=dict()
with open("../data/out_partially_corrected.json","r") as f:
    for line in f:
        data=json.loads(line)
        dialect_with_standard_key[data[list(data.keys())[0]]["orig"]]=data[list(data.keys())[0]]["transl"]

idx_match=0
story_idx=0
dialect=dict()
standard=dict()
with open('../data/pohopekka_stories.json') as f:
    for line in f:
        story=json.loads(line)["content"]
        story_splitted=story.split(". ")
        inside_story_idx=0
        for sentence in story_splitted:
            best_match = process.extractOne(sentence, dialect_with_standard_key.keys())
            if best_match[1]>90:
                matched_key = best_match[0]
                print(matched_key)
                print(sentence)
                print(dialect_with_standard_key[best_match[0]])
                print(idx_match)
                dialect[str(story_idx) + "-" + str(inside_story_idx)] = sentence
                standard[str(story_idx) + "-" + str(inside_story_idx)] = dialect_with_standard_key[best_match[0]]
                idx_match+=1
            inside_story_idx+=1
        story_idx+=1


print(dialect)
with open("../data/standard_finnish_sentences.json","w") as f:
    json.dump(standard, f, ensure_ascii=False)