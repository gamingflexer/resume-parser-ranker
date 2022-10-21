import os

index = "/"

#whole
basepath = os.path.dirname(os.path.realpath(__file__))
models = os.path.join(basepath, 'models')
summarizer = os.path.join(basepath, 'summarizer')

summary_model = os.path.join(basepath,"models","outputs-100-out-lenght")
summary_db = os.path.join(basepath,"models","Summary-db.csv")
summary_extractive = os.path.join(basepath,"models","Extractive_BART")

#relative
skill_csv  = 'models/skills.csv'
nations = 'models/nationality.csv'
state = 'models/state.csv'
country ='models/country.csv'
city = "models/cities_samples.txt"

#temp data

outputDirectory = os.path.join(basepath,"temp")