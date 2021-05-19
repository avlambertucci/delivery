from flask import Flask
from delivery.extensions import site 

# Def that creates an app
def create_app():
  app = Flask(__name__)
  # Calling the registered blueprints
  site.init_app(app)
  # app.register_blueprint(bp)
  return app