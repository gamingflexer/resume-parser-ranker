import os
from parser2 import model_extraction
import json
import shutil
from parser2 import config
from parser2 import utils
from fileconversion import fileconversionToEntites
from parser2.resume_extraction import *
import spacy

en_sm = spacy.load('en_core_web_sm')

class Extract:
    def __init__(self, _file):
        text = fileconversionToEntites(_file, y=0)
        #text= text.decode()
        self.data = str(text)
        #raw = parser.from_file(_file)
        #self.data =  raw['content']
        self.new_data = utils.get_new_data(self.data)
        self.filename = _file.split('/')[-1]
        print(f"Starting model loading - Text extracted - {self.filename}\n")
        print("----------------------\n")

        self.custom_entities = utils.get_custom_entities(self.data)

        self.lang = get_lang(self.data)
        self.personal_info = get_personal(
            self.custom_entities, self.data)

        self.toe = get_total_years(self.data)

        self.experience, self.cjp = model_extraction.get_experience(
            self.new_data)

        self.education = model_extraction.get_education(self.new_data)
        self.awards = get_extra(self.data, 'awards')
        self.skills = get_skills(
            self.custom_entities, self.data)

        self.reference = get_reference(self.data)

        self.details = {"FileName": self.filename,
                        "Personal Details": self.personal_info,
                        "Current Job": self.cjp,
                        "Total Experience(years)": self.toe,
                        "Experience": self.experience,
                        "Education": self.education,
                        "Skills": self.skills,
                        "Reference": self.reference,
                        "Awards": self.awards
                        # "Other Information extracted:":self.others
                        }
        print(json.dumps(self.details) + "\n")

    def get_details(self):
        return (self.details)


def get_extracted(_file):
    parser = Extract(_file)
    return parser.get_details()


def get_parsed(file_name):
    dir_path = config.basepath
    file_path = os.path.join(dir_path, file_name)
    results = get_extracted(file_path)
    return results


def delete():
    dirpath = os.path.join(config.basepath, config.filedir)
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)


if __name__ == '__main__':

    file_path = os.path.join(config.basepath, config.filedir)
    results = [get_extracted(os.path.join(file_path, _file))
               for _file in os.listdir(file_path)]
