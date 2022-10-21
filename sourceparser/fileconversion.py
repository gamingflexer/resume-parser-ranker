import cv2
from fpdf import FPDF
import pdfkit
import textract
import pytesseract
from tika import parser
from utils import extract_data
from autocorrect import Speller
from preprocessing import *
from config import outputDirectory
spell = Speller(only_replacements=True)


def fileconversionToEntites(filename, y):
    eid = ""
    phno = ""
    f_human_name = ""
    fdate = ""
    address = ""
    scraplink = ""
    # count=1
    f_human_name = ""
    pincode = ""
    ftext = ""
    x = filename.rfind(".")
    extension = filename[x + 1:]
    if (extension == "docx"):
        try: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = text.replace("\n", " ")
            text = text.replace("\t", " ")
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)

        except:
            try: #using textract
                text = textract.process(filename)
                text = text.replace("\n", " ")
                text = text.replace("\t", " ")
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                try: #using textract
                    text = textract.process(filename)
                    text = text.decode('utf-8')
                    text = text.replace("\n", " ")
                    text = text.replace("\t", " ")
                    text = spell(text)
                    text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                        text)
                except:
                    text = "Text Not Extracted"
                    text1 = "NAN"
                    scraplink = "NAN"
                    eid = "NAN"
                    phno = "NAN"
                    fdate = "NAN"
                    f_human_name = "NAN"
                    address = "NAN"
                    pincode = "NAN"
                    ftext = "NAN"

        text = text.replace("\n", " ")
        text = text.replace("\t", " ")

        return (text, scraplink, eid, ftext)

    elif (extension == "png" or extension == "jpg" or extension == "jpeg"):
        try: #using tesseract
            file = open(filename, "w")
            pdf = FPDF()
            pdf.add_page()
            fpdf = FPDF('L', 'cm', (500, 550))
            pdf.set_font("Arial", size=12)
            #pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            img = cv2.imread(filename)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            file.write(pytesseract.image_to_string(img))
            file.close()
            f = open(filename, 'r')
            if not os.path.exists(outputDirectory):
                os.mkdir(outputDirectory)
            name1 = outputDirectory
            for x in f:
                x = x.replace("\n", " ")
                x = x.replace("\t", " ")
                pdf.cell(200, 10, txt=x, ln=1, align='L')

            pdf.output(name1)
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try: #using textract
                text = textract.process(filename)
                text = text.decode('utf-8')
                text = text.replace("\n", " ")
                text = text.replace("\t", " ")
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                try: #using textract
                    text = textract.process(filename)
                    text = text.decode('utf-8')
                    text = text.replace("\n", " ")
                    text = text.replace("\t", " ")
                    text = spell(text)
                    text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                        text)
                except:
                    text = "Text Not Extracted"
                    text1 = "NAN"
                    scraplink = "NAN"
                    eid = "NAN"
                    phno = "NAN"
                    fdate = "NAN"
                    f_human_name = "NAN"
                    address = "NAN"
                    pincode = "NAN"
                    ftext = "NAN"

        return (text, scraplink, eid, ftext)

    elif (extension == "txt"):
        try:
            pdf = FPDF()
            pdf.add_page()
            fpdf = FPDF('L', 'cm', (500, 550))
            pdf.set_font("Arial", size=11)
            f = open(filename, 'r')
            for x in f:
                pdf.cell(200, 10, txt=x, ln=1, align='L')

            pdf.output(filename)
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try:
                text = textract.process(filename)
                text = text.replace("\n", " ")
                text = text.replace("\t", " ")
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                try:
                    text = textract.process(filename)
                    text = text.decode('utf-8')
                    text = text.replace("\n", " ")
                    text = text.replace("\t", " ")
                    text = spell(text)
                    text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                        text)
                except:
                    text = "Text Not Extracted"
                    text1 = "NAN"
                    scraplink = "NAN"
                    eid = "NAN"
                    phno = "NAN"
                    fdate = "NAN"
                    f_human_name = "NAN"
                    address = "NAN"
                    pincode = "NAN"
                    ftext = "NAN"
        return (text, scraplink, eid, ftext)

    elif (extension == "html"):
        try:
            converted = "resume" + y + ".pdf"
            name = os.join(outputDirectory, converted)
            with open(filename) as f:
                pdfkit.from_file(f, filename)
            raw = parser.from_file(name)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try: #using textract
                text = textract.process(filename)
                text = text.replace("\n", " ")
                text = text.replace("\t", " ")
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                try: #using textract
                    text = textract.process(filename)
                    text = text.decode('utf-8')
                    text = text.replace("\n", " ")
                    text = text.replace("\t", " ")
                    text = spell(text)
                    text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                        text)
                except:
                    text = "Text Not Extracted"
                    text1 = "NAN"
                    scraplink = "NAN"
                    eid = "NAN"
                    phno = "NAN"
                    fdate = "NAN"
                    f_human_name = "NAN"
                    address = "NAN"
                    pincode = "NAN"
                    ftext = "NAN"

        return (text, scraplink, eid, ftext)

    elif (extension == "rtf"):
        try: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try: #using tika
                raw = parser.from_file(filename)
                text = raw['content']
                text = text.decode('utf-8')
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                text = "Text Not Extracted"
                text1 = "NAN"
                scraplink = "NAN"
                eid = "NAN"
                phno = "NAN"
                fdate = "NAN"
                f_human_name = "NAN"
                address = "NAN"
                pincode = "NAN"
                ftext = "NAN"

        return (text, scraplink, eid, ftext)

    elif (extension == "odt"):
        try: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try: #using tika
                raw = parser.from_file(filename)
                text = raw['content']
                text = text.decode('utf-8')
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                text = "Text Not Extracted"
                text1 = "NAN"
                scraplink = "NAN"
                eid = "NAN"
                phno = "NAN"
                fdate = "NAN"
                f_human_name = "NAN"
                address = "NAN"
                pincode = "NAN"
                ftext = "NAN"

        return (text, scraplink, eid, ftext)

    elif (extension == "doc"):
        try: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)
        except:
            try: #using tika
                raw = parser.from_file(filename)
                text = raw['content']
                text = text.decode('utf-8')
                text = spell(text)
                text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                    text)
            except:
                text = "Text Not Extracted"
                text1 = "NAN"
                scraplink = "NAN"
                eid = "NAN"
                phno = "NAN"
                fdate = "NAN"
                f_human_name = "NAN"
                address = "NAN"
                pincode = "NAN"
                ftext = "NAN"

        return (text, scraplink, eid, ftext)
    elif(extension == "pdf"):
        try: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)

        except: #using tika
            raw = parser.from_file(filename)
            text = raw['content']
            text = spell(text)
            text, text1, scraplink, eid, phno, fdate, f_human_name, address, pincode, ftext = extract_data(
                text)

    return text, scraplink, eid, ftext
