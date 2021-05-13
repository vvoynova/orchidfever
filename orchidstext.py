import requests
import json
from bs4 import BeautifulSoup
import re

with open("orchids.json", "r") as orchidfile:

	orchid_ocr_data = json.load(orchidfile)
	for data_item in orchid_ocr_data:
		#to get ocr portion of base_url
		ocr_item = data_item["article_text_url"]
		

		base_url = f"https://chroniclingamerica.loc.gov{ocr_item}"

		r = requests.get(base_url)

		if r.status_code == 200: 

			ocr_item_soup = BeautifulSoup(r.text, features="html.parser")
			ocr_text = ocr_item_soup.find("p")
			#printed text of entire page minus html
			ocr_text_string = ocr_text.text 
			ocr_text_string_edit = ocr_text_string.replace(".", ". ")
			ocr_text_string_edit2 = ocr_text_string_edit.replace(",", ", ")
			ocr_text_string_edit3 = re.sub(r"\B([A-Z])", r" \1", ocr_text_string_edit2)


			# ***isolating orchid article from rest of text on page ***
			minus_preorchidtext = ocr_text_string_edit3.partition("orchid")[2]
			minus_preorchidtext2 = ("orchid" + minus_preorchidtext)
			minus_postorchidtext = minus_preorchidtext2.rpartition("orchid")[0]
			orchidtext = (minus_postorchidtext + "orchid")
			

			with open("orchidtext.txt", "a") as orchidtext_file:
				orchidtext_file.write(orchidtext)
					
			


			
			