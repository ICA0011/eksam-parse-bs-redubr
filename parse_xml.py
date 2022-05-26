from bs4 import BeautifulSoup
import requests

def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content, 'lxml')
  
  # your code here
  input_tag = soup.find_all("data")
  str_p1 = str(input_tag).replace("[<data>", "")
  value = str_p1.replace("</data>]", "")

  return value.replace(" ", "").replace("\n", "").replace("\r", "")
