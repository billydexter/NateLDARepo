import json
from GibbsSamplingFunctions import organizeData

#Extracts the json file from the earlier data. Separated to save performance.
tweetList = []
with open("WindowsTweetDocuments.json") as file:
    data = json.load(file)
    tweetList = data['tweets']


#maybe add something later

formattedTweetList, wordDictionary = organizeData(tweetList)

print("done")