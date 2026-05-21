# Hobby Movie Recommendation System

A lightweight Streamlit app that recommends movies based on user-selected genres, hobbies, and optional keywords.

## Project structure

- `app.py` - main Streamlit application
- `requirements.txt` - Python dependencies
- `data/generate_data.py` - script to generate a synthetic movie dataset
- `data/synthetic_movies.csv` - generated dataset used by the app

## Setup

1. Create or activate a Python virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Generate the dataset

```powershell
python data/generate_data.py
```

4. Run the app

```powershell
python -m streamlit run app.py
```

## Notes

- If the dataset is missing, `app.py` will show an error and prompt you to run `python data/generate_data.py`.
- The app uses TF-IDF and cosine similarity to match your profile against synthetic movie metadata.

## Deploy to Streamlit

This project is ready for Streamlit Community Cloud deployment.

1. Push your repository to GitHub (already done at `https://github.com/satish20p/movie-rec-system`).
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in.
3. Click **New app** and connect your GitHub account.
4. Select `satish20p/movie-rec-system`, choose the branch `master`, and set the main file to `app.py`.
5. Click **Deploy**.

Streamlit will install dependencies from `requirements.txt` and launch `app.py` automatically.

> If you update the app, push a new commit and Streamlit Cloud will rebuild your app.

## Dependencies

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `faker`
