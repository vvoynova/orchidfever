Orchid Fever in the American Press 
PFCH INFO-664 – Final Project
Vella Voynova

The Orchid Craze of the late 19th century, also known as Orchidelirium or Orchid Fever, inspired a new profession, orchid hunting. Orchid hunters risked (and lost) their lives on dangerous journeys in search of rare, expensive flowers for the wealthy collectors back home. This project used Python to search Chronicling America, a Library of Congress database of digitized historic newspapers, for articles on orchid hunting published between 1881 and 1960. The articles' data and text were scraped with Beautiful Soup. The Natural Language Toolkit helped to analyze the frequency of words and names in article text. Three WordCloud visualizations were created with MatPlotLib. 

The results can be used by anyone with an interest in orchid hunting, and the project can be adapted for searching other topics in Chronicling America.  

Run the code in this order: 

1. orchids4.py
This file pulls digitized images that contain articles about orchid hunting from Chronicling America, uses Beautiful Soup to scrape relevant data, creates URLs for articles’ OCR text, and dumps these URLs in a JSON file. 

2. orchidstext.py
This file opens the JSON file containing OCR text URLs and uses Beautiful Soup to scrape the articles’ text. This code in this file also extracts the orchid article portion of the text. In other words, some images are of an entire article about orchid hunting, while other images contain only a column about orchid hunting. While not a perfect solution, it does this by identifying the first and last mentions of the word “orchid” on the page, and pulling those words and everything in between. Each article is appended to a txt file. 

3. downloadnltk.py 
This code may or may not be necessary for the next step. If you’re getting a persistent “ssl error” when you import Natural Language Toolkit, this code will troubleshoot.  

4. orchids_nltk.py
This file uses Natural Language Toolkit to tokenize each word in the txt file and find the frequency of each word in the entire text file. It removes all stop words in the NLTK corpus. There is a list of custom stop words for gibberish and loose characters that occur due to OCR, but are not identified as stop words by NLTK.
Next, it creates three dictionaries: one for every single word, one for named entities, and one for all words besides named entities. A next step for this project would be to incorporate Stanford NER Tagger in this portion. 
Finally, MatPlotLib creates a wordcloud for each dictionary. 