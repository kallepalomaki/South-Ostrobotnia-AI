import json
import random
from IPython.display import display, JSON

from datasets import Dataset

random.seed(42)
messages_list=[]
#with open("../data/out_saved2.json") as f:
def write_translated():
    idx = 0
    question_arr=[]
    complex_cot_arr=[]
    response_arr=[]
    text_arr=[]
    data_arr=[]
    with open("../data/out_partially_corrected.json") as f:
        for line in f:
            #print(line)
            data=json.loads(line)
            target_data=data[list(data.keys())[0]]["orig"]
            input_data=data[list(data.keys())[0]]["transl"]

            print(str(idx)+",target,"+target_data)
            print(str(idx)+",input,"+input_data)

            system_dict=dict()
            input_dict=dict()
            target_dict=dict()
            system_dict["role"] = "system"
            #system_dict["content"] = "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobotnia"
            #{"role": "system", "content":
            #system_dict["content"]="You are a storyteller who writes in the South Ostrobothnian dialect."
            #{"role": "system",
            system_dict["content"]="You translate standard Finnish sentences into the South Ostrobothnian dialect."
            input_dict["role"] = "user"
            input_dict["content"] = "Ilmaise seuraava Etelä-Pohjanmaan murteella: " + input_data

            target_dict["role"] = "assistant"
            target_dict["content"] = target_data
            #question_arr.append(input_data)
            #complex_cot_arr.append("")
            #response_arr.append(target_data)
            #text_arr.append(input_data + " - " + target_data)
            data_arr.append({
                "Question": input_data,  # Standard Finnish
                "Complex_CoT": "",
                "Response": target_data,  # South Ostrobothnian dialect
                "text": input_data + " - " + target_data  # Same as Question and Response
            })


    return data_arr


def write_predict_next_words(input_filename): #(context_length=10, prediction_length=3):

    #def prepare_finetune_data(input_file, output_file, context_length=10, prediction_length=3):
    """
    Converts plain text into OpenAI fine-tuning format for next-word prediction.

    :param input_file: Path to the text file to be processed.
    :param output_file: Path to save the JSONL formatted fine-tuning data.
    :param context_length: Number of words used as input context.
    :param prediction_length: Number of words to predict as completion.
    """
    max_context=10
    max_prediction=1

    words=[]
    with open(input_filename) as f:
        for line in f:
            data=json.loads(line)
            text=data["content"].replace('\n',' ')
            words_story = text.split()
            words.extend(words_story)

    dataset = []

    for i in range(0, len(words) - max_context - max_prediction, 10):
        context_length = random.randint(3, max_context)
        prediction_length = random.randint(1, max_prediction)
        prompt = ' '.join(words[i:i + context_length])
        completion = ' '.join(words[i + context_length:i + context_length + prediction_length])

        dataset.append({
            "messages": [
                {"role": "system", "content": "You predict the next word in the South Ostrobothnian dialect."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion}
            ]
        })

    #with open(output_file, 'w', encoding='utf-8') as f:
    #    for entry in dataset:
    #        f.write(json.dumps(entry) + '\n')

    #print(f"Dataset saved to {output_file} with {len(dataset)} examples.")

    # Example usage:
    # prepare_finetune_data("input.txt", "output.jsonl")
    random.shuffle(dataset)
    test_set=dataset[0:100]
    train_set=dataset[101:200]
    return train_set, test_set



# Open your text file containing stories
input_file = 'stories.txt'  # Replace with your file path
output_file = 'fine_tuning_data.jsonl'

# List of alternative instructions in Finnish



