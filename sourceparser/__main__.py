import argparse
import pyfiglet
import os
from utils import captcha_verifer

word = pyfiglet.figlet_format("SourceParser")
parser = argparse.ArgumentParser(description="SourceParser")

parser.add_help = True
parser.add_argument("-f","--filename", type=str)
parser.add_argument("-fn","--foldername", type=str)
parser.add_argument("-l","--learner", action='store_true')

args = parser.parse_args()
print(word)

if args.filename:
    print("\nFilename Should not contain any Whilespaces\n")
    from sourceparser import SourceParser
    parser_obj_file = SourceParser(str(args.filename))
    print(parser_obj_file.parser())
elif args.foldername:
    from sourceparser import SourceParser
    os_dir = os.listdir(args.foldername)
    for file in os_dir:
        if file.endswith(tuple(['.pdf', '.docx', '.doc','.txt','.rtf','.html','.htm','.odt'])):
            file_path = os.path.join(args.foldername,file)
            parser_obj_folder = SourceParser(args.foldername + '/' + file)
            print(parser_obj_folder.parser())
elif args.learner:
    print("Learner Mode")
    captcha_verifer()
    from learner.learner import *