from flaskr.configuration import Configuration
from flaskr.flask_application import Application

app = Application.create_app(Configuration)