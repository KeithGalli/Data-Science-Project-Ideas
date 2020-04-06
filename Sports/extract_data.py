import pandas as pd
from bs4 import BeautifulSoup
from urllib import request

website = request.urlopen("https://www.basketball-reference.com/leagues/NBA_2020_per_game.html").read()
soup = BeautifulSoup(website, 'lxml')

table = soup.find('table', attrs={'class': 'sortable', 'id': 'per_game_stats'})

table_headers = [header.text for header in table.find('thead').find_all('th')]
table_rows = table.find_all('tr')

final_data = []
for tr in table_rows:
	td = tr.find_all('td')
	row = [tr.text for tr in td]
	final_data.append(row)

print(table_headers)
df = pd.DataFrame(final_data, columns=table_headers[1:])
df.to_csv('output.csv')