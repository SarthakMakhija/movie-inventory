from flask_migrate import Migrate

from flaskr.entity import db
from flaskr.flask_application import Application
from tests.configuration.TestConfiguration import TestConfiguration

application = Application(TestConfiguration)
app = application.flask_application

migrate = Migrate(app, db)
