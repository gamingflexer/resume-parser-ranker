import os
from config import models_path

basepath = os.path.dirname(os.path.realpath(__file__))

skill_csv  = os.path.join(models_path,'txt_utils', 'skill.csv')
nations = os.path.join(models_path,'txt_utils', 'nationality.csv')
state = os.path.join(models_path,'txt_utils', 'state.csv')
country = os.path.join(models_path,'txt_utils', 'country.csv')
city = os.path.join(models_path,'txt_utils', 'cities_samples.txt')

skills_rb = os.path.join(models_path,'txt_utils', 'skills')
skill_model_dir = os.path.join(models_path,'skills')
resume_model = os.path.join(models_path,'main_model')
education_model = os.path.join(models_path,'education') 
experience_model = os.path.join(models_path,'experience')
