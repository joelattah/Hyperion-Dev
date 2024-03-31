import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

nlp= spacy.load("en_core_web_md")  #load language package

#load the dataset
amazon_reviews = pd.read_csv('amazon_product_reviews.csv', low_memory=False)



#Preprocess the text data
#amazon_reviews = amazon_reviews.dropna(subset=['reviews.text'])# remove all missings values from reviews column
reviews_data = amazon_reviews[['reviews.text']] #selects review column  and removes missing values


#Creating a function to preprocess text
def preprocess(reviews_text):
    #function performs necessary text cleaning prior to analysis
    doc = nlp(reviews_text.lower().strip())
    #removes stopwords and punctuation prior to text analysis
    processed_text = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct] #if token is not a stopword (words that have no meaning)and not a punctuation mark
    return ' '.join(processed_text)



reviews_data['processed.text'] = reviews_data['reviews.text'].apply(preprocess) #creates a new section called processed.txt which applies the preprocess function to reviews.txt


#function to analyse polarity
def analyse_polarity(reviews):
    #Preprocess the text with spaCy
    doc = nlp(reviews)

    #Analyze sentiment with Textblob
    blob = TextBlob(reviews)
    polarity = blob.sentiment.polarity # will give polairty value between -1 and 1

    return polarity



data = reviews_data['processed.text'].values #returns Numpy array containing the values
sentiments = [] #creates an empty list to contain the different sentiment classifications


for item in data: #iterates through array
    polarity_value = analyse_polarity(item)

     # Determine the sentiment based on polarity
    if polarity_value > 0:
        sentiment = 'positive'
    elif polarity_value < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    sentiments.append(sentiment) #appends sentiment to sentiments list
    

positive_count = sentiments.count('positive') #obtains num of positive reviews from sentiments list
negative_count = sentiments.count('negative')#obtains num of negative reviews from sentiments list
neutral_count = sentiments.count('neutral')#obtains num of neutral reviews from sentiments list

total = len(sentiments) #assigns variable total to equal number of reviews

positive_percentage = (positive_count / total)* 100 #calculates percentage of positive reviews
negative_percentage = (negative_count / total)* 100 #calculates percentage of negative reviews
neutral_percentage = (neutral_count / total)* 100 #calculates percentage of neutral reviews

print(f"Percentage of Positive Reviews: {positive_percentage:.2f}%")#rounds the percentage to 2 decimal places
print(f"Percentage of Negative Reviews: {negative_percentage:.2f}%")
print(f"Percentage of Neutral Reviews: {neutral_percentage:.2f}%")

