from simplet5 import SimpleT5
from config import summary_model
import gdown #1uIgVgTFvDt0YtSksMjIXw-fzKGF4-N3B
import re
import os

def summarize_intializer_main(model_type="t5", model_name="t5-small"):
    model = SimpleT5()
    model.from_pretrained(model_type=model_type, model_name=model_name)
    return model

def summarize_intializer_model(model,gpu=True):
    if not os.path.exists(summary_model):
                os.mkdir(summary_model)
    gdown.download("https://drive.google.com/uc?id=1uIgVgTFvDt0YtSksMjIXw-fzKGF4-N3B",output=summary_model,quiet=False)
    if gpu:
        model.load_model(summary_model, use_gpu=True)
    else:
        model.load_model(summary_model, use_gpu=False)
    return model
    
def summarize_text(model, text, multi_batch=True):
    if multi_batch:
        summaries = []
        for each_text in text:
            each_text = re.sub('\n'," ",str(each_text))
            each_text = re.sub('\\n'," ",str(each_text))
            text_to_summarize=f"""summarize:{each_text}"""
            summary = model.predict(text_to_summarize)
            summaries.append(summary)
        return summaries
    else:
        text = re.sub('\n'," ",str(text))
        text = re.sub('\\n'," ",str(text))
        text_to_summarize=f"""summarize:{text}"""
        summary = model.predict(text_to_summarize)
    return summary
