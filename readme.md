### Instruction
1. Create a virtual environment
 `virtualenv vocab`

2. activate virtual environment
 `source vocab/bin/activate`

3. Install dependencies
 `pip install -r requirements.txt`

4. Install popular corpus from fastapi
 `python -m nltk.downloader popular`

5. Run fast api server
 `uvicorn app.main:app --reload`


Access the api docs along with execution option at 
 http://localhost:8000/docs


### NLTK Notebook
This project also accompanies a jupyter notebook with useful nltk concepts.

Run it with the command `jupyter-lab`