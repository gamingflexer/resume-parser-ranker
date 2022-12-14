import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import *
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from date_extractor import extract_dates
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFSyntaxError
from constants import *
from nltk import ngrams
from deep_translator import GoogleTranslator


extracted_dates = {}
person_list = []
person_names = person_list
url1 = []


def url(text5):
    try:
        url = re.search("(?P<url>https?://[^\s]+)", text5).group("url")

    except:
        url = None
    return url


def url_func(text2):
    url1.clear()

    tex = text2
    val1 = "so"
    while(val1 != ""):
        val1 = url(tex)
        if(val1 == None):
            break

        else:

            url1.append(val1)
            for i in url1:
                tex = tex.replace(i, "")

    return url1


def email(text):
    try:
        #text = pre_process1_rsw1(text)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        emails = set(emails)
    except:
        emails = "None"
    return(emails)


def get_phone_numbers(string):
    r = re.compile(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', num) for num in phone_numbers]


# dates grabber
def data_grabber(text):
    dates = extract_dates(text)
    return dates


person_list = []
person_names = person_list


def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary=False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1:  # avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []


def human_name(text):
    names = get_human_names(text)
    for person in person_list:
        person_split = person.split(" ")
        for name in person_split:
            if wordnet.synsets(name):
                if (name in person):
                    person_names.remove(person)
                    break

    person_names


def address_grabber(text):
    regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
    address = re.findall(regexp, text)
    #addresses = pyap.parse(text, country='INDIA')
    return address

# find pincode


def pincode_grabber(text):
    pincode = r"[^\d][^a-zA-Z\d](\d{6})[^a-zA-Z\d]"
    pattern = re.compile(pincode)
    result = pattern.findall(text)
    if len(result) == 0:
        return ' '
    return result[0]


def dob_grabber(text, ents):
    dob = 'Not found'
    lines = [line.strip() for line in text.split('\n')]
    dob_pattern = r'((\d)?(\d)(th)?.((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)|(january)|(february)|(march)|(april)|(may)|(june)|(july)|(august)|(september)|(october)|(november)|(december)|(\d{2})).(\d{4}))'
    required = ''
    matches = ['dob', 'date of birth', 'birth date']
    flag = 0
    count = 0
    for lin in lines:

        if any(x in lin.lower().strip() for x in matches):
            required = lin.lower() + '\n'
            flag = 1
        if flag == 1:
            if len(lin.split()) < 1:
                continue
            required += lin.lower() + '\n'
            count += 1
        if count > 4:
            break
    required = ' '.join(req for req in required.split())

    match = re.findall(dob_pattern, required)
    try:
        return match[0][0]
    except:
        return ''


def pre_process1_rsw1(text):
    # text = p0(text)
    # text = clean_text(text)
    text = "".join(text.split('\n'))  # remove whitespaces
    text = text.lower()

    # using re
    text = re.sub('http\S+\s*', ' ', text)
    text = re.sub('RT|cc', ' ', text)
    text = re.sub('#\S+', ' ', text)
    #text = re.sub('@\S+', ' ', text)

    # removes phone numbers
    text = re.sub(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', '', text)
    text = re.sub(r'[^\x00-\x7f]', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub("\n", " ", text)

    # remove uncessary stop words
    for i in range(len(words_stop)):  # removes emails
        text = text.replace(words_stop[i], "")

    return ''.join(text)


def pre_process2_rsw(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    new_text = [word for word in word_tokens if word not in stop_words]
    return new_text


# remove puncutations
def pre_process3_rpm(text):
    translator = str.maketrans(",", string.punctuation)
    return text.translate(translator)


# remove hex code
def remove_hexcode_rhc(text):
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    return text


url1.clear()

# new functions


def p0(new_text):
    req = ''
    for line in new_text.split('\n'):
        ll = re.sub(r'[^0-9a-zA-Z]+', ' ', line)
        req += ll + '\n'
        new_text = req
    return new_text


def clean_text(val):
    result = list()
    for each in val:
        out = re.sub(r'[^0-9a-zA-Z]+', ' ', each)
        result.append(out)
    return result


def clean_bert(entities1, tags_vals):
    main = []
    for i in entities1:
        if i['entity'] in tags_vals:
            k = {i['entity']: i['text']}
            main = main + [k]

    #save & clean
    k = len(main)

    # clean unnescaary values
    r = []
    for k in range(len(main)):
        for key, value in main[k].items():
            if value == '':
                r = r + [k]
                # main.remove(main[k])
            elif value == ':':
                r = r + [k]
            elif value == ',':
                r = r + [k]
            elif value == 'Resume':
                r = r + [k]
            elif value == '.':
                r = r + [k]
            elif value == ' ':
                r = r + [k]
            elif value == '.':
                r = r + [k]
            elif value == '.':
                r = r + [k]

    for rr in range(len(r)):
        main.remove(main[rr])
    r.clear()

    # clean unnesacry keys
    for val in main:
        for key, value in val.items():
            if key == "Email Address":
                main.remove(val)
            elif key == "UNKNOWN":
                main.remove(val)
            elif key == "Empty":
                main.remove(val)

    return main


def get_number_of_pages(file_name):
    try:
        if isinstance(file_name, io.BytesIO):
            # for remote pdf file
            count = 0
            for page in PDFPage.get_pages(
                file_name,
                caching=True,
                check_extractable=True
            ):
                count += 1
            return count
        else:
            # for local pdf file
            if file_name.endswith('.pdf'):
                count = 0
                with open(file_name, 'rb') as fh:
                    for page in PDFPage.get_pages(
                        fh,
                        caching=True,
                        check_extractable=True
                    ):
                        count += 1
                return count
            else:
                return None
    except PDFSyntaxError:
        return None


def get_links(links):
    extras = ""
    git_link = ""
    lid_link = ""
    li = list(links.split(" "))

    for i in li:
        if 'linkedin' in i:
            lid_link = lid_link + i + ","
        elif 'github' in i:
            git_link = git_link + i + ","
        else:
            extras = extras + i + ","

    l1 = lid_link.split(",")
    l2 = git_link.split(",")
    l3 = extras.split(",")
    linkdedln = ""
    github = ""
    others = ""
    for i in l1:
        if (i == ""):
            pass
        else:
            linkdedln = linkdedln+i+","

    for i in l2:
        if (i == ""):
            pass
        else:
            github = github+i+","

    for i in l3:
        if (i == ""):
            pass
        else:
            others = others+i+","
    print(linkdedln)
    print(github)
    print(others)
    return (linkdedln, github, others)


# extras
def extract_entity_sections_grad(text):
    '''
    Helper function to extract all the raw text from sections of resume
    specifically for graduates and undergraduates

    :param text: Raw text of resume
    :return: dictionary of entities
    '''
    text_split = [i.strip() for i in text.split('\n')]
    # sections_in_resume = [i for i in text_split if i.lower() in sections]
    entities = {}
    key = False
    for phrase in text_split:
        if len(phrase) == 1:
            p_key = phrase
        else:
            p_key = set(phrase.lower().split()) & set(cs.RESUME_SECTIONS_GRAD)
        try:
            p_key = list(p_key)[0]
        except IndexError:
            pass
        if p_key in cs.RESUME_SECTIONS_GRAD:
            entities[p_key] = []
            key = p_key
        elif key and phrase.strip():
            entities[key].append(phrase)
    return entities


def summary_clean(text):

    def remwithre(text):
        there = re.compile(re.escape('.')+'.*')
        return there.sub('', text)

    l = []
    m = text.split(" ")
    for i in m:
        if "github" in i:
            print("found")
            k = i
        else:
            k = remwithre(i)
        l.append(k)

    new_text = ' '.join(l)
    return new_text


linkdien_keys = ['Highlights', 'About', 'Activity', 'Education', 'Experience', 'Licenses & certifications', 'Skills',
                 'Projects', 'Honors & awards', 'Languages', 'Interests', 'Causes', 'Featured']


def linkdien_clean(dict):
    for i in linkdien_keys:  # str
        try:
            k = dict[i]
            k = re.sub("\n", " ", k)
            k = re.sub("/n", " ", k)
            k = summary_clean(k)
            dict[i] = k
        except:
            pass
    for i in linkdien_keys:  # list
        try:
            k = dict[i]
            t = 0
            for m in k:
                m = re.sub("\n", " ", m)
                m = re.sub("/n", " ", m)
                m = summary_clean(m)
                dict[i][t] = m
                t = t+1
        except:
            pass
    return dict


def dict_clean(dict):
    final_keys_1 = ['Current Job', 'Total Experience(years)', 'Awards']  # str
    final_keys_2 = ['Personal Details', 'Experience', 'Education']  # dict
    final_keys_0 = ["Skills", 'Reference', 'university',
                    'degree', 'Companies worked at', 'degree']  # list

    personal_keys = ['Name', 'Phone Number', 'Email Id',
                     'Gender', 'Date of birth', 'Location', 'Pincode']
    exp_keys = ['Designation', 'Company', 'Experience Year', 'Projects']
    edu_keys = ['Degree', 'College', 'Graduation Year',
                'Trainings/Courses', 'Publications']

    # clean function
    for i in final_keys_1:  # str
        k = dict[i]
        k = strip_emoji(k)
        k = re.sub("\n", " ", k)
        k = re.sub("/n", " ", k)
        k = k.replace("Address:-Email:Address:-", "")
        dict[i] = k

    for i in final_keys_0:  # list
        k = dict[i]
        t = 0
        for m in k:
            try:
                m = strip_emoji(m)
                m = re.sub("\n", " ", m)
                m = re.sub("/n", " ", m)
                dict[i][t] = m
                t = t+1
            except:
                pass

    for i in final_keys_2:  # dict
        k = dict[i]
        if i == 'Personal Details':
            for m in personal_keys:
                temp = k[m]
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n", " ", temp)
                    temp = re.sub("/n", " ", temp)
                except:
                    pass
                dict['Personal Details'][m] = temp

        if i == 'Experience':
            for m in exp_keys:
                temp = k[m]
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n", " ", temp)
                    temp = re.sub("/n", " ", temp)
                except:
                    pass
                dict['Experience'][m] = temp

        if i == 'Education':
            for m in edu_keys:
                temp = k[m]
                # print(temp)
                try:
                    temp = strip_emoji(temp)
                    temp = re.sub("\n", " ", temp)
                    temp = re.sub("/n", " ", temp)
                except:
                    pass
                dict['Education'][m] = temp
    return dict

# github links


def find_gitlink(github_links):
    for i in github_links:
        m = i.split("/")
        try:
            m.pop(4)
        except:
            return i

# remove emoji


def strip_emoji(string):
    try:
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', string)
    except Exception as e:
        #print("Error for emoji - ", e)
        return string

def g_translation_function_en(inText):
    try:
        if len(inText) <= 4999:
            outText = GoogleTranslator(
                source='auto', target='en').translate(inText)
            return outText
        else:
            return inText
    except Exception as e:
        #print(e)
        return inText