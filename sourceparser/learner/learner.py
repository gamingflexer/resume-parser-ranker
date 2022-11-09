import os
import json
from config import data_path,resume_path,json_path
from learner.views import *

# make data directory to store the resumes
if os.path.exists(data_path) == False:
    os.mkdir(data_path)
    os.mkdir(resume_path)
    os.mkdir(json_path)
    
def save_json(data, filename):
    with open(os.path.join(json_path, filename), 'w') as f:
        json.dump(data, f)