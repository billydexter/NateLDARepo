import json


def create_files(tweets, prefix):

    in_files = ["relationship_bins/assoc_words.txt",
                "relationship_bins/child_words.txt",
                "relationship_bins/friend_words.txt",
                "relationship_bins/parent_words.txt",
                "relationship_bins/relative_words.txt",
                "relationship_bins/sib_words.txt",
                "relationship_bins/sig_other_words.txt",
                "relationship_bins/sub_words.txt",
                "relationship_bins/sup_words.txt"]

    out_files = ["resultingJSON/assoc_words" + prefix + ".json",
                "resultingJSON/child_words" + prefix + ".json",
                "resultingJSON/friend_words" + prefix + ".json",
                "resultingJSON/parent_words" + prefix + ".json",
                "resultingJSON/relative_words" + prefix + ".json",
                "resultingJSON/sib_words" + prefix + ".json",
                "resultingJSON/sig_other_words" + prefix + ".json",
                "resultingJSON/sub_words" + prefix + ".json",
                "resultingJSON/sup_words" + prefix + ".json"]

    for i in range(0, len(in_files)):
        open_one_file(in_files[i], out_files[i], tweets)

def open_one_file(inFilename, outFilename, tweets):
    print("Reading from " + inFilename + " to " + outFilename + ".")
    a_file = open(inFilename, "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists. append(line_list[0].lower())
    a_file.close()
    list_of_lists = set(list_of_lists)
    keptTweets = {}
    keptTweets['tweets'] = []
    for i in tweets:
        j = set(i)
        if bool(j & list_of_lists):
            keptTweets['tweets'].append(i)

    with open(outFilename, 'w') as outfile:
        json.dump(keptTweets, outfile)