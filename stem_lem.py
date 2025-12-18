import nltk
import spacy

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "runner", "ran", "easily", "fairly", "cats", "cacti", "geese", "rocks", "pythoning"]    
for word in words:
    print(word, "|", stemmer.stem(word))

print("----"*30)

## Lemmatization using spacy
nlp = spacy.load("en_core_web_sm")  

doc = nlp("running runner ran easily fairly cats cacti geese rocks pythoning better best")  
for token in doc:
    print(token.text, "|", token.lemma_, "|", token.lemma)    

print(f"----"*30)
doc2 = nlp("Mando talked for 3 hrs although talking is not his cup of tea he became talkative")
for token in doc2:
    print(token.text, "|", token.lemma_)

print(f"----"*30)

print(nlp.pipe_names)

ar = nlp.get_pipe("attribute_ruler")
ar.add([[{"TEXT":"Bro"}], [{"TEXT":"Brah"}]],{"LEMMA":"Brother"})
doc3 = nlp("Bro, you wanna go? Brah, don't say no! I am exhausted")
for token in doc3:
    print(token.text, "|", token.lemma_)