# Resume Parser & Ranker

```
A simple resume parser used for extracting information from resumes
```
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

# Installation (users)

- You can install this package using

```Coming Soon```

# Installation (dev)

- You can install this package using

```
git clone https://github.com/gamingflexer/resume-parser-ranker.git
cd resume-parser-ranker
pip install .
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

Official documentation is available at: Coming Soon

# Supported File Formats

- PDF and DOCx files are supported on all Operating Systems
- If you want to extract DOC files you can install [textract](https://textract.readthedocs.io/en/stable/installation.html) for your OS (Linux, MacOS)
- Note: You just have to install textract (and nothing else) and doc files will get parsed easily

# Usage

- Import it in your Python project

```python

```

# CLI

For running the resume extractor you can also use the `cli` provided

```bash
usage: sourceparser [-h] [-f FILE] [-d DIRECTORY] [-r REMOTEFILE]
                   [-re CUSTOM_REGEX] [-sf SKILLSFILE] [-e EXPORT_FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  resume file to be extracted
  -d DIRECTORY, --directory DIRECTORY
                        directory containing all the resumes to be extracted
  -sf SKILLSFILE, --skillsfile SKILLSFILE
                        custom skills CSV file against which skills are
                        searched for
  -e EXPORT_FORMAT, --export-format EXPORT_FORMAT
                        the information export format (json)
```

# Result

The module would return a list of dictionary objects with result as follows:

```

```

# Donation

Coming soon 😂
              'Python',
