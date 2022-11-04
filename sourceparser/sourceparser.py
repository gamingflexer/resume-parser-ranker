from parser1 import resumeparse
from parser2 import resumeparse2
from postprocessing import postprocess

class SourceParser:
    def __init__(self, filename):
        self.filename = filename
    
    def parser(self):
        to_delete = ['email', 'phone', 'name', 'total_exp',
                    'designition','FileName','skills', 'File Language']
        
        p1 = resumeparse.read_file(self.filename)
        p2 = resumeparse2.get_parsed(self.filename)
    
        
        p2.update(p1)
        for i in to_delete:
            try:
                del p2[i]
            except:
                continue
            
        p1 = postprocess(p2)
        return p1