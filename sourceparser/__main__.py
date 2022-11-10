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
parser.add_argument("-sm","--summariser", action='store_true')
parser.add_argument("-mb","--multiBatch", action='store_true')
parser.add_argument("-gpu","--gpuPresent", action='store_true')

args = parser.parse_args()
print(word)

if args.filename :
    if args.summariser == False:
        print("\nINFO - Filename Should not contain any Whilespaces\n")
        from sourceparser import SourceParser
        parser_obj_file = SourceParser(str(args.filename))
        print(parser_obj_file.parser())
        if args.learner:
            captcha_verifer()
            from learner.learner import *
            # add to database
    else:
        if args.learner:
            captcha_verifer()
            from learner.learner import *
        from summarizer.summarizer import *
        from tika import parser
        main_model = summarize_intializer_main()
        if args.gpuPresent:
            model = summarize_intializer_model(model = main_model,gpu=True)
        else:
            model = summarize_intializer_model(model = main_model,gpu=False)
        raw = parser.from_file(str(args.filename))
        text = raw['content']
        if args.multiBatch:
            summary = summarize_text(model,text,multi_batch=True)
            print(summary[0])
        else:
            summaries = summarize_text(model,text,multi_batch=False)
            for each_summary in summaries:
                print(each_summary[0])
            
            
        
    
if args.foldername:
    from sourceparser import SourceParser
    os_dir = os.listdir(args.foldername)
    if args.learner:
        captcha_verifer()
        from learner.learner import *
        # add to db
    for file in os_dir:
        if file.endswith(tuple(['.pdf', '.docx', '.doc','.txt','.rtf','.html','.htm','.odt'])):
            file_path = os.path.join(args.foldername,file)
            parser_obj_folder = SourceParser(args.foldername + '/' + file)
            print(parser_obj_folder.parser())
            
    