# Function to prepare data for fine-tuning
def finetuning_stories(input_file_name):
    instructions_finnish = [
        "Kirjoita tarina Etelä-Pohjanmaan murteella, joka perustuu seuraavaan otsikkoon:",
        "Laadi tarina Etelä-Pohjanmaan murteella seuraavasta otsikosta:",
        "Keksi tarina Etelä-Pohjanmaan murteella, joka alkaa tästä otsikosta:",
        "Kertoa tarina Etelä-Pohjanmaan murteella, jonka otsikko on tämä:",
        "Aloita tarina Etelä-Pohjanmaan murteella seuraavasta otsikosta:",
        "Kirjoita tarina Etelä-Pohjanmaan murteella, joka syntyy seuraavasta otsikosta:",
        "Muokkaa seuraava tarina tämän otsikon mukaan:",
        "Kuvittele tarina Etelä-Pohjanmaan murteella, joka alkaa tällä otsikolla:",
    ]

    # List of alternative instructions for generating stories in English
    instructions_english = [
        "Write a story in the South Ostrobothnian based on the following title:",
        "Create a story in the South Ostrobothnian from this title:",
        "Generate a story in the South Ostrobothnian starting from this title:",
        "Tell a story in the South Ostrobothnian with this title:",
        "Generate a narrative in the South Ostrobothnian based on this title:",
        "Write a story in the South Ostrobothnian using the following title:",
        "Imagine a story in the South Ostrobothnian that begins with this title:",
        "Express a story in the South Ostrobothnian that evolves from this title:"
    ]
    dataset=[]
    with open(input_file_name, 'r') as file:
        for line in file:
            story = json.loads(line)["content"].strip()  # Clean the story
            title = json.loads(line)["title"].strip()  # Clean the story

            #for _ in range(8):  # Generate 10 variations
            # Randomly select an instruction for Finnish and English
            prompt_finnish = f"{random.choice(instructions_finnish)}\n{title}"
            prompt_english = f"{random.choice(instructions_english)}\n{title}"

            # Create the training examples for both Finnish and English

            dataset.append({
                "messages": [
                    {"role": "system", "content": "You are a storyteller who writes in the South Ostrobothnian dialect."},
                    {"role": "user", "content": prompt_finnish},
                    {"role": "assistant", "content": story}
                ]
            })
            dataset.append({
                "messages": [
                    {"role": "system", "content": "You are a storyteller who writes in the South Ostrobothnian dialect."},
                    {"role": "user", "content": prompt_english},
                    {"role": "assistant", "content": story}
                ]
            })
                # Write both examples to the output file
    return dataset[0:2]



train_set=[]
test_set=[]
if False:
    train_set_tmp,test_set_tmp=write_predict_next_words(input_filename='../data/pohopekka_stories_general_language_title.json')
    train_set_tmp,test_set_tmp=write_predict_next_words(input_filename='../data/helmia_stories_general_language_title.json')
    train_set.extend(train_set_tmp)
    test_set.extend(test_set_tmp)

if True:
    train_set=write_translated()
    display(JSON(train_set))
    print()


if False:
    train_set.extend(finetuning_stories(input_file_name='../data/pohopekka_stories_general_language_title.json'))
    train_set.extend(finetuning_stories(input_file_name='../data/helmia_stories_general_language_title.json'))

print("kekkonen")
if True:
    with open("../data/train_set_deep_seek.json","w") as f:
        json.dump(train_set,f,ensure_ascii=False)
        f.write("\n")

    with open("../data/test_set_deep_seek.json","w") as f:
        for message in test_set:
            json.dump(message,f,ensure_ascii=False)
            f.write("\n")



# List of alternative instructions in Finnish
instructions_finnish = [
    "Kirjoita seuraava tarina Etelä-Pohjanmaan murteella:",
    "Kertoa seuraava tarina Etelä-Pohjanmaan aksentilla:",
    "Puhuttele tarina Etelä-Pohjanmaan alueen kieliopilla:",
    "Kirjoita seuraava teksti Etelä-Pohjanmaan murteella:",
    "Kuvittele, että kerrot tämän tarinan Etelä-Pohjanmaan murteella:",
    "Ilmaise tämä tarina Etelä-Pohjanmaan murteella:",
    "Kirjoita tämä tarina Etelä-Pohjanmaan alueen aksentilla:",
    "Laadi tämä tarina Etelä-Pohjanmaan murteella:",
    "Muokkaa seuraava tarina Etelä-Pohjanmaan kielioppiin:",
    "Käännä tämä tarina Etelä-Pohjanmaan murteelle:"
]

# List of alternative instructions in English
instructions_english = [
    "Write the following story in the South Ostrobothnian accent of Finnish:",
    "Tell the following story using the South Ostrobothnian accent:",
    "Speak the story in the dialect of South Ostrobothnia:",
    "Write this text in the South Ostrobothnian accent:",
    "Imagine you are telling the story in the South Ostrobothnian accent:",
    "Express this story in the South Ostrobothnian dialect:",
    "Write this story in the South Ostrobothnian regional accent:",
    "Create this story in the South Ostrobothnian dialect:",
    "Adapt the following story to the South Ostrobothnian accent:",
    "Translate this story to the South Ostrobothnian dialect:"
]

# List of alternative instructions for generating stories in Finnish
