import requests, re
from bs4 import BeautifulSoup
import json
main_page_link="https://www.blogit.fi/helmiä-lakeudelta"

page=requests.get(main_page_link)
soup = BeautifulSoup(page.content, 'html.parser')
links=soup.find_all("a")
def add_space_after_dot_comma(text):
    # Define a regular expression pattern to match dot or comma not followed by a space
    pattern = r'(?<=[.,])(?=[^\s])'

    # Use re.sub() to replace dots and commas with space after them
    text_with_spaces = re.sub(pattern, ' ', text)

    return text_with_spaces


data_list=[]
cnt_title=0
titles=[]
with open("../data/helmia_stories.json", "w", encoding="utf-8") as f:
    for link in links:
        print(link)
        page_data=link.get("href")
        if page_data:
            if "helmia" in page_data:
                data_dict = dict()

                print(link.get("href"))
                page2 = requests.get(link.get("href"))
                soup2 = BeautifulSoup(page2.content, 'html.parser')
                data = soup2.find_all(["h1","div"], {"class": ["entry-title","entry-content"]})
                for item in data:
                    if item.name == "h1" and "entry-title" in item.get("class", []):
                        # Start a new entry when a title is found
                        current_title = item.get_text().replace("\xa0", " ").replace("\n", " ")
                        cnt_title+=1
                        #entries.append({"title": current_title, "content": []})
                    elif item.name == "div" and "entry-content" in item.get("class", []):
                        # If content is found, associate it with the last title (if any)
                        content_text = item.get_text().replace("\xa0", " ").replace("\n", " ")
                        content_text = re.sub(r"\.(\w)", r". \1", content_text)
                        if cnt_title==0:
                            current_title="No title"
                        if not(current_title in titles):
                            print(current_title)
                            data_dict["title"]=current_title
                            data_dict["content"]=content_text
                            json.dump(data_dict,f,ensure_ascii=False)
                            f.write("\n")
                            titles.append(current_title)

                        cnt_title=0
