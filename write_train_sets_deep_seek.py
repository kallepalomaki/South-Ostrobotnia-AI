import random
import requests
from bs4 import BeautifulSoup
import json

def get_pohopekka():
    main_page_link="http://pohopekka.blogspot.com/"
    structured_data = []
    page=requests.get(main_page_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    for element in soup.find_all(["h2", "div"]):
        if element.name=="h2":
            latest_h2 = element.text.strip()
        elif element.name=="div" and "blogPost" in element.get("class", []):
            if latest_h2:
                content=element.text.split("# posted")[0].strip().replace('\r',' ').replace('PEKAN SIVUPERSOONA','').\
                    replace('Pekan Sivupersoona','').replace("\n"," ")

                content=content.split("----",1)[0].strip()

                if len(content)>5:
                    structured_data.append({"title": latest_h2, "content": content})
                latest_h2 = None

    return structured_data

def match_story_sentences_to_standard(stories,standard_finnish_sentences):
    story_idx=0
    dialect=dict()
    for story_ in stories:
        story=story_["content"]
        story_splitted=story.split(". ")
        inside_story_idx=0
        for sentence in story_splitted:
            dialect[str(story_idx) + "-" + str(inside_story_idx)] = sentence
            inside_story_idx+=1
        story_idx+=1


    with open(standard_finnish_sentences) as f:
        standard=json.load(f)

    standard_dialect=[]
    for key in standard:
        standard_dialect.append({"standard":standard[key],"dialect":dialect[key]})
    return standard_dialect

def write_translated(standard_dialect):
    data_arr=[]
    for data in standard_dialect:
        target_data=data["dialect"].strip()
        input_data=data["standard"].strip()
        system_dict=dict()
        input_dict=dict()
        target_dict=dict()
        system_dict["role"] = "system"
        system_dict["content"]="You translate standard Finnish sentences into the South Ostrobothnian dialect."
        input_dict["role"] = "user"
        input_dict["content"] = "Ilmaise seuraava Etelä-Pohjanmaan murteella: " + input_data

        target_dict["role"] = "assistant"
        target_dict["content"] = target_data
        data_arr.append({
            "Question": input_data,  # Standard Finnish
            "Complex_CoT": "",
            "Response": target_data,  # South Ostrobothnian dialect
            "text": input_data + " - " + target_data  # Same as Question and Response
        })


    return data_arr

def __main__():
    stories=get_pohopekka()
    standard_dialect=match_story_sentences_to_standard(stories=stories)
    train_set=write_translated(standard_dialect=standard_dialect,standard_finnish_sentences="../data/standard_finnish_sentences.json")
    random.shuffle(train_set)

    with open("../data/train_set_deep_seek_exp.json","w") as f:
        json.dump(train_set,f,ensure_ascii=False)
        f.write("\n")


