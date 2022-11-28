import requests
from bs4 import BeautifulSoup as bs

base_url = "https://ugandatourismcenter.com/list-of-tour-operators-and-travel-companies-in-uganda/"
req = requests.get(base_url)

soup = bs(req.content, 'html.parser')

# filter throught the htmp tags
table = soup.find('div', attrs={'class': 'post-content'})
new_table = table.findAll("li", attrs={'style': 'list-style-type: none;'})

companies = []

# loop through the table and get the data
for i in range(0, len(new_table)):
	cur_table = new_table[i]
	for row in cur_table.findAll("li"):
		# Create array of the text in the row
		text_list = (row.text).split('\n')
		company = {
			'campany_name': text_list[0],
			'address': text_list[1],
			'telephone': text_list[2],
			'website': text_list[3] if len(text_list) == 4 else ''
		}
		companies.append(company)

print(companies)