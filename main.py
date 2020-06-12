from flaskr.configuration import Configuration
from flaskr.flask_application import Application

application = Application.create_app(Configuration)
app = application.flask_application

from flaskr.rest_resource_registry import RestResourceRegistry
RestResourceRegistry(app.api)
