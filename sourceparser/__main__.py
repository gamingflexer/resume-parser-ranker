import argparse
import pyfiglet
import os
from utils import captcha_verifer

word = pyfiglet.figlet_format("SourceParser")
parser = argparse.ArgumentParser(description="SourceParser")

parser.add_help = True
parser.add_argument("-f","--filename", type=str, help="File name to parse")
parser.add_argument("-fn","--foldername", type=str, help="Folder name to parse files in the folder")
parser.add_argument("-l","--learner", action='store_true',help="Uploads the file to the server for learning")
parser.add_argument("-sm","--summariser", action='store_true',help="Summarises the file")
parser.add_argument("-mb","--multiBatch", action='store_true',help="Multi Batch Summariser")
parser.add_argument("-gpu","--gpuPresent", action='store_true',help="Add if GPU Present")
parser.add_argument("-json","--json", action='store_true',help="Add if you want to save the output as json")

args = parser.parse_args()
print(word)

if args.filename :
    if args.summariser == False:
        print("\nINFO - Filename Should not contain any Whilespaces\n")
        from sourceparser import SourceParser
        parser_obj_file = SourceParser(str(args.filename))
        data = parser_obj_file.parse()
        print(data)
        if args.json :
            json.dumps(data, open(f"{str(args.filename)}_sourceparser.json", "w"))                
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
        if args.multiBatch == False:
            raw = parser.from_file(str(args.filename))
            text = raw['content']
            summary = summarize_text(model,text,multi_batch=True)
            print(summary)
            if args.json:
                json.dumps({"summary":summary}, open(f"{str(args.filename)}_summary_sourceparser.json", "w"))    
        else:
            if args.foldername:
                text_list = []
                os_dir = os.listdir(str(args.foldername))
                for file in os_dir:
                    if file.endswith(tuple(['.pdf', '.docx', '.doc','.txt','.rtf','.html','.htm','.odt'])):
                        file_path = os.path.join(args.foldername,file)
                        raw = parser.from_file(file_path)
                        text = raw['content']
                        text_list.append(text)
                summaries = summarize_text(model,text_list,multi_batch=False)
                for each_summary in summaries:
                    print(each_summary)
                    if args.json:
                        json.dumps({"summary":each_summary}, open(f"{str(args.filename)}_summary_sourceparser.json", "w"))    
                
            
        
    
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
            data = parser_obj_folder.parser()
            print(data)
            if args.json:
                json.dumps(data, open(f"{file}_sourceparser.json", "w"))    
            
    