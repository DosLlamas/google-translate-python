from flask import Flask
from flask_dropzone import Dropzone
from flask_session import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "0b66c1464ffb88cf42ac93ab1c613e0431f0b51cd8c0fda1a784774ebdfc"
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)
dropzone = Dropzone(app)

dir_path = os.path.dirname(os.path.realpath(__file__))
app.config.update(
    UPLOADED_PATH = os.path.join(dir_path, "static/uploaded_files/"),
    DROPZONE_ALLOWED_FILE_TYPE = "image",
    DROPZONE_MAX_FILE_SIZE = 3,
    DROPZONE_MAX_FILES = 1,
    AUDIO_FILE_UPLOAD = os.path.join(dir_path, 'static/audio_files/')
)
app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

from application import routes