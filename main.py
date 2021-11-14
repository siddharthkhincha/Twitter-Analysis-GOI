import os, json
from googletrans import Translator
import re
translator = Translator()

def unique_hashtags:
	json_files = [pos_json for pos_json in os.listdir("./data") if pos_json.endswith('.json')]
	count = 0
	hashtags=["hashtags"]
	for file in json_files:
		file = open('./data/'+file)
		data = json.load(file)
		for tweet in data:
			curhash = re.findall(r"#(\w+)", tweet['text'])
			if curhash != []:
				for curtag in curhash:
					flag = 0
					for tag in hashtags:
						if tag == curtag:
							flag=1
							
					if flag == 0:
						hashtags.append(curtag)
		count+=len(data)
		return np.array(hashtags)
for hashtag in unqiue_hashtags:
	print(hashtag)
print(count," tweets")
print(len(hashtags)," hashtags")