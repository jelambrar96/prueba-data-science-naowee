import duckdb
import pandas as pd


def create_duckdb_connection(
        db_path: str = ":memory:",
        read_only: bool = False) -> duckdb.DuckDBPyConnection:
    """
    Crea una conexión a una base de datos DuckDB.

    Args:
        db_path (str): Ruta al archivo de la base de datos DuckDB. Por defecto es ":memory:" para una base de datos en memoria.

    Returns:
        duckdb.DuckDBPyConnection: Objeto de conexión a DuckDB.
    """
    conn = duckdb.connect(database=db_path, read_only=read_only)
    return conn


def create_duckdb_schema(conn: duckdb.DuckDBPyConnection, schema_name: str) -> None:
    """
    Crea un esquema en la base de datos DuckDB si no existe.

    Args:
        conn (duckdb.DuckDBPyConnection): Objeto de conexión a DuckDB.
        schema_name (str): Nombre del esquema a crear.
    """
    conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")


def create_duckdb_table_from_csv(
    conn: duckdb.DuckDBPyConnection,
    table_name: str,
    csv_path: str,
    schema_name: str = "public",
    delimiter: str = ",",
    header: bool = True,
) -> None:
    """
    Crea una tabla en DuckDB a partir de un archivo CSV.

    Args:
        conn (duckdb.DuckDBPyConnection): Objeto de conexión a DuckDB.
        table_name (str): Nombre de la tabla a crear.
        csv_path (str): Ruta al archivo CSV.
        schema_name (str): Nombre del esquema donde se creará la tabla. Por defecto es "public".
        delimiter (str): Delimitador utilizado en el archivo CSV. Por defecto es ",".
        header (bool): Indica si el archivo CSV tiene una fila de encabezado. Por defecto es True.
    """
    header_option = "TRUE" if header else "FALSE"
    conn.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS
        SELECT * FROM read_csv_auto('{csv_path}', delim='{delimiter}', header={header_option});
        """
    )


def duckdb_table_to_df(
    conn: duckdb.DuckDBPyConnection,
    table_name: str,
    schema_name: str = "public"
) -> pd.DataFrame:
    """
    Convierte una tabla de DuckDB a un DataFrame de pandas.

    Args:
        conn (duckdb.DuckDBPyConnection): Objeto de conexión a DuckDB.
        table_name (str): Nombre de la tabla a convertir.
        schema_name (str): Nombre del esquema donde se encuentra la tabla. Por defecto es "public".

    Returns:
        pandas.DataFrame: DataFrame que contiene los datos de la tabla.
    """
    query = f"SELECT * FROM {schema_name}.{table_name};"
    df = conn.execute(query).df()
    return df


def df_to_duckdb_table(
    conn: duckdb.DuckDBPyConnection,
    df: pd.DataFrame,
    table_name: str,
    schema_name: str = "public"
) -> None:
    """
    Crea una tabla en DuckDB a partir de un DataFrame de pandas.

    Args:
        conn (duckdb.DuckDBPyConnection): Objeto de conexión a DuckDB.
        df (pandas.DataFrame): DataFrame que contiene los datos a insertar en la tabla.
        table_name (str): Nombre de la tabla a crear.
        schema_name (str): Nombre del esquema donde se creará la tabla. Por defecto es "public".
    """
    conn.execute(f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS SELECT * FROM df;")
