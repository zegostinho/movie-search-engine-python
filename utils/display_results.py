import streamlit as st

def display_results(results_from_api, results_limit):
    """
    Processes the results and displays them in the application interface.
    Args:
        results_from_api: List of dictionaries containing movie data returned by the API.
        results_limit: Number of results to display, chosen by the user.

    Returns:
        Displays each movie in an expander, showing its title, release year,
        rating, synopsis, and poster when available.
    """

    for movie in results_from_api[:results_limit]:
        if not movie.get("title"):
            continue

        title = movie["title"]
        release_date = str(movie.get("release_date") or "N/A").split("-")[0]
        rating = "N/A"
        synopsis = movie.get("overview") or "N/A"
        poster = None
        vote_average = movie.get("vote_average")

        if vote_average is not None and vote_average > 0:
            rating = round(vote_average, 1)

        if movie.get("poster_path"):
            base_url = "https://image.tmdb.org/t/p/"
            size = "w185"
            poster = base_url + size + movie.get("poster_path")

        with st.expander(f"✅ {title} ({release_date})"):
            col1, col2 = st.columns([1, 3], gap="medium")
            with col1:
                if poster:
                    st.image(poster)
                else:
                    st.write("*Poster not available.*")
            with col2:
                st.write(f"⭐️ **Rating:** {rating}")
                st.write(f"📖 **Synopsis:** {synopsis}")
