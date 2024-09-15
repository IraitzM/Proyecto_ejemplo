import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

clases = ["Setosa", "Versicolor", "Virginica"]

class Measurements(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

def predict(features):
    """
    Usa los modelos entrenados para predecir

    Args:
        features (list): DataFrame de entrada con las columnas
            del Iris dataset.

    Returns:
        float: Predicción del modelo
    """

    # Scaled
    df = pd.DataFrame(features, columns=['sepal_length','sepal_width','petal_length','petal_width'])
    scaler = joblib.load("./model/scaler.joblib")
    x = scaler.transform(df)

    # Model
    df = pd.DataFrame(x, columns=['sepal_length','sepal_width','petal_length','petal_width'])
    model = joblib.load("./model/best_model.joblib")
    return model.predict(df)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris API! You will find the documentation at /docs"}

@app.post("/predict")
def predict_endpoint(measurements: Measurements):
    """
    ### Iris predictor
    
    Usa los modelos entrenados para predecir la clase a la que pertenece una flor.

    Devuelve la clase correspondiente a _Setosa_, _Virgínica_ o _Versicolor_
    """

    prediction = predict([[measurements.sepal_length, measurements.sepal_width, measurements.petal_length, measurements.petal_width]])

    return {"prediction": clases[int(prediction)]}

