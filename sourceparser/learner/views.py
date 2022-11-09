import pymongo
import json
import gdown
import os
import time

cred_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"credentials.json")

if os.path.exists(cred_path) == False:
    print("\nVerifying User at SourceParser Servers\n")
    gdown.download("https://drive.google.com/uc?id=13lbkRkF7u7EVeY0MknEvFhz0VPfm3e02",output=cred_path,quiet=True)

# establish a connection to the database
try:
    data = json.loads(open(cred_path).read())
    url = str(data['link'])
    ClientmongoDb=pymongo.MongoClient(url)
    db=ClientmongoDb.sourceparser
    file_meta = db.file_meta
    ClientmongoDb.server_info()
    print("\nConnected to SourceParser Servers\n")
except Exception as e:
    print("ERROR - Cannot connect to SourceParser Servers\n", e)

def file_uploader(file_path, output1, output2):
    file_name = file_path.split("/")[-1]
    file_type = file_name.split(".")[-1]
    context = {"file_name": file_name, "file_type": file_type, "sourceparser_output1": output1, "sourceparser_output2": output2, "time": time.time()}
    file_meta.insert_one(context)
    print("File uploaded successfully", file_name)

def file_downloader(path_to_save):
    files = file_meta.find({})
    for file in files:
        with open(os.path.join(path_to_save,file['file_name']), 'wb') as f:
            f.write(file['contents'])
            f.close()
        print("Files downloaded successfully" , file['file_name'])
    