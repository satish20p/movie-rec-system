# app.py
import streamlit as st
from movie_rec_model import MovieRecommender

# 1. Page Config Setup
st.set_page_config(page_title="Hobby Movie Recs", page_icon="🎬", layout="centered")

# 2. Load Recommendation Engine
try:
    recommender = MovieRecommender('data/synthetic_movies.csv')
except FileNotFoundError:
    st.error("Dataset not found! Please open your terminal and run 'python data/generate_data.py' first.")
    st.stop()

# 3. User Interface Architecture
st.title("🎬 Hobby-Based Movie Recommendation System")
st.write("Our Content-Based Filtering model maps your hobbies and entertainment preferences straight to our 3,000+ movie database.")

# UI Entry Forms
with st.form("preferences_matrix_form"):
    st.subheader("🛠️ Step 1: Customize Your Profiling Matrix")
    
    available_genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Thriller', 'Romance', 'Horror', 'Documentary', 'Fantasy', 'Mystery']
    available_hobbies = ['Gaming', 'Reading', 'Cooking', 'Traveling', 'Sports', 'Photography', 'Music', 'Gardening', 'Coding', 'Hiking']
    
    user_genres = st.multiselect("Select your favorite movie genres:", available_genres)
    user_hobbies = st.multiselect("Select your core hobbies / everyday interests:", available_hobbies)
    user_vibe = st.text_input("Optional keywords or specific themes (e.g., space, cyberpunk, revenge):")
    
    generate_recs = st.form_submit_button(label="Generate Recommendations")

# 5. Live ML Inference Engine Execution
if generate_recs:
    if not user_genres and not user_hobbies and not user_vibe:
        st.warning("Please select at least one genre or hobby to help our system calculate matches.")
    else:
        with st.spinner("Calculating vector distances across matrix..."):
            top_recommendations = recommender.recommend(
                genres=user_genres,
                hobbies=user_hobbies,
                keywords=user_vibe,
                top_n=5,
            )

            st.success("Analysis complete! Here are your matches:")
            st.write("---")

            for _, row in top_recommendations.iterrows():
                match_percentage = round(row['match_confidence'] * 100, 1)

                if match_percentage > 0:
                    st.subheader(f"🎥 {row['title']}")
                    st.write(f"**🎭 Genres:** {row['genres']} | **🧩 Aligned Hobbies:** {row['associated_hobbies']}")
                    st.progress(int(match_percentage))
                    st.caption(f"Vector Similarity Score: {match_percentage}%")
                    st.write("---")
                else:
                    st.info("No explicit contextual match found for this precise combination. Try tweaking your input words!")
                    break