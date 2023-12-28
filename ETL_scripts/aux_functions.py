# Funciones de apoyo para ETL desde CSV hacia PostgreSQL.
from sqlalchemy import create_engine, text
import pandas as pd

def credentials(path: str) -> dict:
    """Funcion que genera un diccionario con credenciales
    para conectarse a BBDD de origen y de destino.
    Args:
        path (str): Ruta (string) con las credenciales.
    Returns:
        cred (dict): Diccionario con las credenciales.
    """
    import json
    with open(path + "/credentials/credentials.json") as file_credentials:
        cred = json.load(file_credentials).copy()      
    return cred

def update_to_sql(df:pd.DataFrame, table_name:str, key_name:str, engine) -> str:
    """Funcion que actualiza tabla destino con modificaciones.
    Args:
        df (DataFrame): DataFrame con los registros a actualizar.
        table_name (string): Nombre de la tabla a actulizar.
        key_name (string): Nombre del campo clave de la tabla a actualizar.
        engine (engine): Objeto de SQLAlchemy que genera la conexion de Python 
        a PostgreSQL.
    Returns:
        update_len (string): Cantidad de registros a actualizar.
    """
    if len(df) > 0:
        a = []
        update_len = str(len(df.copy()))
        table = table_name
        primary_key = key_name
        temp_table = f"{table_name}_temporary_table"
        for col in df.columns:
            if col == primary_key:
                continue
            a.append(f'"{col}"=s."{col}"')
        df.to_sql(temp_table, engine, if_exists='replace', index=False)
        update_stmt_1 = f'UPDATE public."{table}" f '
        update_stmt_2 = "SET "
        update_stmt_3 = ", ".join(a)
        update_stmt_4 = f' FROM public."{table}" t '
        update_stmt_5 = f' INNER JOIN (SELECT * FROM public."{temp_table}") \
            AS s ON s."{primary_key}"=t."{primary_key}" '
        update_stmt_6 = f' Where f."{primary_key}"=s."{primary_key}" '
        update_stmt_7 = text(update_stmt_1 + update_stmt_2 + update_stmt_3 + update_stmt_4 \
            + update_stmt_5 +  update_stmt_6 +";")
        with engine.begin() as cnx:
            cnx.execute(update_stmt_7)
        drop_temp = text(f'DROP TABLE public.{temp_table}')
        with engine.begin() as cnx:
            cnx.execute(drop_temp)
    else: 
        update_len = '0'
    return update_len

def insert_to_sql(df:pd.DataFrame, table_name:str, engine) -> str:
    """Funcion que agrega nuevos registros a tabla destino.
    Args:
        df (DataFrame): DataFrame con los registros a insertar.
        table_name (string): Nombre de la tabla a la cual se haran insertos de data.
        engine (engine): Objeto de SQLAlchemy que genera la conexion de Python 
        a PostgreSQL.
    Returns:
        insert_len (string): Cantidad de registros a insertar.
    """
    if len(df) > 0:
        insert_len = str(len(df.copy()))
        df.to_sql(table_name, con = engine, method = 'multi',
        index = False, if_exists = 'append', chunksize = len(df.copy())//2 + 1)
    else: 
        insert_len = '0'
    return insert_len