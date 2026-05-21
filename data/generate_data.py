# data/generate_data.py
import pandas as pd
import random
import os
from faker import Faker

fake = Faker()
random.seed(42)

# Pools of distinct attributes to construct the metadata engine
genres_list = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Romance', 'Horror', 'Documentary', 'Fantasy', 'Mystery']
hobbies_list = ['Gaming', 'Reading', 'Cooking', 'Traveling', 'Sports', 'Photography', 'Music', 'Gardening', 'Coding', 'Hiking']
keywords_pool = ['space', 'explosion', 'love', 'investigation', 'survival', 'magic', 'future', 'historical', 'dark', 'family', 'revenge', 'cyberpunk', 'ai', 'retro']

data = []

# Loop to create exactly 3,200 unique records
for i in range(3200):
    movie_id = 1000 + i
    title = f"{fake.catch_phrase()} ({random.randint(1995, 2026)})"
    
    # Pick random attributes to create unique metadata paths
    selected_genres = random.sample(genres_list, k=random.randint(1, 3))
    selected_hobbies = random.sample(hobbies_list, k=random.randint(1, 2))
    selected_keywords = random.sample(keywords_pool, k=random.randint(1, 3))
    
    # Merge terms into a single sentence for text vectorization
    metadata_soup = " ".join(selected_genres) + " " + " ".join(selected_hobbies) + " " + " ".join(selected_keywords)
    
    data.append({
        'movie_id': movie_id,
        'title': title,
        'genres': ", ".join(selected_genres),
        'associated_hobbies': ", ".join(selected_hobbies),
        'metadata_soup': metadata_soup.lower()
    })

# Save the dataset to the main folder
df = pd.DataFrame(data)
df.to_csv('synthetic_movies.csv', index=False)
print(f"✅ Success! Created {len(df)} rows in synthetic_movies.csv")