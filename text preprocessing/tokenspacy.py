import spacy
from spacy.symbols import ORTH

#Creating language object
nlp = spacy.blank("en")

doc = nlp("Betty bought some butter, but the butter was bitter, so she bought some better butter to make the bitter butter better")
doc1 = nlp('''"Let's go to N.Y.!"''')
doc2 = nlp("Jane Doe give 2 $ to Smith")

for token in doc1:
    print(token)

token1 = doc2[4]
print(token1)
print(token1.like_num)

for token in doc2:
    print(token, "==>", "index:",token.i,"is_aplha:",token.is_alpha, "is_punct:", token.is_punct, "like_num:", token.like_num, "is_currency:", token.is_currency)

with open("students.txt") as f:
    text = f.readlines()

print(text)

'''Since spacy takes text, will convert array into text'''

text = ' '.join(text)
print(text)

doctxt = nlp(text)
emails = []
for token in doctxt:
    if token.like_email:
        emails.append(token.text)
print(emails)

nlp = spacy.blank("hi")
doc = nlp("ञने गिवे 100 डोल्लर तो ष्मिथ्")
for token in doc:
    print(token)


nextstat = nlp("gimme white sauce pasta")

tokens = [token.text for token in nextstat]
print(tokens)

nlp.tokenizer.add_special_case("gimme",[
    {ORTH: "gim"},
    {ORTH: "me"}
])

nextstat = nlp("gimme white sauce pasta")

tokens = [token.text for token in nextstat]
print(tokens)

print(nlp.pipe_names)
nlp.add_pipe("sentencizer")

doc = nlp("Dr. Jane is Dentist. He is planning to open Clinic")

for sentence in doc.sents:
    print(sentence)
