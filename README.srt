# Resume Parser & Ranker

```
Resume Parser | Resume Ranker | Resume Summariser
```
- [Collab Notebook](https://colab.research.google.com/drive/1-fUeFKWoPP1P34qER1hJFg0tbNBq58AR?usp=sharing)

# Features

- Extract name
- Extract email
- Extract mobile numbers
- Extract skills
- Extract total experience
- Extract college name
- Extract degree
- Extract designation
- Extract company names

And many more ....

# Installation (users)

- You can install this package using

  - `pip install sourceparser`

- Start Docker Container for runnig the Tika Server
  
  - `docker run --rm -p 9998:9998 logicalspark/docker-tikaserver`


# Installation (dev)

- You can install this package using

```
git clone https://github.com/gamingflexer/resume-parser-ranker.git
cd resume-parser-ranker
pip install -e .
```

- For NLP operations we use spacy and nltk. Install them using below commands:

```bash
# spaCy
python -m spacy download en_core_web_sm

# nltk
python -m nltk.downloader words
python -m nltk.downloader stopwords
```

# Documentation

Official documentation is available at: 

# Supported File Formats

- All files Formats are supported on all Operating Systems (Windows, Linux, Mac OS X, etc.) if any unsupported file format is found, please raise an issue.
- If you want to extract DOC files you can install [textract](https://textract.readthedocs.io/en/stable/installation.html) for your OS (Linux, MacOS)

# Usage

- Import it in your Python project

```python

from sourceparser import SourceParser
parser_obj_file = SourceParser("path/to/file")
print(parser_obj_file)

```

# CLI

For running the resume extractor you can also use the `cli` provided

```bash
usage: sourceparser [-h] [-f FILENAME] [-fn FOLDERNAME] [-l] [-sm] [-mb]
                    [-gpu] [-json]

SourceParser

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        File name to parse
  -fn FOLDERNAME, --foldername FOLDERNAME
                        Folder name to parse files in the folder
  -l, --learner         Uploads the file to the server for learning
  -sm, --summariser     Summarises the file
  -mb, --multiBatch     Multi Batch Summariser
  -gpu, --gpuPresent    Add if GPU Present
```

# Result

The module would return a list of dictionary objects with result as follows:

```

```

# Donation

For running the Self Learner we need funds. If you like this project and want to support us, you can donate us using the below link:

- [Donate](gamingflexer)