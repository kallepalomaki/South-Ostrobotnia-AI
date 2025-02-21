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

with open("../data/helmia_stories.json", "w") as f:
    for link in links:
        print(link)
        page_data=link.get("href")
        if page_data:
            if "helmia" in page_data:
                data_dict = dict()

                print(link.get("href"))
                page2 = requests.get(link.get("href"))
                soup2 = BeautifulSoup(page2.content, 'html.parser')
                title = soup2.find_all("h1", {"class": "entry-title"})
                if title[0].a:
                    title_text=title[0].a.text
                else:
                    title_text="No title"
                data_dict["title"]=title_text
                data=soup2.find_all("div", {"class":"entry-content"})
                data1=data[0].find_all("p")
                text=""
                for item in data1:
                    #print(item.text)
                    line_splitted=item.text.split(". ")
                    for line in line_splitted:
                        line_text=line + ". "
                        line_text=add_space_after_dot_comma(line_text.replace("..","."))
                        if len(line_text) > 3:
                            #f.write(line_text + "\n")
                            text+=line_text
                data_dict["content"]=text
                json.dump(data_dict,f)
                f.write("\n")