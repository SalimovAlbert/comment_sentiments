import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

sentiment_model = "seara/rubert-tiny2-russian-sentiment"
summarization_model = "IlyaGusev/rut5_base_sum_gazeta" # "IlyaGusev/mbart_ru_sum_gazeta"

PATH_DATA = "data"
NAME_DATA = "dataset_sentiments.csv"

col_sentiment = "sentiment"
col_text_comment = "text_comment"
