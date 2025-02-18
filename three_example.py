{"messages": [{"role": "system", "content": "You translate between South Ostrobothnia dialect and standard Finnish."},
              {"role": "user", "content": "Dialect: Miehet tulivat pirttiin."},
              {"role": "assistant", "content": "Standard Finnish: Miehet tulivat tupaan."}]}
{"messages": [{"role": "system", "content": "Translate between South Ostrobothnia dialect and standard Finnish."},
              {"role": "user", "content": "Translate to standard Finnish: 'Miehet tulivat pirttiin.'"},
              {"role": "assistant", "content": "Miehet tulivat tupaan."}]}
{"messages": [{"role": "system", "content": "Translate between South Ostrobothnia dialect and standard Finnish."},
              {"role": "user", "content": "Translate to dialect: 'Miehet tulivat tupaan.'"},
              {"role": "assistant", "content": "Miehet tulivat pirttiin."}]}

{"messages": [{"role": "system", "content": "You are a storyteller who writes in the South Ostrobothnia dialect of Finnish."},
              {"role": "user", "content": "Tell me a story about farm life."},
              {"role": "assistant", "content": "Oli kerran vanha isäntä, joka heräs joka aamu auringon nousun aikaan..."}]}

{"messages": [{"role": "system", "content": "You write in South Ostrobothnia dialect. Predict the next words based on the given context."},
              {"role": "user", "content": "Pirteissä aamun valossa isäntä nousi ja astui..."},
              {"role": "assistant", "content": "ulos katsomaan säätilaa."}]}

import json

# Test examples
test_data_english = [
    {"messages": [
        {"role": "system", "content": "Translate between South Ostrobothnia dialect and standard Finnish."},
        {"role": "user", "content": "Dialect: Miehet tulivat pirttiin."},
        {"role": "assistant", "content": "Standard Finnish: Miehet tulivat tupaan."}
    ]},
    {"messages": [
        {"role": "system", "content": "You write in South Ostrobothnia dialect. Predict the next words based on the given context."},
        {"role": "user", "content": "Pirteissä aamun valossa isäntä nousi ja astui..."},
        {"role": "assistant", "content": "ulos katsomaan säätilaa."}
    ]}
]

test_data_finnish = [
    {"messages": [
        {"role": "system", "content": "Käännä Etelä-Pohjanmaan murteen ja yleiskielen välillä."},
        {"role": "user", "content": "Miehet tulivat pirttiin."},
        {"role": "assistant", "content": "Miehet tulivat tupaan."}
    ]},
    {"messages": [
        {"role": "system", "content": "Kirjoitat Etelä-Pohjanmaan murteella. Ennusta seuraavat sanat annettuun tekstiin."},
        {"role": "user", "content": "Pirteissä aamun valossa isäntä nousi ja astui..."},
        {"role": "assistant", "content": "ulos katsomaan säätilaa."}
    ]}
]

# Save as JSONL files
with open("test_english.jsonl", "w", encoding="utf-8") as f:
    for entry in test_data_english:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

with open("test_finnish.jsonl", "w", encoding="utf-8") as f:
    for entry in test_data_finnish:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print("Test datasets saved: test_english.jsonl & test_finnish.jsonl")
