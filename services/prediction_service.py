import pandas as pd

from utils.model_loader import ModelLoader


class PredictionService:

    @staticmethod
    def predict(form_data):

        model = ModelLoader.load_model()

        input_data = pd.DataFrame([form_data])

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0]
        
        stay_probability = probability[0] * 100
        churn_probability = probability[1] * 100

        return prediction, stay_probability, churn_probability