from flask import Flask
from delivery.extensions import site 
from delivery.extensions import toolbar
from delivery.extensions import config

# Def that creates an app
def create_app():
  app = Flask(__name__)
  config.init_app(app)
  toolbar.init_app(app)
  # Calling the registered blueprints
  site.init_app(app)
  
  return app