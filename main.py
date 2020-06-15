from flaskr.configuration import Configuration
from flaskr.flask_application import Application

application = Application.init_app(Configuration)
app = application.flask_application
