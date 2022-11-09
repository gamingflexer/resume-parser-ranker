import argparse
import pyfiglet
from sourceparser import SourceParser

word=pyfiglet.figlet_format("SourceParser")
parser = argparse.ArgumentParser(description="SourceParser")

parser.add_argument("--filename", type=str)
parser.add_argument("--foldername", type=str)

args = parser.parse_args()
print(word)
parser_obj_file = SourceParser(str(args.filename))
parser_obj_folder = SourceParser(str(args.foldername))

if args.filename:
    print(parser_obj_file.parser())
elif args.foldername:
    print(parser_obj_folder.parser())
