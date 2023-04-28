import nltk
from nltk.corpus import wordnet
from fastapi import FastAPI




app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, I am fastapi"}



@app.get("/substitute")
async def check(sentence: str):
    return check_synonyms(sentence)
     


def check_synonyms(sentence):
    words = ['ubiquitous', 'melancholy', 'conundrum', 'quintessential', 'euphoria', 'clandestine', 
         'tumultuous', 'surreptitious', 'unorthodox', 'salient', 'serendipity', 'formidable', 
         'enigmatic', 'plethora', 'sagacious', 'ephemeral', 'insidious', 'facetious', 'myopic', 
         'indelible','inscrutable']

    tokens = nltk.word_tokenize(sentence)
    for i in range(len(tokens)):
            synonyms = set()
            for syn in wordnet.synsets(tokens[i]):
                for lemma in syn.lemma_names():
                    synonyms.add(lemma)

            for each in synonyms:
                if each in words:
                    tokens[i] = each
                    break

    return  " ".join(tokens)
