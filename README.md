# Twitter Analysis GOI
The main motive behind this project was to take advantage of the power of Social Media to understand how official Indian Government handles function on twitter. By analysing Twitter data we can easily understand which GOI handles focus on which core issues and policies.
Analysis was performed on Twitter data of 115 official Government Handles on about 350,000 tweets using Python. The Twitter API was used to collect all the data.

## DATA
The enitre dataset was collected through the twitter api using a python script. 3.5 Lakh tweets were collected over 115 different Twitter Handles. The data is stored in JSON format.
Preliminary data preprocessing was done to remove empty tweets, links, emoticons, etc.


## Analysis

###  Mentions
An adjacency list was created on the basis of mentions of other handles in the tweets. The list was then converted to a directed graph.
Clustering algorithms were applied over this graph to group the handles into several clusters based on who interact with each other very often.<br /><br />
<img src="https://raw.githubusercontent.com/siddharthkhincha/Twitter-Analysis-GOI/master/graphs/directed_graph_col.png" width ="550" height="500"/>
<br /><br />Used Node2Vec to convert the directed graph into 2 dimensional embedding vectors and applied the KMeans algorithm to form clusters on those embedding vectors.<br /><br />
<img src="https://raw.githubusercontent.com/siddharthkhincha/Twitter-Analysis-GOI/master/graphs/KMeans_Seaborn.png" width="550">

### Time
Looked at the different time the handles tweeted at.<br /><br />
<img src="https://raw.githubusercontent.com/siddharthkhincha/Twitter-Analysis-GOI/master/graphs/finat_tweets_time_default.png" width ="550" height="400" />

### Hashtags
Analysed all the different hashtags being used in the dataset as they are a great indicator of which topic each handle tends to tweet about.  Created a list of unique hashtags by using regex to find all the hashtags and maintaining a list of all hashtags encountered until then.There are 21164 unique hashtags.<br />Then created a pandas dataframe with all the hashtags as the rows and the handles as the columns mapping the number of times each hashtag was used by the different handles. This will be useful for later analysis. 

---


