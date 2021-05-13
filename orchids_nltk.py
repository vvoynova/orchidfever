import nltk
#already downloaded
#nltk.download("punkt")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np

all_words = []
word_items =[]
sorted_words_list = []

#Content for WordClouds
entities = {}
regular_words = {}
all_orchid_words = {}


with open ("orchidtext.txt", "r") as orchidarticles:
	text = orchidarticles 
	stop_words = set(stopwords.words("english"))
	#for loose characters, gibberish, stop words not included in NLTK corpus stopwords or wordcloud STOPWORDS 
	custom_stop_words = ",",".","!", "?", ":", ";", "''","``", "said", "In", "It", "'", "’", "(", ")","[", "]", "”", "“", "«", "ofthe", "andhe", "Each", "each", "From", "from", "There", "San", "Ho", "Here", "Why", "Ir", "Ii", "with", "With", "Mrs.", "Mrs", "Miss", "Mr", "la", "el", "La", "El", "go", "back", "000", "Some", "Not", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "Dr.", "However", "however", "American", "Although", "although", "Almost", "almost", "will", "Will", "ho", "Into", "even", "around", "Around", "ago", "came", "Coming", "coming", "st", "St", "St.", "st.", "Place", "New", "every", "re", "make", "Make", "will", "quick", "Quick", "during", "During", "iff", "Iff", "th", "orchidorchid", "orchidorchidorchid", "Mc", "Ir", "Id", "Hon", "Sho", "Even", "Finally", "Well", "Sometimes", "Never", "know", "Know", "Get", "Got", "get", "got", "Made", "made", "Ever", "put", "never", "ever", "Put", "Once", "Il", "Ii", "Ihe", "Two", "Three", "Ithad", "Without", "intothe", "way", "Their", "Tho", "How", "Like", "Many", "nameyou", "Only", "That", "Yes", "yes", "will", "say", "no", "No", "Among", "Here", "These", "For", "By", "Every", "theonly", "ama", "llko", "ono", "badand", "orthe", "en", "anda", "tne", "tha", "bo", "ot", "another", "Another", "much", "Much", "Nor", "In", "Inthe", "Before", "After", "My", "Of", "How", "More", "So", "On", "What", "Who", "Where", "While", "Now", "Ing", "Inthe", "First", "By", "Never", "All", "Sometimesa", "Been", "Have", "An", "Other", "other", "Wherever", "More", "more", "some", "de", "11", "His", "his", "Her", "her", "As", "as", "partsof", "really", "Really", "might", "■", "within", "nnd", "well", "like", "Its", "I1", "says", "Says", "Saying", "saying", "Ft.", "ft.", "Maybe", "maybe", "Just", "just", "Ih", "%", "thereis","willnot", ": ", "11111", "with", "already", "without", "ones", "us", "Us", "--", "But", "When", "ed", "Ed", "ofthe", "aro", "al", "nd", "lo", "atthe", "ir", "ns", "butthe", "nt", "oi", "ui", "mo", "tl", "io", "oneof", "whichthe", "id", "wo", "te", "de", "De", "ii", "one,", "One", "Must", "upon", "He", "he", "Must", "must", "come", "may", "go,", "Then", "They", "they", "at", "At", "This", "inno", "witha", "Oh", "shall","Both", "She", "she", "We", "we", "Perhaps", "•", "•", "•", "th", "the", "n't", "To", "Ago", "though", "'s", "tho", "Mr.", "Mrs.", "Miss","-", "would", "could", "should", "If", "And", "Or", "The","You", "Is", "<", ">", "*", "&", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", "K.", "L.", "M.", "N.", "O.", "P.", "Q.", "R.", "S.","T.", "U.", "V.", "W.", "X.", "Y.", "Z.", "a.", "b.", "c.", "d.", "e.", "f.", "g.", "h.", "i.", "j.", "k.", "l.", "m.", "n.", "o.", "p.", "q.", "r.", "s.", "t.", "u.", "v.", "w.", "x.", "y.", "z.", "■■", "r1", "T_", "io", "vd", "t-", "r1", "tn", "'ll", "23", "pr", "0", "fr", "sr", "er", "jr.", "_r", "le", "ea", "Oa", "jr.", "whov", "Vcj", "lilfcr", "iv", "ti", "ci", "ii", "aide-1", "li", "Ls", "ki", "aduf", "iici", "Oi", "tne", "■", "of|", "I|", "ca", "c-tyr", "o-t", "an|", "‘", "‘", "tme", "tuml", "hl", "frt", "Zd", "ha", "wa", "wa", "pnt", "I-", "ly", "'d", "-s", "laiii'iii", "imii", "Jiimmii", "Mg", "nt", "ot", "ut", "ro", "nn", "Ho", "lu", "iiiiitlled", "tne", "|they", "#", "T^f", "Sa", "jl", "Jor", "1j", "ij", "jj", "sl3", "•M", "inter-", "i|", "of|", "vs", "||", "•j", "with|", "_", "_", "_", "New|", "to|", "°", "Dr.", "|", "a|", "the|", "The|", "I|", "Md", "Fm", "|", "ta", "'■", "oo", "ct", "ct.", "-S", "iv", "Ki", "Yd", "fr", "»", "ndlllh", "curt", "hi", "ttl", "hlthrto", "ltit", "1101111101", "Graham", "ii", "unknowr", "Clarke", "Hoppington", "Evelyn", "Whenthey", "Someyear", "tint", "lud", "ii", "tint", "1111", "tt", "willalso", "willtiltoalso", "110", "rciurn", "rt", "ret", "itt", "ivit", "hi", "Iii", "wonderful", "Irflll", "Hiiowwhiin", "Hiiowwhiinflower", "eli", "uowwhl", "hit", "ustflower", "Illnn", "Illdt", "dcxrlbed", "dcxrlbedn", "c1rlras", "Ii", "llggest", "iggint", "oicliicls", "Ild", "huids", "ril", "Mrht", "Mrhtof", "llht", "llhtorof", "whih", "thlll", "Unrinull", "Ihlt", "Ihlt", "Inr11", "Captain", "tlunt", "Itutrinuilt", "Unrinull", "Inr11", "Ihlalpllll", "Bariatiratills"
	

	
	
	#getting word tokens for each line: 
	for line in (text):
	  	filtered_line = (word_tokenize(line))
	  	for word in filtered_line:
	  		if word not in stop_words and word not in custom_stop_words:
	  			all_words.append(word) 
	

	words_already_done = []			
	for a_word in all_words:
		if a_word not in words_already_done:
			count = all_words.count(a_word)
			words_already_done.append(a_word)
			


		#all words and their frequency
		word_item = {

					"word" : a_word,
					"count" : count

					}


		#appending words to empty dictionaries for wordclouds 

		#named entities 
		if word_item["count"] > 10 and word_item["word"][0].isupper():
			if word_item["word"] not in entities and (word_item["word"] != "Orchid" or "Orchids"):
				entities[word_item["word"]] = word_item["count"]	
		
		#all words minus named entities 	
		if word_item["count"] > 10 and word_item["word"][0].islower():	
			if word_item["word"] not in regular_words:
				regular_words[word_item["word"]] = word_item["count"]

		#ALL words 
		if word_item["count"] > 10 and word_item["word"] not in all_orchid_words:
			all_orchid_words[word_item["word"]] = word_item["count"]


