import requests
import json
from bs4 import BeautifulSoup


article_list = []

#search results for "orchid hunters" in Chronicling America databse 
base_url = "https://chroniclingamerica.loc.gov/search/pages/results/?state=&dateFilterType=yearRange&date1=1777&date2=1963&language=&ortext=&andtext=&phrasetext=&proxtext=Orchid+Hunters&proxdistance=5&rows=500&searchType=advanced"



r = requests.get(base_url) 


if r.status_code == 200: 
	soup = BeautifulSoup(r.text, features="html.parser")
	paper = soup.find_all("div",{"class":"highlite"}) 
	count = 0
	for paper_item in paper:
		count = count + 1
		if paper_item != None: 
			try:
				paper_a = paper_item("a")
				image_a = (paper_a[1]) #only prints the a element with the title, date, location, image name 
				title_image = image_a.text
				newspaper = title_image.partition(".")[0].strip()
				restof = title_image.partition(".")[2].strip()
				newspaper_type = restof.partition("(")[0].strip()
				restof2 = restof.partition("(")[2].strip()
				location = restof2.partition(")")[0].strip()
				restof3 = restof2.partition(")")[2].strip()
				date1 = restof3.partition("I")[0].strip()
				date2 = date1.partition(",")[2].strip() #[:1] eliminated entire string instead of stripping first character 
				date = date2[:-1] #eliminates last character 
				restof4 = restof3.partition(",")[2].strip()
				restof5 = restof4.partition(",")[2].strip()
				np_image_num = restof5.partition(",")[2].strip()
				url_a = paper_a[0]
				url_src = url_a("img") #list needs to convert to string
				url_src_string = "".join(map(str, url_src)) #converted list to string
				url_src_string_part1 = url_src_string.partition("src=\"")[2]
				url_src_string_part2 = url_src_string_part1.partition("\"/")[0] #strips down to src url 
				paperimage = paper_item("input")
				papertext_url_base = "".join(map(str, paperimage))
				papertext_url_base1 = papertext_url_base.partition("value=\"")[2]
				papertext_url = papertext_url_base1.partition("\"")[0]+"ocr"
				print(title_image)
				print(papertext_url)

			except: 
				print("Couldn't scrape")
		else:
			print("N/A")
		print("----------------------------")
		print(count)

		articlelist_item = {

								"article_info" : title_image,
								"article_text_url" : papertext_url


								}

		article_list.append(articlelist_item)

		with open("orchids.json", "w") as orchidsfile:
			json.dump(article_list, orchidsfile, indent=2)
	
		


