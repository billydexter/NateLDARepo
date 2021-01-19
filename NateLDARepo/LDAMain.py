#The main function of the LDA preparation so far. To run this file so far, run
#"python LDAMain.py [filenames]. It will read all the files and convert them into documents
#and words, so the gibbs sort and LDA can be ran on them.

#if the import statements don't work, try from NateLDARepo.FileToDocument import filesToDocuments
#for each level.
from FileToDocument import filesToDocuments
from PoissonSampling import PoissonSampling
from SampleData import getSampleData1
from WordSample import WordSample
import sys

poissonSampler = PoissonSampling()
wordSampler = WordSample()
files = []
#Get the file arguments from the command line.
for i in range(1, len(sys.argv)):
    files.append(sys.argv[i])
#Turns the files into separated strings of text.
documents = filesToDocuments(files)
#Gets the number of words from each documents based on Poisson Distribution.
wordCounts = poissonSampler.getPoissonSampleNumber(documents)
#Randomly samples words from the document
words = wordSampler.getRandomWordsForEachDocument(wordCounts, documents)
#prints the words to the console. Not the end goal, but just to see what it's like.
print(words)

