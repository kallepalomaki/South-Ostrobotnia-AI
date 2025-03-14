import faiss
import numpy as np
import openai
import json
import openai
import os

with open("../openai.key") as f:
    openai.api_key = f.read().strip().replace("OPENAI_API_KEY=","")

# File paths for storage
FAISS_INDEX_PATH ="../data/faiss_index.bin"
MAPPING_PATH = "../data/id_to_text.json"

client = openai.OpenAI(api_key=openai.api_key)
idx=0
sentence_pairs=[]
with open("../data/out_partially_corrected.json") as f:
    for line in f:
        data=json.loads(line)
        target_data =data[list(data.keys())[0]]["orig"]
        input_data = data[list(data.keys())[0]]["transl"]
        sentence_pairs.append({"standard": input_data, "dialect": target_data})
        if idx > 2:
            break
        idx+=1

print(sentence_pairs)
# Example data
#sentence_pairs = [
#    {"standard": "Minä olen jo menossa.", "dialect": "Mää oon männä jo."},
#    {"standard": "Täällä ollaan huonosti.", "dialect": "Täälä ollahan häjysti!"},
#]

# Generate embeddings


def get_embedding(text):
    response = client.embeddings.create(input=[text], model="text-embedding-ada-002")
    return np.array(response.data[0].embedding, dtype=np.float32)


# Check if FAISS index exists
if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(MAPPING_PATH):
    print("Loading existing FAISS index and mappings...")

    # Load FAISS index
    index = faiss.read_index(FAISS_INDEX_PATH)

    # Load ID-to-text mapping
    with open(MAPPING_PATH, "r") as f:
        id_to_text = json.load(f)

else:

    # Store embeddings in FAISS
    index = faiss.IndexFlatL2(1536)  # 1536 dimensions for OpenAI embeddings
    embeddings = []
    id_to_text = {}

    for i, pair in enumerate(sentence_pairs):
        print(i)
        emb = get_embedding(pair["standard"])
        embeddings.append(emb)
        id_to_text[str(i)] = pair["dialect"]

    index.add(np.array(embeddings))
    faiss.write_index(index,FAISS_INDEX_PATH)

    with open(MAPPING_PATH, "w") as f:
        json.dump(id_to_text,f, ensure_ascii=False)

# Query with standard Finnish
#query = "Olen aina ollut vähän kovaääninen eikä ääneni siellä rintamaitovieroituksessa ainakaan hiljentynyt"
query = "Aitan ovelta huusin matkalaiselle, hevosella pääsee lujaa! "
query_embedding = get_embedding(query)
_, indices = index.search(np.array([query_embedding]), k=3)

# Fetch the corresponding text (document chunks) for these indices
retrieved_chunks = [id_to_text[str(idx)] for idx in indices[0]]

# Combine the selected chunks as context
context = "\n\n".join(retrieved_chunks) + '\npääsee -> pääsöö\naitassa -> puaris' # Concatenate chunks

print(context)

def chat_completion(context, query, flag_full):
    if flag_full:
        query_full=f"Context:{context}\n\nQuestion:{query}"
    else:
        query_full=query
    completion = client.chat.completions.create(
    model="ft:gpt-4o-2024-08-06:personal::B3poyXlC",
    #model= "ft:gpt-3.5-turbo-0125:personal::B1eKaRYa",
    #model="gpt-4o-2024-08-06",
      messages=[
        {"role": "system", "content":  "You translate standard Finnish sentences into the South Ostrobothnian dialect."},# Use colloquial expressions and dialect-specific words.
        {"role": "user", "content": query_full}
      ],
    temperature = 1.0 # Deterministic output
    #top_p = 1,  # Full probability distribution
    )


    return completion.choices[0].message

print(chat_completion(context=context, query=query, flag_full=1))