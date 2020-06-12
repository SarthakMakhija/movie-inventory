import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("tests"), '.')))

from migration_execution import MigrationExecution
from tests.configuration.configuration_test import TestConfiguration


class TestMigrationExecution(MigrationExecution):
    def __init__(self):
        super().__init__(TestConfiguration)


if __name__ == '__main__':
    TestMigrationExecution().migration_manager().run()
