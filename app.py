import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

# Load TMDB API Key
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# Load pickle files from Hugging Face
@st.cache_resource
def load_pickle_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return pickle.loads(response.content)

# Hugging Face URLs
movie_list_url = "https://huggingface.co/datasets/saakshammm/movie-rec/resolve/main/artifacts/%20movie_list.pkl"
similarity_url = "https://huggingface.co/datasets/saakshammm/movie-rec/resolve/main/artifacts/%20similarity.pkl"

# Load data
movies = load_pickle_from_url(movie_list_url)
similarity = load_pickle_from_url(similarity_url)

# Fetch poster from TMDB
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w200{poster_path}"
    except:
        pass
    return None

# Recommend movies
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_posters.append(poster_url)
        if len(recommended_movies) == 8:
            break

    return recommended_movies, recommended_posters

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🎬 Movie Recommendation Engine")

selected_movie = st.selectbox("Type or select a movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"**{names[i]}**")

    cols = st.columns(4)
    for i in range(4, 8):
        with cols[i - 4]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"**{names[i]}**")
