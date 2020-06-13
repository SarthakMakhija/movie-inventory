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


def run_tests_in(directory: str):
    os.system(f"python3 -m unittest discover -s tests/{directory}/")


@manager.command
def unit():
    run_tests_in("unit")


@manager.command
def integration():
    docker_compose_up()
    time.sleep(5)
    run_migrations()
    run_tests_in("integration")
    docker_compose_down()


@manager.command
def all():
    unit()
    integration()


if __name__ == "__main__":
    manager.run()
