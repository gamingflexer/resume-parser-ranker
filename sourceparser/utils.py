import uuid
import random
import pyfiglet
from preprocessing import url_func, email, get_phone_numbers, data_grabber, get_human_names, address_grabber, pincode_grabber, pre_process1_rsw1, remove_hexcode_rhc

def extract_data(text):
    scraplink = ""
    eid = ""
    phno = ""
    f_human_name = ""
    fdate = ""
    address = ""

    link = url_func(text)
    if (len(link) == 0):
        scraplink = "null"
    else:
        scraplink = ""
        for i in link:
            scraplink = scraplink + "  " + i

    mailid = email(text)
    mailid=set(mailid)
    for i in mailid:
        eid = i + "  " + eid
    if (eid is None):
        eid = "null"

    phone_number = get_phone_numbers(text)
    if (len(phone_number) == 0):
        phno = "null"
    else:
        for i in phone_number:
            phno = i + "  " + phno

    e_date = data_grabber(text)
    if (len(e_date) == 0):
        fdate = "null"
    else:
        for k in e_date:
            fdate = fdate + "  " + str(k)

    human_name = get_human_names(text)
    if (human_name is None):
        f_human_name = "null"
    else:
        for i in human_name:
            f_human_name = f_human_name + " " + i

    add = address_grabber(text)
    if (len(add) == 0):
        address = "null"
    else:
        for ad in add:
            address = address + "  " + ad
    
    pincode = pincode_grabber(text)
    text1 = pre_process1_rsw1(text)
    ftext = remove_hexcode_rhc(text1)
    return (text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext)

def uuid_generator():
    return str(uuid.uuid4())

def captcha_verifer():
    check_number = random.randint(0, 999)
    check_string = f"{check_number:>04}"
    print(pyfiglet.Figlet().renderText(check_string))
    response = input("Please enter the number shown above to proceed: ")
    if response != check_string:
        exit(-1)
    print("Passed verification check!")