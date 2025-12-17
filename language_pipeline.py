import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("fr_core_news_sm")

print(nlp.pipe_names)

print(f"----"*30)


doc = nlp("Betty bought some butter, but the butter was bitter, so she bought some better butter to make the bitter butter better")
for token in doc:
    print(token.text, "|", token.pos_, "|", token.lemma_)

print(f"----"*30)


doc2 = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc2.ents:
    print(ent.text, "|", ent.label_,"|", spacy.explain(ent.label_))

print(f"----"*30)


##Converting the same sentennce into French

doc3 = nlp("Apple envisage de racheter une start-up britannique pour 1 milliard de dollars.")
for ent in doc3.ents:
    print(f"In French:", ent.text, "|", ent.label_, "|", spacy.explain(ent.label_)) 


print(f"----"*30)
##Adding Custom Component to the Pipeline

source_nlp = spacy.load("en_core_web_sm")

nlp = spacy.blank("en")
nlp.add_pipe("ner", source =source_nlp)
print(nlp.pipe_names)


doc3 = nlp("Google was founded by Larry Page and Sergey Brin in California.")
for ent in doc3.ents:
    print(ent.text, "|", ent.label_,"|", spacy.explain(ent.label_))

print(f"----"*30)