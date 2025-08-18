from textblob import TextBlob

text= TextBlob(input("Enter the text to analyze the sentiment: "))

#The text.detect_language()
print(text.sentiment)
Sentiment= text.sentiment.polarity

match Sentiment:
    case x if x > 0:
        print("Positive")
    case x if x == 0:
        print("Neutral")
    case x if x < 0:
        print("negative")
    case _:
        print("Unknown sentiment!")

