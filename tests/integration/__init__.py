from flaskr.flask_application import Application
from tests.configuration.configuration_test import TestConfiguration

application = Application.init_app(TestConfiguration)
app = application.flask_application
