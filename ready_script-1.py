    #####################
##### READY_SCRIPT-1.PY #####
#   #####################   #
#                           #
#### Program information ####
program = "Ready Script 1"  #
author  = "Vera Lo"         #
version = "v.0.2-3a"        #
#############################

#################################################################
### [SET THE FOLLOWING] (3) [VALUES] : (nr, directory, and files)
#################################################################
# the number of the element of the filenames in the following list
nr=0 # e.g.: nr=0 --> translates to "files[nr]" or 1st file
######### When not sure set nr=0 then only put 1 file in files[0] 
################################################################
# the text files in directory declared below 
files=["business.txt", "productivity.txt", "xcom2.txt"] # files
#
#########
################################################################
# the directory where the previously declared files are
directory="texts" # directory with files
#########
################################################################
#   [SET THESE VALUES, ELSE THE SCRIPT WILL NOT REALLY WORK!!!]
################################################################

# imports
import re
import subprocess
import heapq
import pyttsx3
import nltk

# get python version
python_version = subprocess.run(['python', '--version'], stdout=subprocess.PIPE, text=True)

# nltk library
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

# the constructed path which has file <- filenames[nr]
path_name = f"./{directory}/{files[nr]}"

# credits function
def credits():
    prog = program
    ver = version
    auth = author
    print("\n" + prog)
    print("\n\nVersion: " + ver + "\nAuthor: " + auth)
    ### Python version
    print("Python: " + python_version.stdout + "\n")

# open up a file from path_name for reading
with open(path_name, 'r', encoding="utf-8") as f:
    article_text = f.read()

### Text cleaning ###
# Removing square brackets and extra spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
# Any whitespace character \s+
article_text = re.sub(r'\s+', ' ', article_text)
# Any special characters and digits
formatted_article_text = re.sub('[^a-zA-Z©]', ' ', article_text)
# Any whitespace character
formatted_article_text = re.sub(r'\s+', ' ', article_text)
title = "Your title is: \"" + article_text[0:25] + "\""

### Lexicon ###
# Convert paragraphs to sentences
sentence_list = nltk.sent_tokenize(article_text)

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)

### Final ingredients ###
# listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
print(rate)

engine.setProperty('rate', 121)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def save(filen):
    engine.save_to_file(formatted_article_text, filen)

### Summary ###
print(summary)

### Splash audio
ready = []
ready.append("Your Ready Script, amazing.")
ready.append("Please help support this model, by visiting our repository at github dot com slash decode witness")

for i in ready:
    talk(i)

### Title ###
print(title)
talk(title)

### Paragraphs reference ###
print(formatted_article_text)

### Audio ###
talk(formatted_article_text)

### (uncomment for:) Unedited article text ;; for your reference ###
# print(article_text)
# talk(article_text)

### Credits ###
credits()