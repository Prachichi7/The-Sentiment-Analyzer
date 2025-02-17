'''from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia= SentimentIntensityAnalyzer()

text= input("Enter a sentence for sentiment analyzing: ")

def sentiment_analysis(text):   
    #sia= SentimentIntensityAnalyzer()
    sentiment_score= sia.polarity_scores(text)["compound"]
    
    match sentiment_score:
        case x if x > 0:
            print("Positive Sentiment")
        case x if x == 0:
            print("Neutral Sentiment")
        case x if x < 0:
            print("Negative Sentiment")
        case _:
            print("Invalid Score")


sentiment_analysis(text)'''


import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia= SentimentIntensityAnalyzer()
file_path= r'D:\sentimentanalyzerprojwithpy\sentimentdataset.csv'

def sentiment_analysis(file_path):   
    #sia= SentimentIntensityAnalyzer()
    df= pd.read_csv(file_path)

    for text in df["text"]:  # Loop through each text in the CSV
        sentiment_score = sia.polarity_scores(text)["compound"]
        match sentiment_score:
            case x if x > 0:
                print("Positive Sentiment")
            case x if x == 0:
                print("Neutral Sentiment")
            case x if x < 0:
                print("Negative Sentiment")
            case _:
                print("Invalid Score")


sentiment_analysis(file_path)

'''df= pd.read_csv(file_path)
print(df)'''




















'''compound= SentimentIntensityAnalyzer 
match compound:
    case x if x > 0.05:
        print("Positive")
    case x if x <- 0.05:
        print("Neutral")
    case x if 0.05 < x > -0.05:
        print("negative")
    case _:
        print("Unknown sentiment!")'''