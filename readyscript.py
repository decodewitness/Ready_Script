### Imports ###
import bs4 as bs
from bs4 import BeautifulSoup

import requests
import urllib.request

import re
import sys
import csv

import heapq
import pyttsx3
import pywhatkit

import nltk
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

### Libraries ###
# nltk
# requests
# bs4 (beautifulsoup)
# pyttsx3
# pywhatkit
# lxml

### Libraries for Windows ###
# python -m pip install pyaudio

### Libraries for Linux ###
# pip install PyAudio # if error then lower python version <= 3.6

### Additional (currently unsupported) libraries ###
# pip install SpeechRecognition
# pip install wikipedia
# pip install pyjokes

### Additional libraries ###
# import datetime
# import wikipedia
# import speech_recognition as sr
# import pyjokes

### File to read ###
filename = "business_1.txt"

def credits():
    program = "Ready Script 1"
    version = "v.0.2-2a"
    author = "vera lo"
    print("\n" + program)
    print("\n\nVersion: " + version + "\nAuthor: " + author)

with open(filename, 'r', encoding="utf-8") as f:
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