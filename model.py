import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class BaliTourismRecommender:
    def __init__(self, csv_path):
        """
        Inisialisasi model dengan load dataset dan preprocessing.
        """
        self.df = pd.read_csv(csv_path)
        self.df['features'] = self.df['kategori'] + ' ' + self.df['preferensi']
        self.tfidf = TfidfVectorizer()
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['features'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        self.indices = pd.Series(self.df.index, index=self.df['nama']).drop_duplicates()

    def recommend(self, place_name, top_n=10):
        """
        Memberikan rekomendasi tempat wisata mirip berdasarkan nama tempat.

        Args:
            place_name (str): Nama tempat wisata untuk dicari kemiripannya.
            top_n (int): Jumlah rekomendasi yang diinginkan.

        Returns:
            pd.DataFrame atau str: DataFrame tempat rekomendasi atau pesan error jika tidak ditemukan.
        """
        if place_name not in self.indices:
            return f"Place '{place_name}' not found in dataset."
        idx = self.indices[place_name]
        sim_scores = list(enumerate(self.cosine_sim[idx].flatten()))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        place_indices = [i[0] for i in sim_scores]
        return self.df[['nama', 'kategori', 'rating']].iloc[place_indices]
