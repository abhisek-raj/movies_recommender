import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np
import gdown
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Load movies data
movies = pickle.load(open('movies.pkl', 'rb'))

# Download similarity matrix from Google Drive if it doesn't exist
SIMILARITY_FILE = 'similarity.pkl'
GDRIVE_FILE_ID = '14rq6b1Y4dbAzGk5GfUlWlGl8ITPCXUpK'  # Google Drive file ID

def download_from_drive(file_id, output):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output, quiet=False)

if not os.path.exists(SIMILARITY_FILE):
    st.info("Downloading similarity matrix...")
    try:
        download_from_drive(GDRIVE_FILE_ID, SIMILARITY_FILE)
        st.success("Similarity matrix downloaded successfully!")
    except Exception as e:
        st.warning("Couldn't download the similarity matrix. Generating it locally... (This may take a while)")
        # Fallback to local generation if download fails
        tfidf = TfidfVectorizer(stop_words='english')
        movies['overview'] = movies['overview'].fillna('')
        tfidf_matrix = tfidf.fit_transform(movies['overview'])
        similarity = linear_kernel(tfidf_matrix, tfidf_matrix)
        with open(SIMILARITY_FILE, 'wb') as f:
            pickle.dump(similarity, f)
        st.success("Similarity matrix generated locally!")

# Load the similarity matrix
with open(SIMILARITY_FILE, 'rb') as f:
    similarity = pickle.load(f)

st.title('Movie Recommender System')

# Add bold introduction line with effect (larger font size and color)
st.markdown(
    "<span style='font-size: 22px; color: #FF5733; font-weight: bold;'>"
    "hey! my name avisek, i guess your movies basis on your interest in movie"
    "</span>",
    unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