#Wordcloud Appearance 
custom_mask = np.array(Image.open("flower_blue.png"))
entities_wordcloud = WordCloud(width = 2000, height = 2000, background_color = "white", stopwords = STOPWORDS, mask = custom_mask).generate_from_frequencies(entities)

custom_mask = np.array(Image.open("pinkstem_flower.png"))
orchids_wordcloud = WordCloud(width = 2000, height = 2000, background_color = "white", stopwords = STOPWORDS, mask = custom_mask).generate_from_frequencies(regular_words)

custom_mask = np.array(Image.open("orchid_yellow.png"))
allorchids_wordcloud = WordCloud(width = 2000, height = 2000, background_color = "white", stopwords = STOPWORDS, mask = custom_mask).generate_from_frequencies(all_orchid_words)


#Use for plotting. When you're done plotting, toggle the plots and turn on the png files below. 
# plt.figure(figsize=(15,8))
# plt.imshow(entities_wordcloud, interpolation = "bilinear")
# plt.show()


# plt.figure(figsize=(15,8))
# plt.imshow(orchids_wordcloud, interpolation = "bilinear")
# plt.show()



# plt.figure(figsize=(15,8))
# plt.imshow(allorchids_wordcloud, interpolation = "bilinear")
# plt.show()



#PNG files for wordclouds 
entities_wordcloud.to_file("entitieswc.png")
orchids_wordcloud.to_file("orchidwordswc.png")
allorchids_wordcloud.to_file("allorchidwordswc.png")

print("Done!")








