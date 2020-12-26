from flask import Flask
from delivery.extensions import site 

def create_app():
  app = Flask(__name__)
  site.init_app(app)
  # app.register_blueprint(bp)
  return app