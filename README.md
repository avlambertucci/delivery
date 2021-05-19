# curso-flask
Repositorio Curso Flask - https://skip.gg/curso-flask-codeshow
# Activating venv on bash shell
. venv/Scripts/activate

# Run server
export FLASK_APP=delivery/app.py
flask run
# Run test
pytest tests -v

# Default folders
delivery
    -extensions
    -static (js, img and css)
    -templates (html)
