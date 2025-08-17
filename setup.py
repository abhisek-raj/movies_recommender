from setuptools import setup, find_packages

setup(
    name="movie-recommender",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'streamlit==1.32.0',
        'pandas==2.1.0',
        'numpy==1.26.0',
        'scikit-learn==1.3.0',
    ],
    python_requires='>=3.8',
    author="Avisek",
    description="A movie recommendation system built with Streamlit",
    url="https://github.com/yourusername/movies_recommender"
)
