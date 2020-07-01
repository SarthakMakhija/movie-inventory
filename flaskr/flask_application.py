from __future__ import annotations

from typing import Type

from core.entrypoint import init_app
from flaskr.configuration import Configuration
from flaskr.entity import db
from flaskr.rest_resource_registry import RestResourceRegistry


class Application:

    @staticmethod
    def create_app(config: Type[Configuration]):
        core_application = init_app(config)
        app = core_application.flask_application

        db.init_app(app)

        RestResourceRegistry(core_application.api)

        return app
