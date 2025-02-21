import json

# Read raw text and split objects
#with open("../data/pohopekka_stories_general_language_title.json", "r", encoding="utf-8") as f:
with open("../data/helmia_stories_general_language_title.json", "r", encoding="utf-8") as f:
    raw_text = f.read().strip()

raw_text=raw_text.replace("\n"," ").replace("}","}\n").replace("    ","").splitlines()
# Split objects using double newlines and filter out empty entries

# Save cleaned JSONL file
with open("../data/dataset_clean.json", "w", encoding="utf-8") as f:
    for line in raw_text:
        json.dump(json.loads(line),f,ensure_ascii=False)
        f.write("\n")