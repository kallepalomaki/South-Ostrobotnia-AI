import requests
from bs4 import BeautifulSoup
import re
import json

main_page_link="http://pohopekka.blogspot.com/"
structured_data = []
page=requests.get(main_page_link)
soup = BeautifulSoup(page.content, 'html.parser')
#text=soup.find_all("div", {"class": "blogPost"})
for element in soup.find_all(["h2", "div"]):
    if element.name=="h2":
        latest_h2 = element.text.strip()
    elif element.name=="div" and "blogPost" in element.get("class", []):
        if latest_h2:
            if "porsta" in latest_h2:
                print("here")
            content=element.text.split("# posted")[0].strip().replace('\r',' ').replace('PEKAN SIVUPERSOONA','').\
                replace('Pekan Sivupersoona','').replace("\n"," ")
            if "--" in content:
                print(content)

            content=content.split("----",1)[0].strip()

            if len(content)>5:
                structured_data.append({"title": latest_h2, "content": content})
            latest_h2 = None

with open("../data/pohopekka_stories.json", "w", encoding="utf-8") as f:
    for item in structured_data:
        #line_splitted=item_text.split("\n")
        #if "posted" in item["content"]:

        print(item["title"])
        print(item["content"])
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")



