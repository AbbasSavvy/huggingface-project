from fastapi import FastAPI
from .summarizer import get_summarizer

app = FastAPI()
summarizer = get_summarizer()


@app.post("/summarize")
def summarize(text: str):
    summary = summarizer(text, max_length=60, min_length=25, do_sample=False)
    return {"summary": summary[0]["summary_text"]}


# test