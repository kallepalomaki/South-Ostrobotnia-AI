import requests
from bs4 import BeautifulSoup
import re

main_page_link="http://pohopekka.blogspot.com/"

page=requests.get(main_page_link)
soup = BeautifulSoup(page.content, 'html.parser')
text=soup.find_all("div", {"class": "blogPost"})
with open("pohopekka.txt", "w") as f:
    for item in text:
        item_text=item.text
        line_splitted=item_text.split("\n")
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
