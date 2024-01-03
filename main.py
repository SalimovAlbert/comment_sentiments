from fastapi import FastAPI
import config
from src import pipeline_sentiment, pipeline_stats, pipeline_summarize
from pydantic import BaseModel
from transformers import pipeline
import uvicorn
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

model_sent = pipeline(model=config.sentiment_model)
model_summ = pipeline(model=config.summarization_model)

app = FastAPI()

class YouTubeUrl(BaseModel):
    url_video: str

@app.post('/get_data')
def get_data_sentiment(youtube: YouTubeUrl):
    print("Got GET request")
    data = pipeline_sentiment(youtube.url_video, config.YOUTUBE_API_KEY, model_sent)
    data.to_csv(f"{config.PATH_DATA}/{config.NAME_DATA}", index=False)
    return {'message': 'Успешно'}
   
@app.post('/get_stats_sentiment') 
def get_stats_sentiment():
    if f"{config.NAME_DATA}" in os.listdir(f"{config.PATH_DATA}"):
        data = pd.read_csv(f"{config.PATH_DATA}/{config.NAME_DATA}")
        if config.col_sentiment in data.columns:
            return pipeline_stats(data, config.col_sentiment)

@app.post('/get_summarization') 
def get_summarization():
    if f"{config.NAME_DATA}" in os.listdir(f"{config.PATH_DATA}"):
        data = pd.read_csv(f"{config.PATH_DATA}/{config.NAME_DATA}")
        if config.col_text_comment in data.columns:
            return pipeline_summarize(data[config.col_text_comment], model_summ)

if __name__ == "__main__":  
    uvicorn.run(app, host="127.0.0.1", port=8000)