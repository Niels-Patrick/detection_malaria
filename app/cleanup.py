import os
from config import Config
import shutil

def cleanup_upload_folder():
    if os.path.exists(Config.UPLOAD_FOLDER):
        shutil.rmtree(Config.UPLOAD_FOLDER)
        print("Upload folder cleaned up.")