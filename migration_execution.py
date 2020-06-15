from typing import Type

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flaskr.configuration import Configuration
from flaskr.entity import db
from flaskr.flask_application import Application


class MigrationExecution:
    def __init__(self, config: Type[Configuration]):
        self.__config = config

    def migration_manager(self) -> Manager:
        app = Application.init_app(self.__config).flask_application
        Migrate(app, db)
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)
        return manager
