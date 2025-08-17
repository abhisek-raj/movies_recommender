from setuptools import setup, find_packages

setup(
    name="movie-recommender",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'scikit-learn',
        'gdown',
    ],
    python_requires='>=3.8',
    author="Avisek",
    description="A movie recommendation system built with Streamlit",
    url="https://github.com/yourusername/movies_recommender"
)

