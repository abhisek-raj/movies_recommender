# Movie Recommender System

A Streamlit-based web application that recommends movies based on user preferences using content-based filtering.

## Features
- Browse and select from a collection of movies
- Get personalized movie recommendations
- Simple and intuitive user interface

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movies_recommender
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Select a movie from the dropdown and click 'Recommend' to get similar movie suggestions

## Deployment

### Streamlit Cloud (Recommended)
1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click 'New app' and connect your GitHub repository
4. Select the branch and main file (app.py)
5. Click 'Deploy!'

### Other Cloud Platforms
This app can also be deployed on:
- Heroku
- AWS Elastic Beanstalk
- Google App Engine

## Project Pipeline

### Data Collection
1. **Source Data**: The system uses a dataset containing movie information including titles, genres, and other relevant features.
2. **Data Format**: 
   - Movie metadata (title, genre, director, actors, etc.)
   - User ratings and interactions (if available)

### Data Preprocessing
1. **Data Cleaning**:
   - Handling missing values
   - Removing duplicates
   - Standardizing text data

2. **Feature Engineering**:
   - Combining relevant features (e.g., combining genres, actors, director)
   - Text vectorization using TF-IDF or similar methods
   - Creating a combined feature vector for each movie

### Model Training
1. **Similarity Calculation**:
   - Using cosine similarity to find similar movies
   - The similarity is calculated based on the combined feature vectors
   - Results are stored in `similarity.pkl`

2. **Model Persistence**:
   - Preprocessed movie data is saved to `movies.pkl`
   - Similarity matrix is saved to `similarity.pkl`

### Web Application
1. **User Interface**:
   - Built with Streamlit
   - Simple dropdown for movie selection
   - Displays top 5 similar movies

2. **Recommendation Logic**:
   - Loads precomputed similarity matrix
   - Finds most similar movies based on user selection
   - Returns results in real-time

## How to Generate/Update Data

### Prerequisites
- Python 3.8+
- Required packages (install via `pip install -r requirements.txt`)
- Source movie dataset (CSV/JSON format)

### Steps to Generate Data
1. **Prepare Source Data**:
   ```python
   import pandas as pd
   
   # Load your dataset
   movies = pd.read_csv('your_dataset.csv')
   ```

2. **Preprocess Data**:
   ```python
   from sklearn.feature_extraction.text import TfidfVectorizer
   from sklearn.metrics.pairwise import cosine_similarity
   
   # Combine features into a single string
   movies['combined_features'] = movies['genres'] + ' ' + movies['director'] + ' ' + movies['actors']
   
   # Create TF-IDF matrix
   tfidf = TfidfVectorizer(stop_words='english')
   tfidf_matrix = tfidf.fit_transform(movies['combined_features'])
   
   # Calculate similarity matrix
   similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
   ```

3. **Save Processed Data**:
   ```python
   import pickle
   
   # Save the movie data
   with open('movies.pkl', 'wb') as f:
       pickle.dump(movies, f)
   
   # Save the similarity matrix
   with open('similarity.pkl', 'wb') as f:
       pickle.dump(similarity, f)
   ```

### Updating the Dataset
1. Replace or update the source dataset
2. Run the preprocessing script again
3. The existing `movies.pkl` and `similarity.pkl` will be overwritten
4. The web app will automatically use the new data on next startup

## Project Structure
- `app.py`: Main application file
- `movies.pkl`: Preprocessed movie data
- `similarity.pkl`: Precomputed similarity matrix
- `requirements.txt`: Python dependencies
- `data_preparation.py`: Script to generate/update the recommendation data (create this file if needed)