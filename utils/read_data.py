import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset(path):
    """
    Loads the IMDb movie dataset.
    Args:
        path: Path to the CSV file to load.

    Returns:
        A DataFrame containing the movie data.
    """
    df = pd.read_csv(path)

    return df
