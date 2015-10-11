from flask import Flask
from flask_compressor import Compressor
from flask_material import Material
from flask_login import LoginManager
from pymongo import MongoClient
app = Flask(__name__,template_folder='../templates')
client = MongoClient('mongodb://localhost/')
database = client.calibrary
compressor = Compressor(app)
Material(app)
app.debug = True
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
import MiniProject.views