import warnings
warnings.filterwarnings("ignore")    
                 
import re
import numpy as np                                  
from nltk.corpus import stopwords                   
from nltk.tokenize import word_tokenize

'''job description is taken as input and cosine similarity is calculated with the resume cleaned and job description cleaned data.'''

def cosine_sim(vec1, vec2):
    '''Return Cosine Similarity.'''
    return  np.dot(vec1,vec2)/(np.linalg.norm(vec1)* np.linalg.norm(vec2))

def ranking(jd_text,data):
    X_list = word_tokenize(data) 
    Y_list = word_tokenize(jd_text)
    
    # sw contains the list of stopwords
    sw = stopwords.words('english') 
    l1 =[];l2 =[]
    
    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw} 
    Y_set = {w for w in Y_list if not w in sw}
    
    # form a set containing keywords of both strings 
    rvector = X_set.union(Y_set) 
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    rank = cosine*100
    return rank

# more to add in the future
def clean_job_description(jd_text):
    '''Clean the job description text.'''
    jd_text = jd_text.lower()
    jd_text = re.sub(r'[^\w\s]','',jd_text)
    return jd_text