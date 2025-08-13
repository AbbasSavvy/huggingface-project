from transformers import pipeline

def get_summarizer():
    return pipeline(task="summarization", model="facebook/bart-large-cnn")

