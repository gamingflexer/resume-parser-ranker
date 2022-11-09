from setuptools import setup
import spacy.cli
spacy.cli.download("en_core_web_sm")

setup(
    name='sourceparser',
    version='0.1.1',
    description='A simple resume parser used for extracting information from resumes',
    url='https://github.com/gamingflexer/resume-parser-ranker',
    author='gamingflexer',
    author_email='',
    license='MIT',
    packages=['sourceparser'],
    install_requires=['spacy==2.1.4', "autocorrect==2.6.1",
                      "date_extractor==5.1.5",
                      "fpdf==1.7.2",
                      "nltk==3.7",
                      "opencv_python==4.6.0.66",
                      "pdfkit==1.0.0",
                      "pdfminer==20191125",
                      "pdfminer.six==20220524",
                      "pytesseract==0.3.10",
                      "setuptools==65.4.0",
                      "python-dateutil==2.8.2",
                      "phonenumbers==8.12.34",
                      "pdfplumber==0.7.5",
                       "textract==1.5.0",
                      "stemming==1.0.1",
                      "tika==1.24",
                      "docx2txt==0.8",
                      "pandas==1.3.5",
                      "spacy_langdetect==0.1.2",
                      "transformers==4.24.0",
                      "torch",
                      "deep_translator==1.9.1",
                      "pyfiglet==0.8.post1",
                      "pymongo==3.10.1"
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
