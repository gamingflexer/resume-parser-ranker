import argparse
import pyfiglet

word=pyfiglet.figlet_format("SourceParser")
parser = argparse.ArgumentParser(description="SourceParser")

parser.add_argument("-f","--filename", type=str)
parser.add_argument("-fn","--foldername", type=str)
parser.add_argument("-l","--learner", action='store_true')

args = parser.parse_args()
print(word)

if args.filename:
    from sourceparser import SourceParser
    parser_obj_file = SourceParser(str(args.filename))
    print(parser_obj_file.parser())
elif args.foldername:
    from sourceparser import SourceParser
    parser_obj_folder = SourceParser(str(args.foldername))
    print(parser_obj_folder.parser())
elif args.learner:
    print("Learner Mode")
    from learner.learner import *