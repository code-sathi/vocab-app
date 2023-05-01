from fastapi import APIRouter
import nltk
from nltk.corpus import wordnet

router = APIRouter()



@router.get("/")
async def root():
    return {"message": "Hello World, I am fastapi"}



@router.get("/substitute")
async def check(sentence: str, words: str):
    return substitute(sentence, words.split(','))

@router.get("/synonyms")
async def check(word: str):
    return check_synonyms(word.split(',')[0])
     

def check_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemma_names():
            synonyms.add(lemma)
    return synonyms


def substitute(sentence,words):
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
