import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MODEL_PATH = os.path.join("saved_models", "malaria_model.joblib")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
