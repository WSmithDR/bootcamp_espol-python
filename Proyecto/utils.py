import pandas as pd

def cargar_csv(filename):
    # Esta funcion debe leer un archivo csv y retornar un dataframe
    return pd.read_csv(filename)

def cargar_tsv(filename):
    # Esta funcion debe leer un archivo tsv y retornar un dataframe
    return pd.read_csv(filename, sep="\t")

def cargar_cabecera(df):
    # Esta funcion debe recibir un dataframe y devolver la cabecera del mismo
    return df.head()

def obtener_columnas(df):
    # Esta funcion debe recibir un dataframe y devolver las columnas del dataframe
    return df.columns.tolist()

def obtener_estadistica_basica(df,columna):
    # Esta funcion debe recibir un dataframe y devolver las estadisticas de una
    # columna 
    return df[columna].describe()

def _obtener_valores_atipicos(df, columna_valor, columna_nombre):
    Q1 = df[columna_valor].quantile(0.25)
    Q3 = df[columna_valor].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return df[(df[columna_valor] < lower_bound) | (df[columna_valor] > upper_bound)][[columna_nombre, columna_valor]]

def encontrar_peliculas_con_valores_atipicos():
    # Debe leer los archivos necesarios para obtener
    # los valores atipicos en numeros de votos y obtener el nombre
    # de las peliculas que tienes estos valores atipicos
    # esta funcion debe retornar un dataframe que contenga las 
    # peliculas con valores atipicos
   df_ratings = cargar_tsv('title.ratings.tsv')
   df_basics = cargar_tsv('title.basics.tsv')
   df = pd.merge(df_ratings, df_basics[['tconst', 'primaryTitle']], on='tconst')
   return _obtener_valores_atipicos(df, 'numVotes', 'primaryTitle')

def _contar_por_categoria(df, columna, separador):
    df[columna] = df[columna].fillna('').str.split(separador)
    categorias = df[columna].explode()
    conteo = categorias.value_counts().reset_index()
    conteo.columns = [columna, 'cantidad']
    return conteo

def obtener_cantidad_peliculas_por_genero():
    # Debe generar un dataframe que contenga la cantidad de peliculas
    # para cada genero, la columna de la cantidad de peliculas debe
    # tener el nombre de cantidad, mientras que la columna de genero
    # debe llamarse genero
    df = cargar_tsv('title.basics.tsv')
    df_generos = _contar_por_categoria(df, 'genres', ',')
    # Aseguramos que las columnas se llamen 'genres' y 'cantidad'
    df_generos.columns = ['genres', 'cantidad']
    return df_generos

def obtener_top_5_peliculas_con_mas_bajo_rating():
    # Debe generar un dataframe que contenga las 5 peliculas
    # con el peor raiting 
    df_ratings = cargar_tsv('title.ratings.tsv')
    df_basics = cargar_tsv('title.basics.tsv')
    df = pd.merge(df_ratings, df_basics[['tconst', 'primaryTitle']], on='tconst')
    return df.sort_values('averageRating').head(5)[['primaryTitle', 'averageRating']]