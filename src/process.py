import pandas as pd
import pandera as pa
from sklearn import preprocessing

def preprocesado(df: pd.DataFrame) -> pd.DataFrame:
    """

    Tomamos los valores de entrada y escalamos los datos

    Args:
        df (pd.DataFrame): DataFrame de entrada con las columnas
            del Iris dataset.

    Returns:
        pd.DataFrame: DataFrame escalado
    """

    schema = pa.DataFrameSchema(
        columns={
            'sepal_length': pa.Column(float),
            'sepal_width': pa.Column(float),
            'petal_length': pa.Column(float),
            'petal_width': pa.Column(float),
        }
    )

    try:
        schema(df)
        col_list = list(schema.columns.keys())

        # El esquema es válido
        scaled = preprocessing.StandardScaler().fit_transform(df[col_list])
        df_scaled = pd.DataFrame(scaled, columns=col_list)

        return pd.concat([df_scaled, df.drop(columns=col_list)], axis=1)
    except pa.errors.SchemaError as exc:
        print(exc)
