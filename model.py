import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import string

offers_df = pd.read_csv('Data/offer_retail_clean.csv')
categories_df = pd.read_csv('Data/categories.csv')
brand_category_df = pd.read_csv('Data/brand_category.csv')

offers_df.head()

# Function to preprocess text
def preprocess_text(text, brand, retailer):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    # Include brand and retailer information in the processed text
    text += f" {brand} {retailer}"
    return text

# Apply the updated preprocessing to relevant columns in the merged dataframe
offers_df['processed_text'] = offers_df.apply(lambda row: preprocess_text(row['OFFER'], row['BRAND'], row['RETAILER']), axis=1)

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the processed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(offers_df['processed_text'])

def get_relevant_offers_df(user_input, tfidf_matrix, offers_df):
    user_input_processed = preprocess_text(user_input, '', '')  # Include brand and retailer information in user input
    user_input_vector = tfidf_vectorizer.transform([user_input_processed])

    similarity_scores = cosine_similarity(user_input_vector, tfidf_matrix).flatten()
    offers_df['similarity_score'] = similarity_scores

    relevant_offers = offers_df.sort_values(by='similarity_score', ascending=False)

    # Create a new DataFrame with relevant information
    relevant_offers_df = pd.DataFrame({
        #'USER_INPUT': [user_input] * len(relevant_offers),  # Repeat user input for each relevant offer
        'OFFER': relevant_offers['OFFER'],
        'RETAILER': relevant_offers['RETAILER'],
        'BRAND': relevant_offers['BRAND'],
        'SIMILARITY_SCORE': relevant_offers['similarity_score']
    }).head(5).reset_index(drop=True)

    relevant_offers_df.index += 1

    return relevant_offers_df

result_df = get_relevant_offers_df("plant based", tfidf_matrix, offers_df)

# # Display the relevant offers DataFrame
result_df.head(10)