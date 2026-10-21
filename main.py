import streamlit as st
import requests
from utils.read_data import load_dataset
from utils.candidates_search import find_candidates
from utils.tmdb import movie_search
from utils.reset import reset
from utils.display_results import display_results


# Configuration of the web page
st.set_page_config(
    page_title='Find Any Movie',
    page_icon='🎬',
    layout='wide'
)

# Load the IMDb dataset for similar title suggestions
df = load_dataset("data/top_1000_imdb_movies.csv")


st.title('Movie Search Engine 🎬', text_alignment='center')
st.subheader(
    "Find any movie even if you don't remember its correct title! 🕵",
    divider='rainbow',
    text_alignment='center'
)

st.markdown('')

if "user_input" not in st.session_state:
    st.session_state.user_input = ""


if "limit" not in st.session_state:
    st.session_state.limit = 5

col1, col2 = st.columns(2, gap="medium")

with col1:
    user_input = st.text_input(
        "Which movie are you looking for? 🔎",
        placeholder="Type here",
        key="user_input"
        )

with col2:
    result_options = list(range(1, 11))
    limit = st.selectbox(
        "How many results do you want to see? 🎯",
        options=result_options,
        key="limit"
        )


# Display search results

if user_input:
    try:
        original_query = user_input

        if user_input != st.session_state.get("previous_query"):
            st.session_state.pop("selected_title", None)

        st.session_state["previous_query"] = user_input

        search_query = st.session_state.get("selected_title") or original_query
        movies = movie_search(search_query)

        if movies is None:
            st.error("Unable to retrieve movie results.")

        elif movies == []:
            candidates = find_candidates(df, original_query, 5, 70)
            if not candidates:
                st.write("No matches found ☹️")

            else:
                st.write(f"No matches found for *{search_query}*.")
                st.write("Is one of these titles close to your search?")

                for candidate in candidates:
                    if st.button(candidate):
                        st.session_state["selected_title"] = candidate
                        st.rerun()


        else:
            display_results(movies, limit)

            st.button("RESET", on_click=reset, icon='🔄')

    except requests.exceptions.Timeout:
        st.error("The request timed out.")

    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the server.")

    except requests.exceptions.HTTPError as error:
        new_response = error.response

        if new_response is not None:
            message = new_response.json()
            st.error(
                f"Error {new_response.status_code}. "
                f"{message.get("status_message", "Unexpected HTTP error.")}"
            )

    except requests.exceptions.JSONDecodeError:
        st.error("The server returned an invalid response")



st.caption("*This project was developed using Streamlit and The Movie Database API*", text_alignment='center')
