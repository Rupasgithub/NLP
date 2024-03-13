# Task 19 - NLP - garden path sentences

# import spacy and load the english language model
import spacy
nlp = spacy.load('en_core_web_md')

# create list with garden-path sentences
gardenpathSentences = ["The old man the boat.", "The complex houses married and single soldiers and their families."]

# extend the list with the sentences given in Practical Task 1
gardenpathSentences_extend = ["Mary gave the child a Band-Aid.", "That Jill is here never hurts.", "The cotton clothing is made of grows in Mississippi."]
gardenpathSentences.extend(gardenpathSentences_extend)

# loop through each sentence in the list to tokenize and perform Named Entity 
# Recognition
for sentence_index in range(len(gardenpathSentences)):
    garden_doc = nlp(gardenpathSentences[sentence_index])
    print([(token.orth_) for token in garden_doc])
    print([(i, i.label_, i.label) for i in garden_doc.ents])
    print()

entity_org = spacy.explain("ORG")
print("SpaCy categorized ORG as " + entity_org)
print()
# Looked up 'ORG', which was explained by spaCy as 'Companies, agencies, 
# institutions etc'. 
# SpaCy categorized 'Band-Aid' as a company, which is accurate. Band-Aid 
# is a brand of adhesive bandages distributed by a consumer health company.

entity_gpe = spacy.explain("GPE")
print("SpaCy categorized GPE as " + entity_gpe)
print()
# Looked up 'GPE', which was explained by spaCy as 'Countries, cities, states'
# SpaCy categorized 'Mississippi' as GPE, which is accurate because
# Mississippi is a state in the USA.









