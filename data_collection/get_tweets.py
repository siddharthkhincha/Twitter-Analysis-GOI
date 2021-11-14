import tweepy
import json
import pandas as pd

API_KEY="T0abNoHgqGiYnQYlD57eaaa7O"
API_KEY_SECRET="KvHYjnOs19JI1BweNo7w6SV9UhT0EpeDaABXKaIaKHZejMT0Eg"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAAPGTgEAAAAAHo%2Faz4XpjHB0rDM%2FAfqc6Tpua4E%3DtifMbB4Zabdi4NNtmdYPl8Ulj0VnlQidAtDkq6EMwINIbyFuxX"
consumer_key = "T0abNoHgqGiYnQYlD57eaaa7O"
consumer_secret = "KvHYjnOs19JI1BweNo7w6SV9UhT0EpeDaABXKaIaKHZejMT0Eg"
access_key = "1347563467209809920-abfRMNANFYpiK9hCsQ8oFD1L9YRzuq"
access_secret = "5PYrJwoTX2CDyocGVxovaYSoWeTKWxYoSxb7NXMhwLFp0"

def initialize(name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    #print("Authenticated\n")
    cursor = tweepy.Cursor(api.user_timeline, screen_name = name, wait_on_rate_limit=True)
    tweets = [x._json for x in cursor.items()]
    #print("Downloaded\n");
    save_file = open(name + '.json','w')
    json.dump(tweets,save_file,indent=4)
    save_file.close()
    
    return len(tweets)

if __name__ == '__main__':
    #name = str(input("Handle of the Twitter user:"))
    df = pd.read_csv("handles.csv")
    for i in range(0,df.shape[0]):
        if df['Downloaded'][i]==0:
        
            print(df['Description'][i]+" has ",str(initialize(df['Handle'][i]))," tweets")
            
        
    #print(initialize(name))
