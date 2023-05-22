### Instruction

1. Create a virtual environment
   `virtualenv vocab`

2. activate virtual environment
   `source vocab/bin/activate`

3. Install dependencies
   `pip install -r requirements.txt`

4. Install popular corpus from fastapi (Wasn't required for me)
   `python -m nltk.downloader popular`

5. Run fast api server
   `uvicorn app.main:app --reload`

Access the api docs along with execution option at
http://localhost:8000/docs

### NLTK Notebook

This project also accompanies a jupyter notebook with useful nltk concepts.

Run it with the command `jupyter-lab`

[nltk basic parsing and pos tagging](nltk_basics_parsing.ipynb)

Deploying in aws Labmda

1. pip install mangum
2. Copy entire content of lib/ to a zip file on the root directory.
3. Copy the entire app/ directory inside the same zip file.
4. Upload this to aws lambda.
