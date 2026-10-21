from rapidfuzz import process, fuzz, utils

def find_candidates (df, movie_name, results_limit, similarity):
    """
    Finds similar movie titles in an IMDb DataFrame using RapidFuzz.
    Args:
        df: DataFrame containing IMDb movie data.
        movie_name: Movie title provided by the user.
        results_limit: Number of candidates to return.
        similarity: Minimum similarity score required for a match.
    Returns:
        A list of movie titles that match the user's search.
    """

    top_matches = process.extract(
        movie_name,
        df['Movie Name'], 
        scorer=fuzz.partial_ratio,
        processor=utils.default_process,
        limit=results_limit,
        score_cutoff=similarity
    )

    candidate_titles = [title[0] for title in top_matches]

    return candidate_titles
