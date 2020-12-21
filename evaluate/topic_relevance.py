from gensim import corpora
from nltk.corpus import wordnet as wn
import pandas as pd
import gensim
import spacy
import nltk
import sys


def processText(text):
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    return " ".join(result)

# Getting Arguments
input_text = []
f = sys.argv[1]
keyword = sys.argv[2]
file = open("output.txt", "r")
for x in file:
  if keyword in x:
    input_text.append(x)

# # Sports
# input_text = [
# "What is the minimum number of people required to play tennis?",
# "Are female tennis players required to wear only white clothes?",
# "How can I be a ball boy?",
# "How many people are required for a football match?",
# "How big is a soccer ball?",
# "How many hours of practice are required to be a successful figure skater?",
# "How do I run?",
# "What if I fall down when running?",
# "Is it okay to drink water during a marathon?",
# "Can I wear a high heel when playing soccer?",
# "What do I do if a cat comes in during a soccer game?",
# "What is the difference between soccer and football?",
# "Is it painful if I get hit by a tennis ball?",
# "Can I paint my tennis ball red?",
# "Can I paint my soccer ball blue?"
# ]



# # Shopping
# input_text2 = [
# "How much are these shoes?",
# "Can I buy a human?",
# "Can I buy a boyfriend?",
# "Can you give me money so that I can buy a new iphone?",
# "Can I buy you?",
# "How much is a brand-new IPad?",
# "Can I buy a house?",
# "What is the mean delivery fee in Amazon?",
# "How much is ChicChoc?",
# "How much is a desktop?",
# "How can I go shopping?",
# "Where is the nearest shopping mall?",
# "How much is americano?",
# "How can I purchase the watch?",
# "What store sells gaming keyboard?"
# ]



# # Music
# input_text3 = [
# "What music do you prefer?",
# "Do you know Rachmaninoff piano concerto no.2?",
# "Do you like classical music?",
# "How many times did you listen to Gangnam Style?",
# "What is the pitch of this song?",
# "What is your favorite music?",
# "Can I listen to music on YouTube?",
# "What’s your KakaoTalk profile music?",
# "Do you often listen to music?",
# "Are you part of any musical groups?",
# "What genre of music do you prefer?",
# "Do you like Brahms?",
# "Do you like Vitas?",
# "Have you listened to Eminem?",
# "What is your favorite idol music?"
# ]



sentences = []

for sentence in input_text:
    sentences.append(processText(sentence))

for i in range(len(sentences)):
    sentences[i] = sentences[i].split()

dictionary = corpora.Dictionary(sentences)
corpus = [dictionary.doc2bow(text) for text in sentences]

NUM_TOPICS = 3 # number of topics
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word = dictionary, passes = 15)
topics = ldamodel.print_topics()
topic_percentages = ldamodel.get_topics()
print(topics)
# Get the words from ldamodel
words_lst = []
x = ldamodel.show_topics(num_topics = NUM_TOPICS, num_words = 5, formatted = False)
topics_words = [(tp[0], [wd[0] for wd in tp[1]]) for tp in x]

# Below Code Prints Only Words 
# for topic,words in topics_words:
#     lst = []
#     word = " ".join(words)
#     for x in range(len(words)):
#         if wn.synsets(words[x])[0].pos() == 'n':
#             lst.append(words[x])
#     words_lst.append(lst)

# Topic Words
print(topics_words)

# Topic terms
topic_terms = []
for j in range(len(words_lst)):
    tmp = wn.synsets(words_lst[j][0])[0].pos()

    topic_term = wn.synset(words_lst[j][0] + '.' + tmp + '.01').hypernyms()
    for synset in topic_term:
        topic_terms.append(synset.lemmas()[0].name())
   
for i, topic_list in enumerate(ldamodel[corpus]):
    print(i + 1,"th sentence" + "'" + "s topic percentages are: ", topic_list)

for j in range(len(topic_terms)):
    print("topic " + str(j + 1) + ": " + topic_terms[j])
