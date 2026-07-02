from rapidfuzz import process, fuzz, utils

def encontrar_filme (df, nome_filme, limite, similaridade):
    """
    Esta função permite fazer uma pesquisa aproximada de títulos de filmes 
    de um dataframe do IMDB, usando a biblioteca rapidfuzz.
    Args:
        df: dataframe com filmes do IMDB
        nome_filme: string providenciada pelo utilizador para encontrar um filme
        limite: número de resultados que o utilizador deseja ver
        similaridade: percentagem de semelhança entre nome_filme e o título encontrado
    Returns:
        Lista com os resultados encontrados, em que cada resultado é um dicionário no qual
        cada chave corresponde a um parâmetro do filme dado pelo dataframe, à exceção de "semelhanca" que indica a 
        percentagem de semelhanca entre o nome indicado pelo utlizador e o título real do filme.
    """

    top_matches = process.extract(
        nome_filme, 
        df['Movie Name'], 
        scorer=fuzz.WRatio, 
        processor=utils.default_process,
        limit=limite,
        score_cutoff=similaridade
    )

    filmes = [] # Lista com os resultados de process.extract()
                # (título no dataframe, valor de similaridade, índice do título no dataframe)

    for titulo, score, indice in top_matches:
        ano = df.iloc[indice]["Year of Release"]
        rating = df.iloc[indice]["Movie Rating"]
        duracao = df.iloc[indice]["Watch Time"]
        sinopse = df.iloc[indice]["Description"]
        filmes.append({
            "titulo": titulo,
            "ano": ano,
            "semelhanca": score,
            "rating": rating,
            "duracao": duracao,
            "sinopse": sinopse
        })
    
    return filmes