from fastapi import APIRouter
from app.services.word_substitute import get_synonym_for_word_in_sentence
from app.services.substitute import substitute
router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World, I am fastapi"}


@router.get("/substitute")
async def check(sentence: str, words: str):
    return substitute(sentence, words.split(','))

# Example sentence: I condemn this, index: 1
@router.get("/synonyms")
async def check(sentence: str, index: int):
    return get_synonym_for_word_in_sentence(sentence, index)
