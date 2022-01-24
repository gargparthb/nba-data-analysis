import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import os

data = pd.DataFrame()

for year in range(1990, 2021):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + ".html"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(
        lambda tag: tag.name == "table"
        and tag.has_attr("id")
        and tag["id"] == "advanced-team"
    )

    table_head = table.find("thead").findAll("tr")[1]
    table_body = table.find("tbody").findAll("tr")

    column_headers = [th.getText() for th in table_head]
    filtered_column_headers = list(filter(lambda t: t != " ", column_headers))[1:]

    team_data = [
        [td.getText() for td in table_body[i].findAll("td")]
        for i in range(len(table_body))
    ]

    df = pd.DataFrame(team_data, columns=filtered_column_headers)
    df["Year"] = year
    data = pd.concat([data, df])
    print(year)

data.to_csv('../data/teams.csv')