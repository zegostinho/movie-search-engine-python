import pandas as pd

def carregar_dataset(path):
    """
    Função para carregar o dataframe com filmes do IMDB.
    Args:
        path: caminho para o ficheiro csv que se pretende carregar.
    Returns: ficheiro csv
    """
    df = pd.read_csv(path, sep=',')

    return df

def tratamento_dados(df):
    """
    Função para tratar os dados da coluna 'Year of Release',
    que são do tipo object e misturam números com letras.
    Esta função permite eliminar as letras, de modo a manter o número intacto,
    que representa o ano de lançamento do filme, e também alterar o tipo
    object para tipo int.
    Args:
        df: dataframe com dados a ser tratados
    Returns: dataframe com os dados tratados na coluna 'Year of Release'
    """
    df['Year of Release'] = (df['Year of Release']
                             .apply(lambda x: "".join(c for c in x if c.isdigit()))
                             .astype(int)
                             )

    return df