from simplet5 import SimpleT5
from config import summary_model
import gdown #1uIgVgTFvDt0YtSksMjIXw-fzKGF4-N3B
import re
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def summarize_intializer_main(model_type="t5", model_name="t5-small"):
    model = SimpleT5()
    model.from_pretrained(model_type=model_type, model_name=model_name)
    return model

def summarize_intializer_model(model,gpu=True):
    if not os.path.exists(summary_model):
                os.mkdir(summary_model)
    gdown.download("https://drive.google.com/uc?id=1NOLDkHFz8rXiKselDEILHvJtb7ux2GZQ",output=os.path.join(summary_model,"config.json"),quiet=True)
    gdown.download("https://drive.google.com/uc?id=14pv8jDmtYPX8yH9aQ0JFWvfjY3XtYY2k",output=os.path.join(summary_model,"pytorch_model.bin"),quiet=True)
    gdown.download("https://drive.google.com/uc?id=1xaVnAJIXnFs-XA77LS0ibQYaJdRHu0aS",output=os.path.join(summary_model,"special_tokens_map.json"),quiet=True)
    gdown.download("https://drive.google.com/uc?id=1GMmnmLZoclWSEO94b3CaymuFjo1A8RU5",output=os.path.join(summary_model,"spiece.model"),quiet=True)
    gdown.download("https://drive.google.com/uc?id=1_CQEFhMLSFYtkweYs-c5zPXjM0_Hcnh9",output=os.path.join(summary_model,"tokenizer_config.json"),quiet=True)
    gdown.download("https://drive.google.com/uc?id=1U94kPlarDdVQQfR_MNpQsV4ufidfKAd7",output=os.path.join(summary_model,"tokenizer.json"),quiet=True)
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
            text_to_summarize=f"""summarize:{each_text[:511]}"""
            summary = model.predict(text_to_summarize)
            summaries.append(summary)
        return summaries
    else:
        text = re.sub('\n'," ",str(text))
        text = re.sub('\\n'," ",str(text))
        text_to_summarize=f"""summarize:{text[:511]}"""
        summary = model.predict(text_to_summarize)
    return summary
