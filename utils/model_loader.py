import joblib
from config import MODEL_PATH


class ModelLoader:

    _model = None

    @classmethod
    def load_model(cls):

        if cls._model is None:

            cls._model = joblib.load(MODEL_PATH)

        return cls._model