import os
import time

from flask_script import Manager

from main import app

manager = Manager(app)


def docker_compose_up():
    base_directory = os.getcwd()
    os.system(f"docker-compose -f {base_directory}/tests/docker-compose.yml up -d")


def docker_compose_down():
    base_directory = os.getcwd()
    os.system(f"docker-compose -f {base_directory}/tests/docker-compose.yml down")


def run_migrations():
    base_directory = os.getcwd()
    os.system(f"python3 {base_directory}/tests/migration/migration_execution_test.py db upgrade")


def run_integration_test():
    os.system(f"python3 -m unittest discover -s tests/ -p test_integration_*.py")


def run_unit_test():
    os.system(f"python3 -m unittest discover -s tests/ -p test_unit_*.py")


@manager.command
def unit():
    run_unit_test()


@manager.command
def integration():
    docker_compose_up()
    time.sleep(5)
    run_migrations()
    run_integration_test()
    docker_compose_down()


@manager.command
def all():
    unit()
    integration()


if __name__ == "__main__":
    manager.run()
