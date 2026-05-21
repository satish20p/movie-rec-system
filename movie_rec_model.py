import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path


class MovieRecommender:
    def __init__(self, csv_path: str = 'data/synthetic_movies.csv'):
        self.csv_path = Path(csv_path)
        self.df = self._load_dataset()
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['metadata_soup'])

    def _load_dataset(self) -> pd.DataFrame:
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Dataset not found at {self.csv_path}")
        return pd.read_csv(self.csv_path)

    @staticmethod
    def build_profile(genres, hobbies, keywords):
        genres_text = ' '.join(genres) if genres else ''
        hobbies_text = ' '.join(hobbies) if hobbies else ''
        keywords_text = keywords or ''
        return f"{genres_text} {hobbies_text} {keywords_text}".strip().lower()

    def recommend(self, genres, hobbies, keywords='', top_n=5) -> pd.DataFrame:
        user_profile = self.build_profile(genres, hobbies, keywords)
        if not user_profile:
            raise ValueError('At least one genre, hobby, or keyword is required for recommendations.')

        user_vector = self.tfidf.transform([user_profile])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix).flatten()

        results = self.df.copy()
        results['match_confidence'] = similarity_scores
        return results.sort_values(by='match_confidence', ascending=False).head(top_n)
