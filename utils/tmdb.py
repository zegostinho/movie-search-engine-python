import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

ACCESS_TOKEN = st.secrets.get(
    "TMDB_ACCESS_TOKEN",
    os.getenv("TMDB_ACCESS_TOKEN")
)

url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}


@st.cache_data(ttl=3600)
def movie_search(user_query):
    """
    Searches for movies using the TMDB API.
    Args:
        user_query: Movie title entered by the user.

    Returns:
        List of dictionaries containing movie data, or None if the
        response does not contain a 'results' key.

    """
    params = {
        "query": user_query
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data.get("results")