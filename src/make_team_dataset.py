import pandas as pd
from bs4 import BeautifulSoup
import requests

data = pd.DataFrame()

for year in range(1977, 2021):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + ".html"
    page = requests.get(url)

	# selects the table from the webpage		
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(
        lambda tag: tag.name == "table"
        and tag.has_attr("id")
        and tag["id"] == "advanced-team"
    )

    table_head = table.find("thead").findAll("tr")[1]
    table_body = table.find("tbody").findAll("tr")

	# extracts data from table head
    column_headers = [th.getText() for th in table_head]
    filtered_column_headers = list(filter(lambda t: t != " ", column_headers))[1:]

	# actual data from the table
    team_data = [
        [td.getText() for td in table_body[i].findAll("td")]
        for i in range(len(table_body))
    ]

	# integration with the master dataframe
    df = pd.DataFrame(team_data, columns=filtered_column_headers)
    df["Year"] = year
    data = pd.concat([data, df])
    print(year)

data.to_csv('../data/teams.csv')