from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")

dwarf_table = soup.find_all("table")
table_rows = dwarf_table[7].find_all("tr")

temp_list = []
for tr_tag in table_rows:
    td_tags = tr_tag.find_all("td")

    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

headers = ["Name", "Distance", "Mass", "Radius"]
dwarf_data = zip(name, distance, mass, radius)

df = pd.DataFrame(
    list(dwarf_data), 
    columns=headers
    )
df.to_csv("data.csv", index=False)