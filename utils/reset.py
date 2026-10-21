import streamlit as st

def reset():
    """
    Resets the search inputs and session state to their default values.

    Cleans the user's input and selected movie title, resets the result
    limit to 5, and clears the previous search query.


    """
    st.session_state.user_input = ""
    st.session_state.limit = 5
    st.session_state.pop("selected_title", None)
    st.session_state.pop("previous_query", None)
