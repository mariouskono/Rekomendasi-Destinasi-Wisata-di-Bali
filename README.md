# Bali Tourist Attractions Recommendation System

## Project Overview

This project implements a **Content-Based Recommendation System** for tourist attractions in Bali, Indonesia. Using a cleaned dataset of 772 attractions collected from Google Maps, the system recommends similar places based on categories and visitor preferences.

## Features

- Dataset includes detailed information: name, category, location, rating, preference, coordinates, and images.
- Content-based filtering using TF-IDF vectorization and cosine similarity.
- Provides top-10 recommendations for any given tourist spot.
- Visualizations for data distribution and similarity heatmaps.
- Easy-to-use Python module for recommendations.

## Dataset

The dataset was collected via automated scraping from Google Maps and is publicly available on Kaggle:

[Bali Tourist Attractions Dataset from Google Maps](https://www.kaggle.com/datasets/bertnardomariouskono/bali-tourist-attractions-dataset-from-google-maps)

## Usage

1. Run the Jupyter notebook (`notebook.ipynb`) to explore the data, train the model, and generate recommendations.
2. Use the Python module (`model.py`) to integrate the recommendation system into your applications.

Example usage in Python:

```python
from model import BaliTourismRecommender

recommender = BaliTourismRecommender('dataset_tempat_wisata_bali_cleaned.csv')
recommendations = recommender.recommend('Taman Mumbul Sangeh')
print(recommendations)
