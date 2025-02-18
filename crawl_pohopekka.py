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
            content=element.text.split("# posted")[0].strip().replace('\r','')
            if "--" in content:
                print(content)

            content=content.split("----",1)[0].strip()

            if len(content)>5:
                structured_data.append({"title": latest_h2, "content": content})
            latest_h2 = None

with open("../data/pohopekka_stories.json", "w") as f:
    for item in structured_data:
        #line_splitted=item_text.split("\n")
        #if "posted" in item["content"]:
        if "porsta" in item["title"]:
            print(item["title"])
            print(item["content"])

        print(item["title"])
        print(item["content"])
        json.dump(item,f)


if False:
    for line in line_splitted:
        line_splitted2=line.split(". ")
        d=". "
        s = [e + d for e in line.split(d) if e]
        line_splitted2=s
        for line2 in line_splitted2:
            line_splitted3=line2.split("\r")
            for line3 in line_splitted3:
                line3=line3.strip()
                if (line3 == "") or ("----" in line3):
                    pass
                else:
                    if ("posted" not in line3) and (len(line3)>3):
                        line3=line3.replace(" ."," ").replace("_","").replace("/"," ").replace("!.", "!")
                        line3=re.sub(r'(?<=\S)\.(?=\w)', '. ', line3)
                        f.write(line3 + "\n")
