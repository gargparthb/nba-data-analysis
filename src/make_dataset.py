import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

url = "https://www.basketball-reference.com/leagues/NBA_2022.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(
  lambda tag: tag.name == "table"
  and tag.has_attr("id")
  and tag["id"] == "advanced-team"
)

tbody = table.find("tbody")
trs = tbody.findAll("tr")

for tr in trs:
  tds = tr.find_all('td')
  for td in tds:
    print(td.text)