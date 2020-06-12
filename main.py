from flaskr.configuration import Configuration
from flaskr.flask_application import Application

application = Application(Configuration)
app = application.flask_application
